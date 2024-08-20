// These are used by the onmessage function in index.js

function messageHandler(message) {
    const messageList = $('#message-list-div')[0];

    // Any updates here should also be done to messages/detail.html
    messageList.innerHTML += `
          <div id="message-${message.id}" class="w-full px-5 py-1 justify-center flex flex-row gap-3.5 flex-none">
            <a>
              <img id="message-${message.ID}-user-icon"
                   class="cursor-pointer size-10 flex-none aspect-square object-cover rounded-full mt-1 user-icon-popup-link"
                   src="${message.serverized_author.display_avatar}"
                   alt="${message.serverized_author.username}"
                   data-user-id="${message.serverized_author.id}"
                   onclick="sendMemberRequest(${message.serverized_author.id})">
            </a>
            <div id="message-${message.id}-child"
                 class="grow text-gray-300 flex flex-col">
              <h4 class="text-lg font-bold">${message.serverized_author.username}</h4>
              <p>${message.content}</p>

              ${message.attachments.length > 0 ? `
                <div id="message-${message.id}-attachments"
                     class="flex flex-row gap-3.5">
                  ${message.attachments.map((attachment) => `
                    <a href="${attachment.download_url}"
                       target="_blank"
                       class="inline-block py-1 px-2.5 rounded-xl bg-gray-700 text-white cursor-pointer">${attachment.name}</a>
                  `).join('')}
                </div>
              ` : ''}
            </div>
          </div>
        `;

    lastMessage = message;
}

function attachmentHandler(message) {
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

function messageEditHandler(message) {
    const messageDiv = $(`#message-${message.id}-child`)[0];

    const textContainer = messageDiv.find('p')[0];
    textContainer.innerHTML = message.content;
}
