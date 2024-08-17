const socket = new WebSocket(`ws://${GET_HOST}/ws/messages/${SERVER_ID}/${CHANNEL_ID}/`);

socket.onopen = function (e) {
    console.log('Message socket connected');
}

function addMessage(message) {
    const messageList = $('#message-list-div')[0];

    // Any updates here should also be done to messages/detail.html
    messageList.innerHTML += `
          <div id="message-${message.id}" class="w-full px-5 py-1 justify-center flex flex-row gap-3.5 relative">
            <a id="message-${message.ID}-user-icon" class="cursor-pointer user-icon-popup-link">
              <img class="size-10 flex-none aspect-square object-cover rounded-full mt-1"
                   src="${message.author.display_avatar}" alt="${message.author.username}">
              <div class="hidden user-icon-popup" id="message-${message.id}-profile">
                {% include 'users/profile.html' with user=message.author %}
              </div>
            </a>
            <div id="message-${message.id}-child" class="grow text-gray-300 flex flex-col">
              <h4 class="text-lg font-bold">${message.author.username}</h4>
              <p>${message.content}</p>

              ${message.attachments.length > 0 ? `
                <div id="message-${message.id}-attachments" class="flex flex-row gap-3.5">
                  ${message.attachments.map((attachment) => `
                    <a href="${attachment.download_url}" target="_blank" class="inline-block min-w-20 py-1 px-2.5 rounded-xl bg-gray-700 text-white cursor-pointer">${attachment.name}</a>
                  `).join('')}
                </div>
              ` : ''}
            </div>
          </div>
        `;

    lastMessage = message;
}

function updateAttachments(message) {
    const messageChildDiv = $(`#message-${message.id}-child`)[0];
    const attachmentsDiv = $(`#message-${message.id}-attachments`)[0];

    if (attachmentsDiv) {
        attachmentsDiv.innerHTML = message.attachments.map((attachment) => `
                <a href="${attachment.download_url}" target="_blank" class="inline-block min-w-20 py-1 px-2.5 rounded-xl bg-gray-700 text-white cursor-pointer">${attachment.name}</a>
            `).join('');
    } else {
        messageChildDiv.innerHTML += `
                <div id="message-${message.id}-attachments" class="flex flex-row gap-3.5">
                    ${message.attachments.map((attachment) => `
                        <a href="${attachment.download_url}" target="_blank" class="inline-block py-1 px-2.5 rounded-xl bg-gray-700 text-white cursor-pointer">${attachment.name}</a>
                    `).join('')}
                </div>
            `;
    }
}

socket.onmessage = function (e) {
    const data = JSON.parse(e.data);

    if (data.type === 'message') {
        addMessage(data.message);
    } else if (data.type === 'attachment') {
        updateAttachments(data.message);
    }
}

socket.onclose = function (e) {
    console.error('Message socket closed unexpectedly');
}

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
