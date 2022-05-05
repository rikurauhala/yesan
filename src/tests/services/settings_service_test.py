import unittest

from services.settings_service import SettingsService


class TestSettingsService(unittest.TestCase):
    def setUp(self):
        self._settings_service = SettingsService()

    def test_import_settings(self):
        content = self._settings_service.import_settings()

        self.assertEqual(len(content), 19)

    def test_export_settings(self):
        content = self._settings_service.import_settings()
        success = self._settings_service.export_settings(content)

        self.assertTrue(success)
