import unittest
from powerlib.configurations.model import Configuration


class ConfigurationTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_merge(self):
        config_1 = Configuration({'a': 1, 'b': 2, 'c': {'ca': "Hello"}})
        config_2 = Configuration({'a': 2, 'c': {'cb': "World"}, 'd': 3})
        expected = Configuration({'a': 2, 'b': 2, 'c': {'cb': "World"}, 'd': 3})
        self.assertEqual(config_1.merge(config_2), expected)

    def test_configuration_getitem_is_configuration(self):
        config = Configuration({'a': 1, 'b': 2, 'c': {'ca': "Hello"}})
        child_config = config['c']
        self.assertTrue(isinstance(child_config, Configuration))

    def test_configuration_get_is_configuration(self):
        config = Configuration({'a': 1, 'b': 2, 'c': {'ca': "Hello"}})
        child_config = config.get('c')
        self.assertTrue(isinstance(child_config, Configuration))
