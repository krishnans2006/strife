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
