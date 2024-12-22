from pathlib import Path

import requests


def download_to_local(url: str, path: Path, mkdir: bool = True):
    if not isinstance(path, Path):
        raise ValueError(f"{path} must be a valid pathlib.Path object")
    if mkdir:
        path.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url)
        response.raise_for_status()
        # Write the file out in binary mode to prevent any newline conversions
        path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return False
