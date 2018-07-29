# coding=utf-8

import sys
import numpy
import epd2in7b
import text_to_image
from PIL import Image, ImageOps, ImageFont, ImageDraw

E_PAPER_WIDTH = 264
E_PAPER_HEIGHT = 176

LEFT_COLUMN_WIDTH = 116
HEADER_HEIGHT = 42
TITLE_HEIGHT = 42
DETAIL_HEIGHT = 92
WHITE = (255, 255, 255)

MAIN = 1
AIRPORT = 2
DAISHI = 3
ZUSHI = 4
KURIHAMA = 5

IMAGE_MAIN = "./image/map_main-line.png"
IMAGE_AIRPORT = "./image/map_airport-line.png"
IMAGE_DAISHI = "./image/map_daishi-line.png"
IMAGE_ZUSHI = "./image/map_zushi-line.png"
IMAGE_KURIHAMA = "./image/map_kurihama-line.png"
IMAGE_FULL = "./image/map_full.png"
IMAGE_LEGEND = "./image/map_legend.png"


def show_image(black_image, red_image):
    epd = epd2in7b.EPD()
    epd.init()

    frame_black = epd.get_frame_buffer(black_image)
    frame_red = epd.get_frame_buffer(red_image)
    epd.display_frame(frame_black, frame_red)


if __name__ == '__main__':

    title = u"調整中"
    detail = u"データ取得中…"
    highlightLine = [MAIN, AIRPORT, DAISHI, ZUSHI, KURIHAMA]

    image_black = Image.new("RGB", (E_PAPER_WIDTH, E_PAPER_HEIGHT), WHITE)
    image_red = Image.new("RGB", (E_PAPER_WIDTH, E_PAPER_HEIGHT), WHITE)

    image_black_temp = Image.open(IMAGE_FULL)
    image_black.paste(image_black_temp, mask=image_black_temp)

    image_red_temp = Image.open(IMAGE_LEGEND)
    image_red.paste(image_black_temp, mask=image_red_temp)

    for line in highlightLine:
        if line == AIRPORT:
            image_red_temp = Image.open(IMAGE_AIRPORT)
        elif line == DAISHI:
            image_red_temp = Image.open(IMAGE_DAISHI)
        elif line == ZUSHI:
            image_red_temp = Image.open(IMAGE_ZUSHI)
        elif line == KURIHAMA:
            image_red_temp = Image.open(IMAGE_KURIHAMA)
        else:
            image_red_temp = Image.open(IMAGE_MAIN)

        image_red.paste(image_black_temp, mask=image_red_temp)

    image_red.paste(ImageOps.invert(text_to_image.text_to_image(
        LEFT_COLUMN_WIDTH, HEADER_HEIGHT, u"京急線", 24)), (0, 0))

    image_black.paste(text_to_image.text_to_image(
        LEFT_COLUMN_WIDTH, TITLE_HEIGHT, title, 16), (0, HEADER_HEIGHT))

    image_black.paste(text_to_image.text_to_image(
        LEFT_COLUMN_WIDTH, DETAIL_HEIGHT, detail, 14), (0, HEADER_HEIGHT + TITLE_HEIGHT))

    show_image(image_black.rotate(90, expand=True),
               image_red.rotate(90, expand=True))
