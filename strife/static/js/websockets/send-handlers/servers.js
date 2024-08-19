function sendMemberRequest(member_id) {
    socket.send(JSON.stringify({
        'type': 'req_member',
        'member_id': member_id
    }));
}

function sendUserRequest(user_id) {
    socket.send(JSON.stringify({
        'type': 'req_user',
        'user_id': user_id
    }));
}

function sendRoleAdd(select_element) {
    const element = $(select_element);
    const role_id = element.val();
    const member_id = element.parent().parent().data('member-id');

    socket.send(JSON.stringify({
        'type': 'add_role',
        'role_id': role_id,
        'member_id': member_id
    }));
}

function sendRoleRemove(role_button_element) {
    const element = $(role_button_element).parent();
    const role_id = element.data('role-id');
    const member_id = element.parent().parent().data('member-id');

    socket.send(JSON.stringify({
        'type': 'remove_role',
        'role_id': role_id,
        'member_id': member_id
    }));
}
