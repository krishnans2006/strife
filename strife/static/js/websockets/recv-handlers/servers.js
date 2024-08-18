// These are used by the onmessage function in index.js
// Requires: users/avatars.js

function memberHandler(member) {
    populatePopup(member);
}

function userHandler(user) {
    populatePopup(user);
}

function changeRolesHandler(member) {
    updatePopupRoles(member);
}
