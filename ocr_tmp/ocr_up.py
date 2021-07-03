# -*- coding: UTF-8 -*-
# import pytesseract
# from PIL import Image
 
# img = Image.open("alphabet_ocr.png")
# code = pytesseract.image_to_string(img)
# print(code)

# # #!/usr/bin/python
# # -*- coding: UTF-8 -*-
import cv2
import sys
# import pyocr
# from PIL import Image
# import pytesseract
# import pyocr.builders
path = '/home/upup/Documents/ocr/img_mask.png'
img16 = cv2.imread(path,cv2.IMREAD_UNCHANGED) # flag)
cv2.imshow('ori',img16)
cv2.waitKey(0)

img8 = (img16/256).astype('uint8')
cv2.imshow('new',img8)
cv2.waitKey(0)

# tools = pyocr.get_available_tools()
# tool = tools[0]

# # cap = cv2.VideoCapture(0)


# imgs = Image.open('alphabet_ocr.png')
# imga = imgs.convert('L')
# ans = pytesseract.image_to_string(imga)
# print('OCR光學辨識：',ans)

# while True:  
#     # ret, frame = cap.read()

#     Height , Width, _ = imgs.shape#[:2]

#     img = cv2.resize(imgs,(int(Width),int(Height)))

#     #OCR 讀取範圍 紅框
#     cv2.rectangle(img, (100, 100), (Width-200,Height-200),(0, 0, 255), 10)

#     dst = img[100:Height-200,100:Width-200]#OCR讀出識別後印出

#     PIL_Image = Image.fromarray(dst)
#     text = tool.image_to_string(
#         PIL_Image,
#         lang = 'chi_tra+eng',
#         builder=pyocr.builders.TextBuilder())
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:

#         break
#     if k == 32:
#         if(text !=''):
#             print(text)
#             with open('識別的文字.txt','a',encoding='utf-8') as fObject:
#                 fObject.write(text+'\n')
                 
#     cv2.imshow('001',img)
#     cv2.waitKey(1)

# cap.release()
# cv2.destroyAllWindows()
