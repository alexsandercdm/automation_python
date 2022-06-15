import os
import pyautogui
from time import sleep
#from PIL import Image, ImageDraw, ImageFont

def abrir_menu():
    """
    1º - PASSO: ABRIR MENU DA WARELINE
    menu_ico: faz a verredura e identifica se o mesmo já está aberta, caso sim, moveTo até a posição
    Caso não, abre o executavel do windows, e digita o endereço de .exe
    executa o menu.
    """
    try:
        menu_ico = pyautogui.locateCenterOnScreen(r'modulos/menu-ico.png', confidence=0.9)
        pyautogui.moveTo(menu_ico[0], menu_ico[1], 0.3)
        pyautogui.click()
    except:
        pyautogui.hotkey('win', 'r')
        pyautogui.typewrite('C:\WareWin\menu.exe\n', interval=0.1)

    print('Abrindo menu...')


def abrir_modulo():
    """
    2º - PASSO: ABRIR MODULO FATURAS
    modulos_faturas: identifica se o modelo está na tela, caso sim, abre, caso não, para.
    """
    modulo_faturas = pyautogui.locateCenterOnScreen(r'modulos/faturas.png', confidence=0.9)
    try:
        if not modulo_faturas:
            print('Modulo Nao encontrado')
        else:
            pyautogui.moveTo(modulo_faturas[0], modulo_faturas[1], 0.2)
            pyautogui.doubleClick()
    except FileNotFoundError:
        print(FileNotFoundError)

    print('Abrindo Modulo...')



def logar_modulo():
    """
    # 3º - PASSO: LOGAR COM USUARIO E SENHA
    login: identifica se existe a tela de login
    login: caso apresente erro no login, o mesmo repete a digitacao do login/senha
    """
    login = pyautogui.locateAllOnScreen(r'modulos/login.png', confidence=0.9)
    login_tentava = pyautogui.locateAllOnScreen(r'modulos/login-tentaiva.png', confidence=0.9)

    login_usuario = 'ALEXSANDER'
    login_senha = 'ware2019'

    if login:
        pyautogui.typewrite(login_usuario, interval=0.2)
        pyautogui.press('enter')
        pyautogui.typewrite(login_senha, interval=0.2)
        pyautogui.press('enter')
        if login_tentava:
            pyautogui.moveTo(594, 452, 0.1)
            pyautogui.doubleClick()
            pyautogui.typewrite(login_usuario, interval=0.2)
            pyautogui.press('enter')
            pyautogui.typewrite(login_senha, interval=0.2)
            pyautogui.press('enter')
    else:
        print('Não foi possivel logar')

    print('Logando...')

def tab_matmed():
    """
    4º - PASSO: IR PARA TABELA DE SERVIÇO
    5º - PASSO: IR PARA MAT./MED. PRÓPRIA DOS CONVÊNIOS
    faturas_aberto: faz a verificação e validação para ver se o modulo se encontra aberto,
    caso não, para a execução, caso sim, conitua o processo.
    """

    try:
        faturas_aberto = pyautogui.locateOnScreen(r'modulos/faturas-aberto.png', confidence=0.99)
    except:
        print('erro')

    if not faturas_aberto:
        print('Não está aberto ainda')
    else:

        # Tabela de Servico
        pyautogui.moveTo(109, 35, 0.2)
        pyautogui.click()
        # Mat./Med Proprio dos Convenios
        pyautogui.moveTo(161, 226, 0.2)
        pyautogui.click()

    print('Acessando tabela...')

def pesquisa_de_item():
    """
    6º - PASSO: SELECIONAR O TIPO DA TABELA
    7º - PASSO: SELECIONAR A PESQUISA P/ CÓDIGO PRÓPRIO
    8º - PASSO: PESQUISAR ITEM (FORMATAR O CAMPO P/ 8 DIGITOS C/ ZEROS A ESQUERDA)
    9º - PASSO: CLICAR NO ITEM
    10º - PASSO: IR ATÉ VALOR MAT/MED
    11º - PASSO: VALIDAR SE ESTA CORRETO, CASO NÃO, CORRIGIR
    12º - PASSO: SALVAR E CONFIRMAR
    13º - PASSO: REPETIR DO PASSO 7º
    """
    print('Atualizando valores...')

    # Tipo de Tabela
    pyautogui.moveTo(491, 546, 0.2)
    pyautogui.doubleClick()
    pyautogui.typewrite('13', 0.2)
    pyautogui.press('enter')
    # Filtro Cod. Proprio
    pyautogui.moveTo(140, 526, 0.2)
    pyautogui.click()
    # Filtro pesquisa

    valor_pesquisa = ['00000248', '00000272', '00000426', '00036811', '00000450']
    preco_p_alterar = ['0,3900', '0,9375', '0,3700', '0,0200', '0,7126']

    for pesquisa, preco in zip(valor_pesquisa, preco_p_alterar):
        pyautogui.moveTo(42, 548, 0.2)
        pyautogui.doubleClick()
        pyautogui.press('del')
        pyautogui.typewrite(pesquisa, 0.2)
        pyautogui.press('enter')

        pyautogui.screenshot(f'prints/pesquisa_{pesquisa}.png', region=(26, 538, 80, 18))

        pyautogui.moveTo(74, 550, 1)
        pyautogui.doubleClick()
        pyautogui.press('del')
        pyautogui.moveTo(1336, 145)
        pyautogui.doubleClick()

        barra_pesquisa = pyautogui.locateAllOnScreen(
            f'prints/pesquisa_{pesquisa}.png', confidence=0.9, region=(150, 150, 300, 326))

        for pos in barra_pesquisa:
            pyautogui.moveTo(pos[ 0 ] + 20, pos[ 1 ] + 10, 0.9)
            pyautogui.doubleClick()
            # alterar preço
            pyautogui.moveTo(489, 498, 0.5)
            pyautogui.doubleClick()
            pyautogui.typewrite(preco, 0.2)
            sleep(1.5)
            # salvar alteracao
            pyautogui.moveTo(87, 70, 0.3)
            pyautogui.click()
            pyautogui.moveTo(652, 442, 0.5)
            pyautogui.click()
            # fechar
            # pyautogui.moveTo(987, 154, 0.6)
            # pyautogui.click()

    '''
    img_pesquisa = Image.new("RGB", (270,50), color=(255,255,192,0))
    font = ImageFont.truetype(r'fonts/courier-normal.ttf', 48)
    img_pesquisa1 = ImageDraw.Draw(img_pesquisa)
    img_pesquisa1.text((0,0), text=valor_pesquisa, font=font, fill=0, align="left")
    img_pesquisa.save(f'prints/pesquisa_{valor_pesquisa}.png', "PNG")
    '''
def remover_arquivos():

    pesquisa = []
    path = 'prints/'
    dir = os.listdir(path)
    for file in dir:
        pesquisa.append(file[9:17])
    for file1, pesq in zip(dir, pesquisa):
        if file1 == (f'pesquisa_{pesq}.png'):
            os.remove(f'prints/{file1}')


sleep(1)
abrir_menu()
sleep(6)
abrir_modulo()
sleep(6)
logar_modulo()
sleep(2)
tab_matmed()
sleep(2)
pesquisa_de_item()
sleep(2)
remover_arquivos()
pyautogui.alert('Programa Finalizado')
