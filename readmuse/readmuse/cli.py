import argparse
from pathlib import Path
from .generator import ReadmeGenerator
from .llm_client import AIPromptClient
from .config import get_config

def run():
    parser = argparse.ArgumentParser(description="Generate README using LLM")
    parser.add_argument("--dir", default=".", help="Directory with .py files")
    parser.add_argument("--output", default="README.md", help="Output README path")
    args = parser.parse_args()

    config = get_config()
    paths = [p for p in Path(args.dir).glob("*.py") if p.name != "main.py"]
    client = AIPromptClient(config["API_URL"], config["API_KEY"])
    generator = ReadmeGenerator(paths, Path(args.output), client)
    generator.generate()
