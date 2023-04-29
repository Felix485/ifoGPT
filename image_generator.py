from PIL import Image, ImageDraw, ImageFont
import textwrap


def create_image_with_text(logo_path, text, output_path, font_path=None, max_width=None, input_path=None, line_spacing=5):
    # Load the logo image
    logo = Image.open(logo_path)

    # Create an empty image with white background
    img_w, img_h = 1000, 1000
    background = Image.new('RGBA', (img_w, img_h), (255, 255, 255, 255))

    # Paste the logo onto the background
    background.paste(logo, (20, 870))
    im = Image.open(input_path)
    background.paste(im, (20, 20))

    # Create a draw object and font object
    draw = ImageDraw.Draw(background)
    if font_path:
        font = ImageFont.truetype(font_path, 60)
    else:
        font = ImageFont.load_default()

    # Wrap the text into multiple lines if it's too long
    if max_width is None:
        max_width = img_w
    wrapped_text = textwrap.fill(text, width=max_width, break_long_words=True, break_on_hyphens=True)

    # Calculate the size and position of the text
    text_bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=font, spacing=line_spacing, align='center')
    text_w, text_h = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    text_x = (img_w - text_w) // 2
    text_y = img_h - (text_h // 2) - 200

    # Draw the text onto the image
    draw.multiline_text((text_x, text_y), wrapped_text, font=font, fill=(0, 0, 0, 255), spacing=line_spacing, align='center')

    # Save the image
    background.save(output_path)


# Example usage:
input_path = "downloaded_images/graphic_images/20230428-ifo-pm-bip-lang-0423-de.png"
logo_path = "ifo_logo.png"
text = "Dies ist KEIN sehr langer Text über Wirtschaftsnachrichten. Er ist bestimmt sehr wichtig."
output_path = "output.png"
font_path = "WorkSans.ttf"  # Path to your desired font (optional)
max_width = 25  # Maximum number of characters per line (optional)
create_image_with_text(logo_path, text, output_path, font_path, max_width, input_path)

