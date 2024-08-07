# pyparseit/cli.py

import argparse
import sys

from .exceptions import PyParsecError
from .parser import parse_markdown_file, parse_markdown_string


def main():
    args = parse_arguments()
    try:
        if args.string:
            snippets = parse_markdown_string(args.input, args.language)
        else:
            snippets = parse_markdown_file(args.input, args.language)
        output_snippets(snippets, args.output)
    except PyParsecError as e:
        handle_error(e)


def parse_arguments():
    parser = argparse.ArgumentParser(description="Parse Markdown and extract code snippets.")

    parser.add_argument(
        'input',
        type=str,
        help='The input Markdown content or file path.'
    )

    parser.add_argument(
        '-s', '--string',
        action='store_true',
        help='Indicate that the input is a Markdown string.'
    )

    parser.add_argument(
        '-l', '--language',
        type=str,
        help='The programming language of code snippets to extract (e.g., python, json, javascript).'
    )

    parser.add_argument(
        '-o', '--output',
        type=str,
        help='Path to the output file to save extracted code snippets.'
    )

    return parser.parse_args()


def output_snippets(snippets, output_path):
    if output_path:
        save_to_file(snippets, output_path)
    else:
        display_snippets(snippets)


def display_snippets(snippets):
    for i, snippet in enumerate(snippets, start=1):
        print(f"\n--- Code Snippet {i} ({snippet.language}) ---\n")
        print(snippet.content)


def save_to_file(snippets, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        for i, snippet in enumerate(snippets, start=1):
            file.write(f"\n--- Code Snippet {i} ({snippet.language}) ---\n")
            file.write(snippet.content + "\n")
    print(f"Extracted code snippets saved to {output_path}")


def handle_error(e):
    sys.stderr.write(f"Error: {e}\n")
    sys.exit(1)


if __name__ == '__main__':
    main()
