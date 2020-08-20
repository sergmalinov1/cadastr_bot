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
    '5123781400:01:001:1104'

]









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