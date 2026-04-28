PROFILE_FIELDS_HOOK = "profile.fields"


class SteamService:
    def __init__(self, module):
        self.module = module

    def register_hooks(self):
        self.module.register_hook_provider(PROFILE_FIELDS_HOOK, self.build_profile_fields)

    def unregister_hooks(self):
        self.module.unregister_hook_provider(PROFILE_FIELDS_HOOK)

    def build_profile_fields(self, ctx, member, user_data, server_data):
        steam_id = user_data.get("steam")
        if not steam_id:
            return []

        steam_label = str(steam_id)
        try:
            summary = self.module.get_player_summary(str(steam_id))
            if summary and summary.get("personaname"):
                steam_label = summary["personaname"]
        except Exception:
            pass

        return [
            {
                "name": "Профиль Steam",
                "value": f"[{steam_label}](https://steamcommunity.com/profiles/{steam_id})",
            }
        ]
