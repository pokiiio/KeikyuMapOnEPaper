# coding=utf-8

import numpy
import epd2in7b
import text_to_image
from PIL import Image, ImageOps, ImageFont, ImageDraw

E_PAPER_WIDTH = 264
E_PAPER_HEIGHT = 176

LEFT_COLUMN_WIDTH = 116
HEADER_HEIGHT = 42
TITLE_HEIGHT = 42


def show_image(black_image, red_image):
    epd = epd2in7b.EPD()
    epd.init()

    frame_black = epd.get_frame_buffer(black_image)
    frame_red = epd.get_frame_buffer(red_image)
    epd.display_frame(frame_black, frame_red)


if __name__ == '__main__':

    image_black = Image.new(
        "RGB", (E_PAPER_WIDTH, E_PAPER_HEIGHT), (255, 255, 255))

    image_red = Image.new(
        "RGB", (E_PAPER_WIDTH, E_PAPER_HEIGHT), (255, 255, 255))

    image_black_temp = Image.open("./image/map_full.png")
    image_black.paste(image_black_temp, mask=image_black_temp)

    image_red_temp = Image.open("./image/map_main-line.png")
    image_red.paste(image_black_temp, mask=image_red_temp)

    image_red.paste(ImageOps.invert(text_to_image.text_to_image(
        LEFT_COLUMN_WIDTH, HEADER_HEIGHT, u"京急線", 24)), (0, 0))

    image_red.paste(text_to_image.text_to_image(
        LEFT_COLUMN_WIDTH, TITLE_HEIGHT, u"運転見合わせ", 16), (0, HEADER_HEIGHT))

    show_image(image_black.rotate(90, expand=True),
               image_red.rotate(90, expand=True))
