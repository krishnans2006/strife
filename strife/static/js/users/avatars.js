// User avatar popup
$(document).ready(() => {
    $('.user-icon-popup-link').click((e) => {
        const profile = $(e.currentTarget).parent().find('.user-icon-popup');
        profile.toggleClass('hidden');
    });

    $('.user-profile-backdrop').click(() => {
        $('.user-profile-backdrop').parent().addClass('hidden');
    });
});
