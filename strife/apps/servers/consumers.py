import json

from strife.apps.home.consumers import GenericConsumer

from .models import Server


class ServerConsumer(GenericConsumer):
    def initialize(self):
        # Set parameters
        self.server_id = self.scope["url_route"]["kwargs"]["server_id"]
        assert self.server_id

        self.server = Server.objects.get(id=self.server_id)
        assert self.server.members.filter(user=self.user).exists()

        # Register supported types
        self.supported_types_json["req_member"] = self.handle_req_member_payload

    def handle_req_member_payload(self, payload):
        # Don't need to check permissions here; the user is already in the server

        # Get member info
        member_id = payload["member_id"]
        member = self.server.members.get(id=member_id)

        # Send the member info
        self.send(
            text_data=json.dumps(
                {
                    "type": "member",
                    "member": member.to_dict(),
                }
            )
        )
