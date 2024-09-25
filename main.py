from nlp_processor import parse_user_description
from wallpaper_generator import generate_random_vibgyor_wallpaper

def main():
    print("Welcome to Luminous - AI-based Wallpaper Generator!")

    # Get user input
    description = input("Describe the type of wallpaper you want: ")

    # Parse the description
    keywords = parse_user_description(description)
    print(f"Extracted Keywords: {keywords}")

    # Generate the wallpaper
    wallpaper = generate_random_vibgyor_wallpaper()

    # Save the wallpaper
    wallpaper.save('generated_wallpaper.png')
    print("Wallpaper generated successfully and saved as 'generated_wallpaper.png'.")

if __name__ == '__main__':
    main()
