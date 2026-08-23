from pathlib import Path
from pypdf import PdfReader


class DocumentParser:
    def extract_text(self, file_path: str) -> str:
        path = Path(file_path)

        if path.suffix.lower() == ".txt":
            return path.read_text(encoding="utf-8")
        if path.suffix.lower() == ".pdf":
            return self._extract_pdf(path)
        raise ValueError(f"unsupported file type: {path.suffix} ")

    def _extract_pdf(self, path: Path) -> str:
        reader = PdfReader(path)
        pages = []
        for page in reader.pages:
            text = page.extract_text()

            if text:
                pages.append(text)

        return "\n".join(pages)
