from pathlib import Path

from tkdesigner.figma import endpoints
from tkdesigner.figma.frame import Frame

from tkdesigner.template import TEMPLATE


class Designer:
    def __init__(self, token: str, file_key: str, output_path: Path):
        self.output_path = output_path
        self.figma_file = endpoints.Files(token, file_key)
        self.file_data = self.figma_file.get_file()
        self.frameCounter = 0

    def to_code(self) -> list[str]:
        """Return main code."""

        frames = list[str]()
        for f in self.file_data["document"]["children"][0]["children"]:
            try:
                frame = Frame(f, self.figma_file, self.output_path, self.frameCounter)
            except Exception as e:
                raise FileNotFoundError("Frame not found in figma file or is empty") from e
            frames.append(frame.to_code(TEMPLATE))
            self.frameCounter += 1
        return frames

    def design(self):
        """Write code and assets to the specified directories."""
        code = self.to_code()
        for i, e in enumerate(code):
            # tutorials on youtube mention `python3 gui.py` added the below check to keep them valid
            if i == 0:
                self.output_path.joinpath("gui.py").write_text(e, encoding='UTF-8')
            else:
                self.output_path.joinpath(f"gui{i}.py").write_text(e, encoding='UTF-8')
