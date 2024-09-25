import unittest

from lib import Container
from lib import Module
from lib.loaders import FileLoader


class TestContainer(unittest.TestCase):
    def test_add_definitions(self):
        Container.add_definitions({"version": "hello"})
        self.assertEqual(Container.config, {"version": "hello"})

    def test_get(self):
        Container.add_definitions({"version": "hello"})
        self.assertEqual(Container.get("version"), "hello")

    def test_get_with_class_name(self):
        Container.add_definitions({Module.__name__: FileLoader([])})
        self.assertIsInstance(Container.get(Module.__name__), FileLoader)

    def test_get_with_another_key(self):
        self.assertEqual(Container.get('test'), None)
        