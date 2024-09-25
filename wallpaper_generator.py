from PIL import Image
import random

# VIBGYOR color palette in RGB format
VIBGYOR_COLORS = {
    'Violet': (148, 0, 211),
    'Indigo': (75, 0, 130),
    'Blue': (0, 0, 255),
    'Green': (0, 255, 0),
    'Yellow': (255, 255, 0),
    'Orange': (255, 165, 0),
    'Red': (255, 0, 0)
}

def generate_random_vibgyor_wallpaper(width=1920, height=1080):
    """Generates a wallpaper with random VIBGYOR colors."""
    image = Image.new('RGB', (width, height))
    pixels = image.load()

    # Fill image with random colors from VIBGYOR
    for i in range(width):
        for j in range(height):
            color = random.choice(list(VIBGYOR_COLORS.values()))
            pixels[i, j] = color

    return image

# Example usage:
# wallpaper = generate_random_vibgyor_wallpaper()
# wallpaper.show()
# wallpaper.save('vibgyor_wallpaper.png')
