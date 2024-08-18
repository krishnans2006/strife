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
