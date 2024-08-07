# pyparseit/utils.py

def read_markdown_file(file_path: str) -> str:
    """
    Read the content of a Markdown file.

    Args:
        file_path (str): Path to the Markdown file.

    Returns:
        str: Content of the Markdown file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def find_code_blocks(markdown_content: str) -> list:
    """
    Find and return all code blocks from the Markdown content.

    Args:
        markdown_content (str): The content of a Markdown file or string.

    Returns:
        list: A list of code blocks found in the Markdown content.
    """
    code_blocks = []
    lines = markdown_content.split('\n')
    inside_block = False
    current_block = []

    for line in lines:
        if line.strip().startswith('```'):
            if inside_block:
                # Add the block when the closing ``` is found
                inside_block = False
                code_blocks.append('\n'.join(current_block))
                current_block = []
            else:
                inside_block = True
                current_block.append(line)
        elif inside_block:
            current_block.append(line)

    return code_blocks
