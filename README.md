# readmuse(This README.md is also the output of this project)

## Project Purpose
The `readmuse` project aims to automate the generation of high-quality README.md files for Python projects. By leveraging the power of AI language models, specifically the OpenAI GPT-3.5 Turbo model, this tool assists technical writers and software engineers in quickly creating project-level documentation.

## Installation & Usage
To install and use `readmuse`, follow these steps:
1. Clone the repository: `git clone https://github.com/your/repo.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up your environment variables by creating a `.env` file with the following keys:
   - `API_URL` (default: `https://openrouter.ai/api/v1/chat/completions`)
   - `API_KEY` (Your openrouter API key. It can be a free API key.)
4. Run the CLI by executing: `python cli.py --dir /path/to/your/python/files --output /path/to/output/README.md`

## Core Modules & Logic
### `llm_client.py`
- `AIPromptClient`: A class that interacts with the OpenAI API to generate project summaries based on provided code snippets.

### `file_loader.py`
- `CodeFile`: A class for loading and reading the content of Python code files.

### `config.py`
- `get_config()`: A function to retrieve configuration settings, including the API URL and API key from environment variables.
- `raise_key_error()`: An error-raising function for missing API keys.

### `cli.py`
- `run()`: A function to handle command-line arguments, directory parsing, and README generation using the `ReadmeGenerator`.

### `generator.py`
- `ReadmeGenerator`: A class responsible for generating README files by summarizing the content of Python code files using the `AIPromptClient`.

## Design Overview
The project follows a modular design, separating concerns into different components for improved readability and maintainability. The `llm_client.py` module handles API interactions, the `file_loader.py` module deals with file operations, and the `generator.py` module orchestrates the README generation process. The CLI (`cli.py`) provides a user-friendly interface to generate README files effortlessly.

## Limitations or TODOs
- Enhance error handling and logging mechanisms for better debugging.
- Implement unit tests to ensure code reliability and accuracy.
- Provide additional customization options for README generation, such as template selection.
- Optimize API calls and response handling for improved performance.

Feel free to contribute to the project or provide feedback for further enhancements!