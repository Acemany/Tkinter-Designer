"""Small utility functions."""

from io import BytesIO
from pathlib import Path
from typing import Any

import requests
from PIL import Image


def woah(msg: str) -> Any:
    raise ValueError(msg)


def find_between(s: str, first: str, last: str):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)

        return s[start:end]
    except ValueError:
        return ""


def download_image(url: str, image_path: Path):
    response = requests.get(url, timeout=5000)
    content = BytesIO(response.content)
    im = Image.open(content)
    im = im.resize((im.size[0] // 2, im.size[1] // 2), Image.Resampling.LANCZOS)
    with open(image_path, "wb") as file:
        im.save(file)
