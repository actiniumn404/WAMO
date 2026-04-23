import os
from PIL import Image, ImageDraw, ImageOps

def crop_to_square(image):
    width, height = image.size
    side = min(width, height)

    left = (width - side) // 2
    top = (height - side) // 2
    right = left + side
    bottom = top + side

    return image.crop((left, top, right, bottom))

def add_bg(image_path, output_path):
    image = Image.open(image_path).convert("RGBA")

    # Crop rectangular image to centered square first
    image = crop_to_square(image)

    # Resize square to desired pfp size
    image = image.resize((365, 365), Image.LANCZOS)

    width, height = image.size

    # Create circular mask
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, width, height), fill=255)

    # Apply mask to make image circular
    image.putalpha(mask)

    background = Image.open("static/Background.png").convert("RGBA")
    foreground = image

    paddingx = (background.size[0] - foreground.size[0]) // 2
    paddingy = (background.size[1] - foreground.size[1]) // 2

    foreground = ImageOps.expand(
        foreground,
        border=(paddingx, paddingy, paddingx, paddingy),
        fill=(0, 0, 0, 0)
    )

    foreground = foreground.resize(background.size, Image.LANCZOS)

    # Overlay foreground on background
    output = Image.alpha_composite(background, foreground)

    # Save as png
    output.save(output_path.split(".")[0] + ".png")


# Example usage
add_bg("static/pfps_raw/williampfp.png", "static/pfps/williampfp.png")