$('#js-user-profile').on('click', function (e) {
    // If it's the modal itself, do nothing
    if (e.target != this) {
        return;
    }

    // Hide the modal and backdrop
    $(this).addClass('hidden');
});


function populatePopup(user) {
    // Make sure element with id js-user-profile exists
    const userProfile = $('#js-user-profile');

    if (userProfile.length < 0) {
        return;
    }

    const container = $('#js-user-profile-container');
    const image = $('#js-user-profile-image');
    const displayName = $('#js-user-profile-display-name');
    const username = $('#js-user-profile-username');
    const bio = $('#js-user-profile-bio');

    image.attr('src', user.display_avatar);
    image.attr('alt', user.username);

    displayName.text(user.display_name);
    username.text(user.username);
    bio.text(user.bio);

    // Clear roles from previous popups
    $('.js-user-profile-role').remove();

    if (user.is_serverized) {
        $(".js-user-profile-member-only-div").removeClass("hidden");

        if (user.roles.length === 0) {
            $("#js-user-profile-no-roles").removeClass("hidden");
        } else {
            for (role of user.roles) {
                $("#js-user-profile-role-example")
                    .clone()
                    .removeAttr("id")
                    .text(role.name)
                    .css("background-color", role.color)
                    .addClass("js-user-profile-role")
                    .appendTo("#js-user-profile-roles-div");
            }
        }
    }

    userProfile.removeClass('hidden');
}
