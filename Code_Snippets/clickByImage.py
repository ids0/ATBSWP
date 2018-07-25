import pyautogui, os
os.chdir(r'D:\Drive\Code\ATBSWP\Chapter_18')
image = list(pyautogui.locateAllOnScreen('submit.png'))
imageCenter = pyautogui.center(image[0])
pyautogui.click(imageCenter)