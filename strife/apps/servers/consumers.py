import json

from strife.apps.home.consumers import GenericConsumer

from .models import Server


class ServerConsumer(GenericConsumer):
    def initialize(self):
        super().initialize()

        # Set parameters
        self.server_id = self.scope["url_route"]["kwargs"]["server_id"]
        assert self.server_id

        self.server = Server.objects.get(id=self.server_id)
        assert self.server.members.filter(user=self.user).exists()

        # Register supported types
        self.supported_types_json["req_member"] = self.handle_req_member_payload
        self.supported_types_json["add_role"] = self.handle_add_role_payload
        self.supported_types_json["remove_role"] = self.handle_remove_role_payload

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
                    "error": False,
                    "member": member.to_dict(),
                }
            )
        )

    def handle_add_role_payload(self, payload):
        # Check permissions
        if not self.user.as_serverized(self.server_id).can_manage_roles:
            self.send(
                text_data=json.dumps(
                    {
                        "type": "change_roles_res",
                        "error": True,
                        "message": "You do not have permission to manage roles.",
                    }
                )
            )
            return

        # Get member info
        member_id = payload["member_id"]
        member = self.server.members.get(id=member_id)

        # Get role info
        new_role_id = payload["role_id"]
        role = self.server.roles.get(id=new_role_id)

        # Add the role
        member.roles.add(role)
        member.save()

        # Send the member info
        self.send(
            text_data=json.dumps(
                {
                    "type": "change_roles_res",
                    "error": False,
                    "member": member.to_dict(),
                }
            )
        )

    def handle_remove_role_payload(self, payload):
        # Check permissions
        if not self.user.as_serverized(self.server_id).can_manage_roles:
            return

        # Get member info
        member_id = payload["member_id"]
        member = self.server.members.get(id=member_id)

        # Get role info
        old_roles = payload["role"]
        role = self.server.roles.get(name=old_roles)

        if member not in role.members.all():
            return

        # Remove the role
        member.roles.remove(role)
        member.save()

        # Send the member info
        self.send(
            text_data=json.dumps(
                {
                    "type": "change_roles_res",
                    "error": False,
                    "member": member.to_dict(),
                }
            )
        )
