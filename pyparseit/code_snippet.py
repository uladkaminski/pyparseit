# code_snippet.py

class CodeSnippet:
    def __init__(self, language: str, content: str):
        self.language = language
        self.content = content

    def __repr__(self):
        return f"<CodeSnippet language={self.language} content={len(self.content)} chars>"

    def __str__(self):
        return f"Language: {self.language}\nContent:\n{self.content}"
