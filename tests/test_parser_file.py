# tests/test_parser_file.py

import os
import unittest

from pyparsec import parse_markdown_file, CodeSnippet


class TestParseMarkdownFile(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test_file.md'
        self.markdown_content = """
        # Example Markdown

        Here is some Python code:

        ```python
        def hello_world():
            print("Hello, world!")
        ```

        Here is some JSON:

        ```json
        {
            "name": "John",
            "age": 30
        }
        ```
        """
        with open(self.file_path, 'w') as f:
            f.write(self.markdown_content)

    def tearDown(self):
        os.remove(self.file_path)

    def test_extract_python_snippets_from_file(self):
        snippets = parse_markdown_file(self.file_path, language='python')
        self.assertEqual(len(snippets), 1)
        self.assertEqual(snippets[0].language, 'python')
        self.assertIn('def hello_world()', snippets[0].content)

    def test_extract_json_snippets_from_file(self):
        snippets = parse_markdown_file(self.file_path, language='json')
        self.assertEqual(len(snippets), 1)
        self.assertEqual(snippets[0].language, 'json')
        self.assertIn('"name": "John"', snippets[0].content)

    def test_extract_all_snippets_from_file(self):
        snippets = parse_markdown_file(self.file_path)
        self.assertEqual(len(snippets), 2)
        self.assertTrue(all(isinstance(snippet, CodeSnippet) for snippet in snippets))
