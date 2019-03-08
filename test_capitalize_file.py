import unittest
import capitalize_file
class TestCapitalize(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = capitalize_file.captitalize_text(text)
        self.assertEqual(result,'Python')
    def test_multiple_word(self):
        text = 'python is growing'
        result = capitalize_file.captitalize_text(text)
        self.assertEqual(result,'Python is growing')
if __name__ == '__main__':
    unittest.main()
