from PIL import Image, ImageDraw, ImageFont
import textwrap
import streamlit as st


def create_image_with_text(text, logo_path="layer-1.png", output_path="output.png", font_path="WorkSans.ttf",
                           max_width=31,
                           input_path="downloaded_images/cv_images/cvfoto-schultz.jpg", line_spacing=30):
    # Load the logo image
    logo_image = Image.open(logo_path)

    # Create an empty image with a specific background color
    image_width, image_height = 4000, 2000
    background_image = Image.new('RGBA', (image_width, image_height), (13, 64, 128, 255))

    # Paste the input image onto the background
    input_image = Image.open(input_path)
    input_image = input_image.resize((2000, 2000))

    # Define the cropping area (left, upper, right, lower)
    crop_area = (300, 0, 1700, 2000)
    # Crop the input image
    cropped_image = input_image.crop(crop_area)

    background_image.paste(input_image, (2000, 0))
    background_image.paste(logo_image, (0, 0), logo_image)

    # Create a draw object and font object
    draw = ImageDraw.Draw(background_image)
    text_fill_color = (255, 255, 255)

    # Load the font
    if font_path:
        font = ImageFont.truetype(font_path, 100)
    else:
        font = ImageFont.load_default()

    # Wrap the text into multiple lines if it's too long
    if max_width is None:
        max_width = image_width

    try:
        wrapped_text = textwrap.fill(text, width=max_width, break_long_words=True, break_on_hyphens=True)
    except AttributeError as e:
        st.error(f"Text: {text} Error: {e}")
        raise

    # Calculate the size and position of the text
    text_bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=font, spacing=line_spacing, align='center')
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    text_x = (image_width - text_width - 2000) // 2
    text_y = (image_height // 2) - (text_height // 2)

    # Draw the text onto the image
    draw.multiline_text((text_x, text_y), wrapped_text, font=font, fill=(255, 255, 255, 255),
                        spacing=line_spacing, align='center')

    # Save the image
    background_image.save(output_path)
