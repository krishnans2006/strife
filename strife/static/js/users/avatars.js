const userProfile = $('#js-user-profile');

userProfile.on('click', function (e) {
    // If it's the modal itself, do nothing
    if (e.target != this) {
        return;
    }

    // Hide the modal and backdrop
    $(this).addClass('hidden');
});


function populatePopup(user) {
    // Make sure element with id js-user-profile exists
    if (userProfile.length < 0) {
        return;
    }

    // const container = $('#js-user-profile-container');
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
        $(".js-user-profile-member-only-div").removeClass("hidden").data('member-id', user.id);

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

    userProfile.data('user-id', user.id);
    userProfile.removeClass('hidden');
}


function updatePopupRoles(member) {
    // Make sure we're getting a member (with roles)
    if (!member.is_serverized) {
        return;
    }

    // Make sure there's a popup present
    if (userProfile.length < 0) {
        return;
    }

    // Make sure they haven't closed the popup
    if (userProfile.hasClass('hidden')) {
        return;
    }

    // Make sure the popup is for the same user
    const popupUserId = userProfile.data('user-id');
    if (parseInt(popupUserId) !== member.id) {
        return;
    }

    // Clear roles from previous popups
    $('.js-user-profile-role').remove();

    $(".js-user-profile-member-only-div").removeClass("hidden").data('member-id', member.id);

    if (member.roles.length === 0) {
        $("#js-user-profile-no-roles").removeClass("hidden");
    } else {
        for (role of member.roles) {
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
