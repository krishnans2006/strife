function showMessageButtons(message_id) {
    $(`#message-${message_id}-buttons`).removeClass('hidden');
}

function hideMessageButtons(message_id) {
    $(`#message-${message_id}-buttons`).addClass('hidden');
}
