import pyautogui, time
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
test = pyautogui.size()
print(test)
for i in range(10):
    test =pyautogui.position()
    time.sleep(0.5)
    print(test)
    continue
    pyautogui.moveRel(100,  0, duration=0.25)
    pyautogui.moveRel(0,    100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0,    -100, duration=0.25)

