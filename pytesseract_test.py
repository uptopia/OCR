#!/usr/bin/python
# -*- coding: UTF-8 -*-
#================================#
#           光學字元辨識
#  Optical Character Recognition 
#        pytesseract測試 
#================================#
# https://ithelp.ithome.com.tw/articles/10227263
# written by Shang-Wen, Wong
# 2021.3.20

#***************#
# 使用限制＆TODO
#***************#
#遇到圖中有中文字會報錯
#不確定非平面或realsense效果如何
#不確定其他角度是否可以辨識
#不公整的英文字也看不出來pcl

import numpy as np
from PIL import Image, ImageDraw, ImageFont

# import pyocr
# import pyocr.builders
import pytesseract
import cv2

#================#
#     輸入圖片
#================#
load_img_path = 'img/alphabet_ocr.png'#logoall, test_letter, screenshot, GL, clean_alphabet, alphabet_ocr
img = cv2.imread(load_img_path, cv2.IMREAD_COLOR)

# img_ori = Image.open(load_img_path)
# img = img_ori
img_h , img_w, _ = np.array(img).shape

# # CONVERT TO uint8
# img = img_ori.convert('L')
# img_h , img_w = np.array(img).shape

print("Load Image: {0}; (height, width) = {1}, {2}".format(load_img_path, img_h, img_w))

#=====================#
#  測試pytesseract功能
#=====================#
### https://github.com/madmaze/pytesseract
decode1 = pytesseract.image_to_string(img) #lang = "eng+chi_tra"
decode2 = pytesseract.image_to_boxes(img)
decode3 = pytesseract.image_to_data(img)

print('decode1\n', decode1)
print('decode2\n', decode2)
print('decode3\n', decode3)

#==================#
# 標示文字及文字位置
#==================#
### 使用pytesseract.image_to_boxes資訊
### (letter, x1, y1, x2, y2, ?)
info_array = decode2.split(None) #separate by "blank"

idx = int(np.size(info_array)/6)

for i in range(idx):
    cnt = i*6

    letter = info_array[cnt]
    x1 = int(info_array[cnt + 1])
    y1 = img_h - int(info_array[cnt + 2])
    x2 = int(info_array[cnt + 3])
    y2 = img_h - int(info_array[cnt + 4])
    center_x = int((x1 + x2)/2)
    center_y = int((y1 + y2)/2)

    # draw = ImageDraw.Draw(img)
    # draw.rectangle((x1, y1, x2, y2), outline = "red")
    # draw.text((center_x, center_y), letter, fill = 'red')
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.putText(img, letter, (center_x, center_y), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
cv2.imshow('cv_image', img)
cv2.waitKey(0)       
# img.show()


# #================#
# #   辨識結果存檔
# #================#
# save_img_path = "img/letter_detected.png"
# img.save(save_img_path, "PNG")
