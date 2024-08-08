# tests/test_parser.py

import unittest

from pyparseit import parse_markdown_string, CodeSnippet
from pyparseit.parser import contains_snippet_string


class TestParseMarkdownString(unittest.TestCase):
    def setUp(self):
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

        Here is some JavaScript:

        ```javascript
        function greet() {
            console.log("Hello, world!");
        }
        ```
        """

    def test_extract_python_snippets(self):
        snippets = parse_markdown_string(self.markdown_content, language='python')
        self.assertEqual(len(snippets), 1)
        self.assertEqual(snippets[0].language, 'python')
        self.assertIn('def hello_world()', snippets[0].content)

    def test_extract_json_snippets(self):
        snippets = parse_markdown_string(self.markdown_content, language='json')
        self.assertEqual(len(snippets), 1)
        self.assertEqual(snippets[0].language, 'json')
        self.assertIn('"name": "John"', snippets[0].content)

    def test_extract_all_snippets(self):
        snippets = parse_markdown_string(self.markdown_content)
        self.assertEqual(len(snippets), 3)
        self.assertTrue(all(isinstance(snippet, CodeSnippet) for snippet in snippets))

    def test_extract_no_snippets(self):
        snippets = parse_markdown_string(self.markdown_content, language='ruby')
        self.assertEqual(len(snippets), 0)

    def test_contains_python_snippets(self):
        self.assertTrue(contains_snippet_string(self.markdown_content, language='python'))

    def test_contains_no_snippets(self):
        self.assertFalse(contains_snippet_string(self.markdown_content, language='ruby'))
