# pyparseit/parser.py

from typing import List, Optional

from .code_snippet import CodeSnippet
from .utils import read_markdown_file, find_code_blocks


def parse_markdown_file(file_path: str, language: Optional[str] = None) -> List[CodeSnippet]:
    """
    Parse a Markdown file and extract code snippets of a specific language.

    Args:
        file_path (str): The path to the Markdown file.
        language (Optional[str]): The programming language to filter snippets by.

    Returns:
        List[CodeSnippet]: A list of extracted code snippets.
    """
    markdown_content = read_markdown_file(file_path)
    return _parse(markdown_content, language)


def parse_markdown_string(markdown_string: str, language: Optional[str] = None) -> List[CodeSnippet]:
    """
    Parse a Markdown string and extract code snippets of a specific language.

    Args:
        markdown_string (str): The Markdown content as a string.
        language (Optional[str]): The programming language to filter snippets by.

    Returns:
        List[CodeSnippet]: A list of extracted code snippets.
    """
    return _parse(markdown_string, language)


def _parse(content: str, language: Optional[str] = None) -> List[CodeSnippet]:
    """
    Internal method to parse the Markdown content.

    Args:
        content (str): The Markdown content.
        language (Optional[str]): The programming language to filter snippets by.

    Returns:
        List[CodeSnippet]: A list of extracted code snippets.
    """
    code_blocks = find_code_blocks(content)
    snippets = []

    for block in code_blocks:
        lang, code_content = _identify_code_block(block)
        if (language is None) or (lang.lower() == language.lower()):
            snippets.append(CodeSnippet(lang, code_content))

    return snippets


def _identify_code_block(block: str) -> tuple:
    """
    Identify the language and content of a code block.

    Args:
        block (str): A string representing a code block in Markdown.

    Returns:
        tuple: A tuple containing the language and content of the code block.
    """
    lines = block.splitlines()
    if lines:
        # Extract the language from the opening line of the code block
        language_line = lines[0]
        if language_line.strip().startswith('```'):
            language = language_line.strip()[3:].strip()  # Get the text after ```
            content = "\n".join(lines[1:])  # Everything after the first line is code
        else:
            language, content = "", "\n".join(lines)
    else:
        language, content = "", ""
    return language, content
