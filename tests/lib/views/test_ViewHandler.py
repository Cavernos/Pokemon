import os
from pathlib import Path
from unittest import TestCase

from app.MainMenuModule.views import HomeView
from lib import Container
from lib.views import ViewHandler


class TestViewHandler(TestCase):
    def setUp(self):
        Container.add_definitions(os.path.join(Path(os.path.dirname(__file__)).parent.parent.parent, "config", "config.py"))
        self.view_handler = ViewHandler()

    def test_set_view(self):
        self.view_handler.set_view(HomeView)
        self.assertIsInstance(self.view_handler.get_view(), HomeView)

    def test_error_set_view(self):
        self.assertEqual(self.view_handler.set_view(HomeView), "")
