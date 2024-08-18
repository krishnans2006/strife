// These are used by the onmessage function in index.js
// Requires: users/avatars.js

function memberHandler(member) {
    populatePopup(member);
}

function userHandler(user) {
    populatePopup(user);
}

function changeRolesHandler(data) {
    const member = data.member;
    const roles = data.roles;

    const memberRow = document.getElementById(`member-${member.id}`);
    const rolesList = memberRow.querySelector('.roles-list');

    rolesList.innerHTML = '';
    roles.forEach(role => {
        const roleElement = document.createElement('li');
        roleElement.textContent = role;
        rolesList.appendChild(roleElement);
    });
}
