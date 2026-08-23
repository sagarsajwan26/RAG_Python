from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile


class StorageService:
    def __init__(self, base_dir: str = "storage/documents"):
        self.base_dir = Path(base_dir)

    async def save(
        self,
        file: UploadFile,
        tenant_id: int,
    ) -> str:
        tenant_dir = self.base_dir / str(tenant_id)
        tenant_dir.mkdir(parents=True, exist_ok=True)
        extension = Path(file.filename or "").suffix.lower()
        filename = f"{uuid4()}{extension}"
        file_path = tenant_dir / filename

        with file_path.open("wb") as buffer:
            while chunk := await file.read(1024 * 1024):
                buffer.write(chunk)

            return str(file_path)
