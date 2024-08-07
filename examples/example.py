# example.py

from pyparsec import parse_markdown_file, parse_markdown_string

file_path = 'example_file.md'
language = 'python'

python_snippets = parse_markdown_file(file_path, language=language)

print("Extracted Python Snippets from File:")
for snippet in python_snippets:
    print(f"Language: {snippet.language}\nContent:\n{snippet.content}\n")

markdown_string = """
# Sample Markdown

Here is some Python code:

```python
def hello_world():
    print("Hello, world!")
```

Here is some JavaScript code:

```javascript
function helloWorld() {
    console.log("Hello, world!");
}
```

And here is some JSON:

```json
{
    "name": "John",
    "age": 30
}
```
"""

json_snippets = parse_markdown_string(markdown_string, language='json')

print("Extracted JSON Snippets from String:")
for snippet in json_snippets:
    print(f"Language: {snippet.language}\nContent:\n{snippet.content}\n")
