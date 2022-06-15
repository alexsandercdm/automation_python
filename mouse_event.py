import pyautogui

list = [ ]
entrada = input('Aperte o 1: ')

x = pyautogui.position()

if entrada == 1:
    list.append(x)
print(x)




