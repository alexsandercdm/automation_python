import pyautogui
import time

time.sleep(3)

cadger = pyautogui.locateCenterOnScreen(r'icones/ate.png', confidence=0.9)

if cadger:
    print(cadger)
    print(cadger[0])
    print(cadger[1])
    print('Existe o item na tela')
    pyautogui.moveTo(cadger[ 0 ], cadger[ 1 ], 0.2)
    pyautogui.doubleClick()
else:
    print('não existe o item na tela')

time.sleep(8)

login =  pyautogui.locateCenterOnScreen(r'icones/login.png', confidence=0.9)

if login:
    pyautogui.typewrite('alexsander', interval=0)
    pyautogui.press('enter')
    pyautogui.typewrite('ware2019', interval=0)
    pyautogui.press('enter')
    login_tentiva = pyautogui.locateCenterOnScreen(r'icones/login-tentativa.png', confidence=0.9)
    if login_tentiva:
        print('erro no login')
    else:
        print(('login Realizado com sucesso'))
else:
    print('Não foi possivel fazer login')



