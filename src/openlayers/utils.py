import base64
from pathlib import Path

def create_icon_src_from_file(filename: str) -> bytes:
    with open(filename, "rb") as f:
        encoded_image = base64.b64encode(f.read()).decode('utf-8')

    image_type = Path(filename).suffix.replace(".", "")
    return f"data:image/{image_type};base64," + encoded_image
