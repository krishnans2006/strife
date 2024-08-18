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

    userProfile.removeClass('hidden');
}
