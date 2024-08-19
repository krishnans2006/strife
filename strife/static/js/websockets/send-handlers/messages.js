// Messages-specific socket functions

function sendAttachments(message_id) {
    if (uploadedFiles.length > 0) {
        // Use FileReader and ArrayBuffer to send files
        for (let i = 0; i < uploadedFiles.length; i++) {
            const file = uploadedFiles[i];

            let formData = new FormData();
            formData.append('file', file);

            // POST to be processed by Django
            $.ajax({
                url: `/servers/${SERVER_ID}/channels/${CHANNEL_ID}/messages/${message_id}/attachments/upload/`,
                type: 'POST',
                data: formData,
                processData: false,
                contentType: false,
            });
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
            sendAttachments(lastMessage.id);
        }

        waitForMessageUpdateThenUploadAttachments();

        contentInput.value = '';
        contentInput.disabled = false;
        contentInput.focus();
    }
}
