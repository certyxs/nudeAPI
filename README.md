# nudeAPI

Simple Python wrapper for fetching images from nekobot.xyz with caching and a built-in server.
Example

from nudeAPI import NudeAPI

api = NudeAPI()

print("Valid types:", ", ".join(sorted(api.VALID_TYPES)))
img_type = input("Enter image type: ").strip().lower()

try:
    url = api.fetch_image_cli(img_type)
    print("Image URL:", url)
except Exception as e:
    print("Error:", e)
