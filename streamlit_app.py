import streamlit as st
from wallpaper_generator import generate_random_vibgyor_wallpaper
from nlp_processor import parse_user_description

def main():
    st.title("Luminous - AI-based Wallpaper Generator")

    # Take user input
    description = st.text_input("Describe your wallpaper: ")

    if st.button("Generate"):
        # Parse the description and display extracted keywords
        keywords = parse_user_description(description)
        st.write(f"Extracted Keywords: {keywords}")

        # Generate wallpaper
        wallpaper = generate_random_vibgyor_wallpaper()

        # Save the image to display it
        wallpaper.save('generated_wallpaper.png')

        # Display the wallpaper in Streamlit
        st.image('generated_wallpaper.png', caption='Generated Wallpaper')

if __name__ == '__main__':
    main()
