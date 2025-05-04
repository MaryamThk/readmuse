from pathlib import Path
from .file_loader import CodeFile
from .llm_client import AIPromptClient

class ReadmeGenerator:
    def __init__(self, paths: list[Path], output_path: Path, client: AIPromptClient):
        self.paths = paths
        self.output_path = output_path
        self.client = client

    def generate(self) -> None:
        full_code_summary = ""
        for path in self.paths:
            code = CodeFile(path).content
            full_code_summary += f"### {path.name}\n```python\n{code}\n```\n\n"

        readme_content = self.client.summarize_project("readmuse", full_code_summary)
        self.output_path.write_text(readme_content, encoding="utf-8")

