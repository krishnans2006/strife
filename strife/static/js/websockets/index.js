// Contains the setup for websocket connections
// These depend on the existence of the `socket` global variable
// So, make sure an initializer is run first

socket.onopen = function (e) {
    console.log('Message socket connected');
}

socket.onmessage = function (e) {
    const data = JSON.parse(e.data);

    if (data.type === 'message') {
        messageHandler(data.message);
    } else if (data.type === 'attachment') {
        attachmentHandler(data.message);
    } else if (data.type === 'member') {
        memberHandler(data.member);
    }
}

socket.onclose = function (e) {
    console.error('Message socket closed unexpectedly');
}
