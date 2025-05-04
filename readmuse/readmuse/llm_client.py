import requests

class AIPromptClient:
    def __init__(self, api_url: str, api_key: str):
        self.api_url = api_url
        self.api_key = api_key

    def summarize_project(self, project_name: str, all_code: str) -> str:
        prompt = (
            f"You are an expert technical writer and software engineer.\n"
            f"Write a high-quality `README.md` file for a Python project named `{project_name}`.\n\n"
            f"## Include the following sections:\n"
            f"1. **Project Purpose** – What problem does this project solve?\n"
            f"2. **Installation & Usage** – How should users install and use it?\n"
            f"3. **Core Modules & Logic** – Describe the key components (files, classes, functions).\n"
            f"4. **Design Overview** – Optional, only if there's architectural design worth noting.\n"
            f"5. **Limitations or TODOs** – Optional, if you detect any incomplete or rough areas.\n\n"
            f"Below is the codebase to analyze:\n\n"
            f"{all_code}"
        )

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a technical writer creating project-level documentation."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }

        resp = requests.post(self.api_url, json=payload, headers=headers)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()
