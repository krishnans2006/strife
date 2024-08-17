// Messages-specific socket functions

function sendFile(fileObj, fileData, messageID) {
    const fileMetadata = JSON.stringify({
        name: fileObj.name,
        type: fileObj.type,
        size: fileObj.size,
        messageID: messageID,
    });

    const enc = new TextEncoder();
    const prefix = enc.encode('!file!');
    const metadata = enc.encode(fileMetadata);
    const separator = enc.encode('!');
    const data = fileData;

    let toSend = new Uint8Array(prefix.byteLength + metadata.byteLength + separator.byteLength + data.byteLength);
    toSend.set(new Uint8Array(prefix), 0);
    toSend.set(new Uint8Array(metadata), prefix.byteLength);
    toSend.set(new Uint8Array(separator), prefix.byteLength + metadata.byteLength);
    toSend.set(new Uint8Array(data), prefix.byteLength + metadata.byteLength + separator.byteLength);

    socket.binaryType = 'arraybuffer';
    socket.send(toSend);
    socket.binaryType = 'blob';
}

function sendSocketAttachments() {
    if (uploadedFiles.length > 0) {
        // Use FileReader and ArrayBuffer to send files
        for (let i = 0; i < uploadedFiles.length; i++) {
            const file = uploadedFiles[i];
            const reader = new FileReader();

            reader.onload = function (e) {
                let rawData = new ArrayBuffer();
                rawData = e.target.result;

                sendFile(file, rawData, lastMessage.id);
            };

            reader.readAsArrayBuffer(file);
        }

        uploadedFiles = [];
        $('#attachments-view').empty();
    }
}

function sendSocketMessage() {
    let contentInput = $('#send-message #content')[0];

    if (contentInput.value) {
        contentInput.disabled = true;

        let data = {
            type: 'message',
            content: contentInput.value,
        };

        lastMessageIDBeforeSend = lastMessage ? lastMessage.id : -1;

        socket.send(JSON.stringify(data));

        function waitForMessageUpdateThenUploadAttachments() {
            if (lastMessageIDBeforeSend === (lastMessage ? lastMessage.id : -1) || lastMessage.author.id !== parseInt(USER_ID)) {
                setTimeout(waitForMessageUpdateThenUploadAttachments, 100);
                return;
            }
            sendSocketAttachments();
        }

        waitForMessageUpdateThenUploadAttachments();

        contentInput.value = '';
        contentInput.disabled = false;
        contentInput.focus();
    }
}
