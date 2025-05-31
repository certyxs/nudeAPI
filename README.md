# nudeAPI 🚀

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-1.0.0-brightgreen)

Simple Python wrapper for fetching nude images and a built-in server.  
🔥 Fast, lightweight, and easy to use!

---

## ⚙️ Setup

Before using the API, **run `nudeAPI-SETUP.py`** to install all required dependencies.  
Put **all files in the same folder** before running your program.

---

## 🚀 Example Usage

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
