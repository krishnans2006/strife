function processMessageKeydown(input) {
    if (event.key === 'Enter') {
        event.preventDefault();
        sendSocketMessage();
    }
}
