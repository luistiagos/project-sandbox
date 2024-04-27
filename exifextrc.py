from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_data(image_path):
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data:
                exif_info = {}
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    exif_info[tag_name] = value
                return exif_info
            else:
                return "No Exif data found."
    except Exception as e:
        return f"Error: {e}"

# Example usage
image_path = "mockup.jfif"
exif_info = get_exif_data(image_path)
print(exif_info)
