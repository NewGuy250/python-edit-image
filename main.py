from PIL import Image, ImageEnhance, ImageFilter
import os

# Paths for input and output directories
path = "./imgs"
pathOut = "./edited"

# Ensure output directory exists
os.makedirs(pathOut, exist_ok=True)

# Process each file in the input directory
for filename in os.listdir(path):
    if filename.lower().endswith(("png", "jpg", "jpeg", "bmp")):  # Process only image files
        img = Image.open(f"{path}/{filename}")

        # Apply the SHARPEN filter and turn into greyscale
        edit = img.filter(ImageFilter.SHARPEN).convert("L")

        # Factor to adjust the contrast
        factor = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)

        # Convert RGBA to RGB if necessary
        if edit.mode == "RGBA":
            edit = edit.convert("RGB")

        # Clean up the filename for saving
        clean_name = os.path.splitext(filename)[0]

        # Save the edited image as JPEG
        edit.save(f"{pathOut}/{clean_name}_edited.jpg", "JPEG")

print("Image processing complete!")