import pyautogui, os, time
os.chdir(r'D:\Drive\Code\ATBSWP\Chapter_18')

def commentAfterDelay():
    pyautogui.click(100,100)
    pyautogui.typewrite('In IDLE, Alt-3 comments out a line.')
    time.sleep(2)
    pyautogui.hotkey('alt','3')

commentAfterDelay()