from PIL import Image, ImageDraw, ImageFont
import textwrap


def create_image_with_text(text, logo_path="layer-1.png",  output_path="output.png", font_path="WorkSans.ttf", max_width=25, input_path="downloaded_images/cv_images/cvfoto-schultz.jpg", line_spacing=30):
    # Load the logo image
    logo = Image.open(logo_path)

    # Create an empty image with white background
    img_w, img_h = 4000, 2000
    background = Image.new('RGBA', (img_w, img_h), (13,64,128, 255))

    # Paste the logo onto the background
    im = Image.open(input_path)
    im = im.resize((2000,2000))
    # Define the cropping area (left, upper, right, lower)
    crop_area = (300, 0, 1700, 2000)
    # Crop the image
    cropped_image = im.crop(crop_area)
    #background.paste(logo, (0, 0))

    background.paste(im, (2000,0))
    background.paste(logo, (0, 0), logo)



    # Create a draw object and font object
    draw = ImageDraw.Draw(background)
    fill_color = (255, 255, 255)


    if font_path:
        font = ImageFont.truetype(font_path, 120)
    else:
        font = ImageFont.load_default()

    # Wrap the text into multiple lines if it's too long
    if max_width is None:
        max_width = img_w
    wrapped_text = textwrap.fill(text, width=max_width, break_long_words=True, break_on_hyphens=True)

    # Calculate the size and position of the text
    text_bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=font, spacing=line_spacing, align='center')
    text_w, text_h = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    text_x = (img_w - text_w - 2000) // 2
    text_y = (img_h//2) - (text_h // 2) 

    # Draw the text onto the image
    draw.multiline_text((text_x, text_y), wrapped_text, font=font, fill=(255, 255, 255, 255), spacing=line_spacing, align='center')

    # Save the image
    background.save(output_path)


# Example usage:
#input_path = "downloaded_images\cv_images\cvfoto-schultz.jpg"
#logo_path = "ifo_logo.png"
#text = "Dies ist KEIN sehr langer Text über Wirtschaftsnachrichten. Er ist bestimmt sehr wichtig."
#output_path = "downloaded_images/output_image/output.png"
#font_path = "WorkSans.ttf"  # Path to your desired font (optional)
#max_width = 35  # Maximum number of characters per line (optional)
#create_image_with_text(logo_path, text, output_path, font_path, max_width, input_path)

