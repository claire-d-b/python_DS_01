from PIL import Image
import numpy as np

# Grayscale ('L' Mode):
# Channels: 1 (Intensity)
# Description: Each pixel value represents the intensity of the grayscale color, ranging from black (0) to white (255). There is no alpha channel in this mode.
# To create a grayscale image from a 3D list using Pillow, you need to ensure that the 3D list represents an image where the third dimension contains only one value (the grayscale intensity). The 3D list should be structured as [height][width][1], where each sub-list represents a row of pixels, and each pixel has a single grayscale intensity value.

def slice_me_3d(family: list, start_x: int, end_x: int, start_y: int, end_y: int) -> list:
    ret = []
    if isinstance(family, list):
        ret = family[start_x:end_x]
        for x, row in enumerate(ret):
            ret[x] = row[start_y:end_y]
    else:
        raise AssertionError("Error: parameter is not a list")
    return ret

def create_image(barray: list) -> Image:
    # Get the dimensions of the image
    height = len(barray)
    width = len(barray[0])

    # Create a new Pillow image with RGB mode
    image = Image.new('RGB', (width, height))

    # Populate the image with pixel values
    pixels = image.load()
    for y, row in enumerate(barray):
        for x, color in enumerate(row):
            pixels[x, y] = tuple(color)

    # Save the image as a JPEG file
    return image

def ft_load(path: str) -> bytearray:
    try:
        Image.open(path)
        image = Image.open(path)
        barray = []

        width, height = image.size

        for x in range(0, height):
            barray.insert(x, [])
            for y in range(0, width):
                r, g, b = image.getpixel((y, x))
                barray[x].insert(y, [r, g, b])

        string = "The shape of image is: "
        items = image.getpixel((0, 0))
        i = 0
        for item in items:
            i += 1
        print(string, (height, width, i))

    except AssertionError as e:
        raise AssertionError("Error: failed to open file")
    return barray
