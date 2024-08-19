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
        updatePopupServerized(user);
    }

    if (user.user_id === parseInt(USER_ID)) {
        $('.js-user-profile-me-only-div').removeClass('hidden');
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

    updatePopupServerized(member);
}

function getContrastingBW(hex) {
    if (hex.indexOf('#') === 0) {
        hex = hex.slice(1);
    }
    // convert 3-digit hex to 6-digits.
    if (hex.length === 3) {
        hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2];
    }
    if (hex.length !== 6) {
        throw new Error('Invalid HEX color.');
    }
    const r = parseInt(hex.slice(0, 2), 16),
        g = parseInt(hex.slice(2, 4), 16),
        b = parseInt(hex.slice(4, 6), 16);

    // https://stackoverflow.com/a/3943023/11317931
    return (r * 0.299 + g * 0.587 + b * 0.114) > 186
        ? '#000000'  // too bright
        : '#FFFFFF';  // too dark
}

// Only call if the user is serverized
function updatePopupServerized(member) {
    $(".js-user-profile-member-only-div").removeClass("hidden").data('member-id', member.id);

    // Logic for permission-based div visibility here
    if (true) {
        $(".js-user-profile-manage-roles-only-div").removeClass("hidden");
    }

    const roleSelect = $('#js-user-profile-roles-select');

    if (member.roles.length === 0) {
        $("#js-user-profile-no-roles").removeClass("hidden");
    } else {
        $("#js-user-profile-no-roles").addClass("hidden");

        // Show all roles in the dropdown
        $(".js-user-profile-roles-select-role").removeClass("hidden");

        // Then for every role the member already has
        for (const role of member.roles) {
            // Add the role to the popup
            $("#js-user-profile-role-example")
                .clone()
                .attr("id", `js-user-profile-role-${role.id}`)
                .data("role-id", role.id)
                .prepend(role.name)
                .css("background-color", `#${role.color}`)
                .css("color", getContrastingBW(role.color))
                .addClass("js-user-profile-role")
                .removeClass("hidden")
                .appendTo("#js-user-profile-roles-div");
            // Remove it from the dropdown
            $(`#js-user-profile-roles-select-role-${role.id}`).addClass("hidden");
        }
    }

    const numOptions = roleSelect.find("option").length;
    const numHidden = roleSelect.find("option.hidden").length;

    if (numOptions === numHidden) {
        roleSelect.addClass("hidden");
    } else {
        roleSelect.removeClass("hidden");
    }

    roleSelect.val("-1");  // "Add a role"
}
