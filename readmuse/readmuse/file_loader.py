from pathlib import Path

class CodeFile:
    def __init__(self, path: Path):
        self.path = path
        self.content = self._read()

    def _read(self) -> str:
        with self.path.open("r", encoding="utf-8") as f:
            return f.read()
