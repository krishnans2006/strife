function sendMemberRequest(member_id) {
    socket.send(JSON.stringify({
        'type': 'req_member',
        'member_id': member_id
    }));
}
