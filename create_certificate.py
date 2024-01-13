# pip install pillow 

from PIL import Image, ImageDraw, ImageFont

def create_certificate(names, id, certificate:str, output_folder:str):

    print('Creating your certificates...')

    for name, dni in zip(names, id):
        text_y_position = 675
        img = Image.open(certificate, mode='r')
        img_width = img.width
        image_height = img.height

        # draw
        draw = ImageDraw.Draw(img)

        # font
        font_size = 150

        if len(name) > 30:
            font_size = font_size / 2
        elif len(name) > 20:
            font_size = font_size * 2/3

        # IMPORTANT
        # Set your own Font! If you get errors you can use the available fonts on your computer
        font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', int(font_size))
        font2 = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', size=55)

        # text width
        text_width, _ = draw.textsize(name, font=font)

        # draw test for name
        draw.text(((img_width - text_width) / 2, text_y_position), name, font=font, fill='black')

        #draw test for ID
        draw.text((2400, 1280), f'ID: {str(dni)}', font=font2, fill='black')

        # save certificates in a folder
        output_path = f"{output_folder}/{name}.pdf"
        img.save(output_path)
        print(f"Saved certificate for {name} at {output_path}")