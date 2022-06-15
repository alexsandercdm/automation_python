import pyautogui
import time

print(pyautogui.position())
pyautogui.hotkey('win','r')
pyautogui.typewrite('C:\WareWin\menu.exe\n', interval=0)
time.sleep(10)
#pyautogui.moveTo(379, 753, duration=0.2)
pyautogui.click(180, 207, button='left', clicks=2)
time.sleep(10)
pyautogui.typewrite('alexsander', interval=0)
pyautogui.hotkey('tab')
#time.sleep(2)
pyautogui.typewrite('ware2019', interval=0)
#time.sleep(1)
pyautogui.hotkey('enter')
pyautogui.click(31, 35, button='left', clicks=1, interval=0.2)
pyautogui.click(86, 643, button='left', clicks=1, interval=0.2)
pyautogui.click(323, 414, button='left', clicks=1, interval=0.2)

print(pyautogui.position())