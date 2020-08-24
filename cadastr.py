import cv2
import pyautogui as PG
import numpy as np
import imutils
import time
import functions as FN



img_detail_title = cv2.imread('detail_title.png') #поиск кнопки поиска кадастра

cadastr_list = [
    '5123781400:01:001:1139',
    '5123781400:01:001:1122',
    '5123781400:01:001:1120',
    '5123781400:01:001:1104',
    '5121010100:01:004:0286',
    '5121010100:01:004:0188',
    '5121010100:01:004:0189',
    '5121010100:01:004:0010',
    '5121010100:01:004:0183',
    '5121010100:01:004:0186',
    '5121010100:01:004:0191',
    '5121010100:01:004:0193',
    '5121010100:01:004:0265',
    '5121010100:01:004:0287',
    '5121010100:01:004:0185',
    '5121010100:01:004:0495',
    '5121010100:01:004:0180',
    '5121010100:01:004:0044',
    '5121010100:01:004:0179',
    '5121010100:01:004:0181',
    '5121010100:01:004:0182',
    '5121010100:01:004:0184',
    '5121010100:01:004:0192',
    '5121010100:01:004:0196',
    '5121010100:01:004:0197',
    '5121010100:01:004:0198',
    '5121010100:01:004:0261'

]

list_value = FN.parser_html()
FN.generate_excel(list_value)

#for value in list_value:
#    print(value.key)
#    print(value.value)
#    print("-------")

#time.sleep(3)

#url_cadaster = "https://e.land.gov.ua/back/cadaster/?cad_num="
#?cad_num=1222080500%3A01%3A001%3A0027
#for cadastr in cadastr_list:
#    FN.open_page_in_new_tab(url_cadaster+cadastr)
#    time.sleep(1)

#time.sleep(3)

#for cadastr in cadastr_list:
#FN.main_process(cadastr)


#НЕ РАБОТАЕТ, ПРОВЕРИТЬ ПОЧЕМУ?
#status = FN.compare_img(img_detail_title)
#frame = FN.get_screenshot()
#cv2.imshow("Screenshot", frame)
#if (status == False):
#    print("НЕ открыта деталка")


cv2.waitKey(0)