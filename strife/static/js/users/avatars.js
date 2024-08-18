$('#js-user-profile').on('click', function (e) {
    // If it's the modal itself, do nothing
    if (e.target != this) {
        return;
    }

    // Hide the modal and backdrop
    $(this).addClass('hidden');
});
