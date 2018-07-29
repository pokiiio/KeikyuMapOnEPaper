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

ALL_LINES = u"全線"
MAIN_LINE_STATIONS = [u"泉岳寺", u"品川", u"北品川", u"新馬場", u"青物横丁", u"鮫洲", u"立会川", u"大森海岸", u"平和島", u"大森町", u"梅屋敷", u"京急蒲田",  u"雑色", u"六郷土手", u"京急川崎",  u"八丁畷", u"鶴見市場", u"京急鶴見", u"花月園前", u"生麦", u"京急新子安", u"子安",
                      u"神奈川新町", u"仲木戸", u"神奈川", u"横浜", u"戸部", u"日ノ出町", u"黄金町", u"南太田", u"井土ヶ谷", u"弘明寺", u"上大岡", u"屏風浦", u"杉田", u"京急富岡", u"能見台", u"金沢文庫", u"金沢八景",  u"追浜", u"京急田浦", u"安針塚", u"逸見", u"汐入", u"横須賀中央", u"県立大学", u"堀ノ内", u"京急大津", u"馬堀海岸", u"浦賀"]
AIRPORT_LINE_STATIONS = [u"空港線", u"糀谷", u"大鳥居", u"穴守稲荷",
                         u"天空橋", u"羽田空港", u"羽田空港国内線ターミナル", u"羽田空港国際線ターミナル"]
DAISHI_LINE_STATIONS = [u"大師線", u"港町",
                        u"鈴木町", u"川崎大師", u"東門前", u"産業道路", u"小島新田"]
ZUSHI_LINE_STATIONS = [u"逗子線", u"六浦", u"神武寺", u"新逗子"]
KURIHAMA_LINE_STATIONS = [u"久里浜線", u"新大津", u"北久里浜", u"京急久里浜",
                          u"YRP野比", u"京急長沢", u"津久井浜", u"三浦海岸", u"三崎口"]

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


def get_title(text):
    if text.find(u"平常") > -1:
        return u"平常運転"

    if text.find(u"見合わせ"):
        return u"運転見合わせ"

    if text.find(u"遅れ") or text.find(u"乱れ"):
        return u"遅延"

    if text.find(u"運休"):
        return u"運休"

    return u"運行情報あり"


def get_highlited_lines(text):
    if text.find(ALL_LINES) > -1:
        return [MAIN, AIRPORT, DAISHI, ZUSHI, KURIHAMA]

    highlited_lines = []

    for station in MAIN_LINE_STATIONS:
        if text.find(station) > -1:
            highlited_lines.append(MAIN)
            break

    for station in AIRPORT_LINE_STATIONS:
        if text.find(station) > -1:
            highlited_lines.append(AIRPORT)
            break
    for station in DAISHI_LINE_STATIONS:
        if text.find(station) > -1:
            highlited_lines.append(DAISHI)
            break

    for station in ZUSHI_LINE_STATIONS:
        if text.find(station) > -1:
            highlited_lines.append(ZUSHI)
            break

    for station in KURIHAMA_LINE_STATIONS:
        if text.find(station) > -1:
            highlited_lines.append(KURIHAMA)
            break

    return highlited_lines


if __name__ == '__main__':

    title = u"調整中"
    detail = u"データ取得中…"

    if len(sys.argv) == 2:
        detail = unicode(sys.argv[1], 'utf-8')
        title = get_title(detail)

    highlightLine = get_highlited_lines(detail)

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
