"""Utility classes and functions for Figma API endpoints."""

from typing import Any
import requests


class Files:
    """https://www.figma.com/developers/api#files-endpoints"""

    API_ENDPOINT_URL = "https://api.figma.com/v1"

    def __init__(self, token: str, file_key: str):
        self.token = token
        self.file_key = file_key

    def __str__(self):
        return f"Files {{ Token: {self.token}, File: {self.file_key} }}"

    def get_file(self) -> dict[str, Any]:
        try:
            response = requests.get(
                f"{self.API_ENDPOINT_URL}/files/{self.file_key}",
                headers={"X-FIGMA-TOKEN": self.token},
                timeout=5000)
        except ValueError as e:
            raise RuntimeError(
                "Invalid Input. Please check your input and try again.") from e
        except requests.ConnectionError as e:
            raise RuntimeError(
                "Tkinter Designer requires internet access to work.") from e

        return response.json()

    def get_image(self, item_id: str) -> str:
        response = requests.get(
            f"{self.API_ENDPOINT_URL}/images/{self.file_key}?ids={item_id}&scale=2",
            headers={"X-FIGMA-TOKEN": self.token},
            timeout=5000
        )

        return response.json()["images"][item_id]
