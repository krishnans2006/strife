// Scroll to bottom
$(document).ready(() => {
    const messageList = $('#message-list')[0];
    messageList.scrollTop = messageList.scrollHeight;
});

// Used in messages/create.html
// And in sendSocketMessage()
let uploadedFiles = [];

// Stores the most recent message
let lastMessage = null;
