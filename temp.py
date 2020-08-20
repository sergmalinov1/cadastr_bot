#делаем скрин и перегоняем его в формат с которым работает opencv
img = pyautogui.screenshot() #делаем скриншот
frame = np.array(img) #подгоняем в формат с которым работает opencv
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #делаем коррекцию цвета. ибо к перегнанного изображения не верные цвета
cv2.imshow("Screenshot", frame)



pyautogui.size()
pyautogui.moveTo(100, 200)  # moves mouse to X of 100, Y of 200.

pyautogui.click()  # click the mouse
pyautogui.click(x=100, y=200)  # move to 100, 200, then click the left mouse button.
pyautogui.click(button='right')  # right-click the mouse


pyautogui.write('Hello world!')                 # prints out "Hello world!" instantly pyautogui.press('enter')  # press the Enter key
pyautogui.press('f1')     # press the F1 key
pyautogui.press('left')   # press the left arrow key
pyautogui.keyDown('shift')  # hold down the shift key
pyautogui.keyUp('shift')    # release the shift key

pyautogui.hotkey('ctrl', 'shift', 'esc')

######################


for cdr in cadastr_list:
    PG.moveTo(900, 270)  # фокус на поле ввода кадастрового номера
    PG.click()
    PG.hotkey('ctrl', 'a')

    PG.write(cdr)
    time.sleep(0.4)

    PG.press('tab')
    PG.press('enter')

    ##CHECK!!
    time.sleep(3)

    # download all data
    PG.hotkey('ctrl', 's')

    cadastr_name = cdr.replace(':', '_')

    time.sleep(1)
    PG.write(cadastr_name)
    time.sleep(0.1)

    PG.press('tab')
    time.sleep(0.1)

    PG.press('tab')
    time.sleep(0.2)

    PG.press('enter')
    time.sleep(0.6)

    # Save pdf

    PG.press('tab')
    time.sleep(0.1)

    PG.press('enter')
    time.sleep(0.6)

    PG.hotkey('ctrl', 'R')
    time.sleep(2)


#################################
frame = FN.get_screenshot()
FN.compare_img(frame, img_btn_show)
position = FN.find_element_position(frame, img_search_cadastr)
field_center = (position[0] + 200, position[1] + 30)
print(field_center)










