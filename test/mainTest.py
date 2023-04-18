import unittest

from alfred_to_csv_converter import create_snippet_data, create_snippet_extra_data


class TestAlfredCSVConverter(unittest.TestCase):

    def test_create_snippet_data(self):
        content = {
            "alfredsnippet": {
                "name": "test snippet",
                "keyword": "test",
                "snippet": "print('Hello, world!')",
            }
        }
        folder_name = "test_folder"
        expected_output = "test snippet,test,print('Hello, world!'),test_folder"
        self.assertEqual(create_snippet_data(content, folder_name), expected_output)

    def test_create_snippet_extra_data(self):
        content = {
            "snippetkeywordprefix": "test",
            "snippetkeywordsuffix": "",
        }
        folder_name = "test_folder"
        expected_output = "test,,test_folder"
        self.assertEqual(create_snippet_extra_data(content, folder_name), expected_output)


if __name__ == '__main__':
    unittest.main()
