// These are used by the onmessage function in index.js

function memberHandler(member) {
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

    image.attr('src', member.display_avatar);
    image.attr('alt', member.username);

    displayName.text(member.display_name);
    username.text(member.username);
    bio.text(member.bio);

    // Clear roles from previous popups
    $('.js-user-profile-role').remove();

    if (member.is_serverized) {
        $(".js-user-profile-member-only-div").removeClass("hidden");

        if (member.roles.length === 0) {
            $("#js-user-profile-no-roles").removeClass("hidden");
        } else {
            for (role of member.roles) {
                $("#js-user-profile-role-example").clone().removeAttr("id").text(role.name).css("background-color", role.color).addClass("js-user-profile-role").appendTo("#js-user-profile-roles-div");
            }
        }
    }

    userProfile.removeClass('hidden');
}
