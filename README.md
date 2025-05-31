# nudeAPI

Simple Python wrapper for fetching images from nekobot.xyz with caching and a built-in server.

---

## Setup

Before using the API, **run `nudeAPI-SETUP.py`** to install all required dependencies.

Put **all files in the same folder** before running your program.

---

## Example

```python
from nudeAPI import NudeAPI

api = NudeAPI()

print("Valid types:", ", ".join(sorted(api.VALID_TYPES)))
img_type = input("Enter image type: ").strip().lower()

try:
    url = api.fetch_image_cli(img_type)
    print("Image URL:", url)
except Exception as e:
    print("Error:", e)
