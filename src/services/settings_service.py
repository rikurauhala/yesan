from file_handler import file_handler


class SettingsService:
    """Handles all functionality related to settings."""

    def __init__(self):
        """Initializes a new instance of SettingsService."""

    def import_settings(self, default=False):
        """Imports settings from the .env file.

        Returns:
            List: Rows containing the contents of the env. file.
        """
        return file_handler.import_settings(default)

    def export_settings(self, content):
        """Exports settings into the .env file.

        Args:
            content (List): Rows containing the contents of the Text object in the Settings view.

        Returns:
            Boolean: True if the operation succeeded as expected.
        """
        return file_handler.export_settings(content)


settings_service = SettingsService()
