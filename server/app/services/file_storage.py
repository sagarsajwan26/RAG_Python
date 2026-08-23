from pathlib import Path
from fastapi import UploadFile


class FileStorage:
    def __init__(self, base_path: str = "uploads"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

    async def save(self, file: UploadFile, filename: str) -> str:
        file_path = self.base_path / filename

        with file_path.open("wb") as buffer:
            while chunk := await file.read(1024 * 1024):
                buffer.write(chunk)

        return str(file_path)
