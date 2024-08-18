function sendMemberRequest() {
    socket.send(JSON.stringify({
        'type': 'req_member',
        'member_id': this.dataset.member_id
    }));
}
