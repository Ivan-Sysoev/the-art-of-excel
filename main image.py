from PIL import Image
import openpyxl
from openpyxl.styles import PatternFill

class Painter:
    def __init__(cls, img):
        cls.img = img
    
    def get_image_data(cls):
        """Изображение ==> массив RGB значений пикселей"""
        im = Image.open(cls.img)
        rgb_code = im.convert("RGB")
        cls.width, cls.height = im.size
        return [[rgb_code.getpixel((n,i)) for n in range(cls.width)] for i in range(cls.height)]
    
    def color_pixel(cls):
        wb = openpyxl.Workbook()
        ws = wb.active

        for row_num, pixel_row in enumerate(cls.get_image_data()):
            for column_num, pixel_rgb in enumerate(pixel_row):
                color = "%02x%02x%02x" % pixel_rgb
                colorFill = PatternFill(start_color=color, end_color=color, fill_type="solid")
                ws.cell(row=row_num+1, column=column_num+1).fill = colorFill

        wb.save(filename="result.xlsx")
    
Painter("IMG_0003 (1).jpg").color_pixel()