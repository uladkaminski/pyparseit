# PyParseit

**PyParseit** is a Python library designed to parse Markdown files and strings to extract code snippets based on specific programming languages. It provides a simple and intuitive interface for developers who want to quickly extract and utilize code blocks from Markdown documents or strings.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Parsing from a File](#parsing-from-a-file)
  - [Parsing from a String](#parsing-from-a-string)
  - [Checking for Snippets in a File](#checking-for-snippets-in-a-file)
  - [Checking for Snippets in a String](#checking-for-snippets-in-a-string)
- [Command-Line Interface](#command-line-interface)
- [Examples](#examples)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Markdown is widely used for documentation, blogging, and technical writing. PyParseit simplifies the task of extracting code snippets from Markdown files and strings, making it ideal for static site generators, content management systems, and more.

## Features

- Parse Markdown files or strings to extract code blocks.
- Filter code snippets by programming language (e.g., Python, JavaScript, JSON).
- Check for the existence of code snippets of a specific language in files or strings.
- Command-line interface for easy integration into scripts and workflows.
- Customizable and extensible API for developers.

## Installation

You can install PyParseit via pip:

```bash
pip install pyparseit
```

Alternatively, you can clone the repository and install it manually:

```bash
git clone https://github.com/uladkaminski/pyparseit.git
cd pyparseit
python setup.py install
```

## Usage

### Parsing from a File

Here's a basic example of how to use PyParseit to extract Python code snippets from a Markdown file:

```python
from pyparseit import parse_markdown_file
```

Specify the file path and language

```python
file_path = 'example_file.md'
language = 'python'
```

Parse the Markdown file to extract Python code snippets
```python
python_snippets = parse_markdown_file(file_path, language=language)
```

Display extracted Python snippets from the file
```python
for snippet in python_snippets:
  print(f"Language: {snippet.language}\nContent:\n{snippet.content}\n")
```

### Parsing from a String

PyParseit can also parse Markdown content directly from a string:

```python
from pyparseit import parse_markdown_string

# Define a Markdown string with multiple code blocks
markdown_string = """
# Sample Markdown

Here is some Python code:

\`\`\`python
def hello_world():
    print("Hello, world!")
\`\`\`

Here is some JavaScript code:

\`\`\`javascript
function helloWorld() {
    console.log("Hello, world!");
}
\`\`\`

And here is some JSON:

\`\`\`json
{
    "name": "John",
    "age": 30
}
\`\`\`
"""

# Parse the Markdown string to extract JSON code snippets
json_snippets = parse_markdown_string(markdown_string, language='json')

# Display extracted JSON snippets from the string
print("Extracted JSON Snippets from String:")
for snippet in json_snippets:
  print(f"Language: {snippet.language}\nContent:\n{snippet.content}\n")
```

### Checking for Snippets in a File

You can also check if a Markdown file contains code snippets of a specific language:

```python
from pyparseit import contains_snippet_file

# Specify the file path and language
file_path = 'example_file.md'
language = 'python'

# Check if the Markdown file contains Python code snippets
has_python_snippet = contains_snippet_file(file_path, language=language)

print(f"File contains Python snippets: {has_python_snippet}")
```

### Checking for Snippets in a String

Similarly, you can check if a Markdown string contains code snippets of a specific language:

```python
from pyparseit import contains_snippet_string

# Define a Markdown string with multiple code blocks
markdown_string = """
# Sample Markdown

Here is some Python code:

\`\`\`python
def hello_world():
    print("Hello, world!")
\`\`\`

Here is some JavaScript code:

\`\`\`javascript
function helloWorld() {
    console.log("Hello, world!");
}
\`\`\`

And here is some JSON:

\`\`\`json
{
    "name": "John",
    "age": 30
}
\`\`\`
"""

# Check if the Markdown string contains Python code snippets
has_python_snippet = contains_snippet_string(markdown_string, language='python')

print(f"String contains Python snippets: {has_python_snippet}")
```

## Command-Line Interface

PyParseit also provides a CLI for easy usage from the terminal:

```bash
pyparseit path/to/your/file.md -l python -o output.txt
```

This command parses the specified Markdown file, extracts Python code snippets, and saves them to `output.txt`.

## Examples

Check out the [examples](examples/) directory for more use cases and demonstrations of how to integrate PyParseit into your projects.

## API Reference

### `parse_markdown_file`

- **Description**: Parses Markdown content from a file to extract code snippets.
- **Parameters**:
  - `file_path (str)`: The path to the Markdown file.
  - `language (Optional[str])`: The programming language to filter snippets by.
- **Returns**: `List[CodeSnippet]`: A list of extracted code snippets.

### `parse_markdown_string`

- **Description**: Parses Markdown content from a string to extract code snippets.
- **Parameters**:
  - `markdown_string (str)`: The Markdown content as a string.
  - `language (Optional[str])`: The programming language to filter snippets by.
- **Returns**: `List[CodeSnippet]`: A list of extracted code snippets.

### `contains_snippet_file`

- **Description**: Checks if a Markdown file contains at least one code snippet of a specific language.
- **Parameters**:
  - `file_path (str)`: The path to the Markdown file.
  - `language (Optional[str])`: The programming language to filter snippets by.
- **Returns**: `bool`: `True` if the file contains at least one snippet of the specified language, `False` otherwise.

### `contains_snippet_string`

- **Description**: Checks if a Markdown string contains at least one code snippet of a specific language.
- **Parameters**:
  - `markdown_string (str)`: The Markdown content as a string.
  - `language (Optional[str])`: The programming language to filter snippets by.
- **Returns**: `bool`: `True` if the string contains at least one snippet of the specified language, `False` otherwise.

### `CodeSnippet`

- **Description**: Represents a code snippet with language and content.
- **Attributes**:
  - `language: str`: The programming language of the code snippet.
  - `content: str`: The code snippet's content.

### Exceptions

- **`PyParsecError`**: Base exception for parser errors.

## Contributing

Contributions are welcome! If you'd like to contribute to PyParseit, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Implement your changes and add tests if applicable.
4. Commit your changes and push to your fork.
5. Submit a pull request with a description of your changes.

Please ensure your code adheres to the project's coding standards and passes all tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
