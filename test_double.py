import unittest

from double import double_characters


class TestDouble(unittest.TestCase):

    def test_double_characters_doubles_characters(self):
        self.assertEqual(double_characters("Martin"), "MMaarrttiinn")

    def test_empty_string_throws_error(self):
        self.assertRaises(ValueError, double_characters, "")