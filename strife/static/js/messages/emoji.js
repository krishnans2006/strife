function insertAtCursor(myField, myValue) {
    if (document.selection) {
        myField.focus();
        sel = document.selection.createRange();
        sel.text = myValue;
    } else if (myField.selectionStart || myField.selectionStart == '0') {
        var startPos = myField.selectionStart;
        var endPos = myField.selectionEnd;
        myField.value = myField.value.substring(0, startPos)
            + myValue
            + myField.value.substring(endPos, myField.value.length);
        myField.focus();
        myField.selectionStart = startPos + myValue.length;
        myField.selectionEnd = startPos + myValue.length;
    } else {
        myField.value += myValue;
        myField.focus();
    }
}

const emojiPicker = $('#emoji-picker');
const openEmojiPicker = $('#open-emoji-picker');
const messageBox = $('#content');

openEmojiPicker.on('click', () => {
    emojiPicker.toggleClass('hidden');
});

emojiPicker.on('emoji-click', (e) => {
    const emoji = e.detail.unicode;
    const content = $('#content')[0];
    insertAtCursor(content, emoji);
});

messageBox.on('click', () => {
    emojiPicker.addClass('hidden');
});
