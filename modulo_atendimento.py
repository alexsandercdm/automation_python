from PyQt5 import QtWidgets, uic, QtGui
from time import sleep
import pyautogui
import sys

class Interface(QtWidgets.QMainWindow):


    def __init__(self):

        super(Interface, self).__init__()
        uic.loadUi("front-end/automacao-frontend-v1.0.ui", self)

        self.alteratd = self.findChild(QtWidgets.QLineEdit, 'dadoscancelamento')
        self.obsatd = self.findChild(QtWidgets.QLineEdit, 'dadosobservacao')
        self.obsatd.returnPressed.connect(self.append_clear)

        self.inserir_dados = self.findChild(QtWidgets.QPushButton, 'inserirdados')
        self.inserir_dados.clicked.connect(self.append_clear)

        self.execucao = self.findChild(QtWidgets.QPushButton, 'alterarcenso')
        self.execucao.clicked.connect(self.alterar_censo)

        self.list_view = self.findChild(QtWidgets.QListView, 'exibirdados')
        self.list_entry = QtGui.QStandardItemModel()
        self.list_view.setModel(self.list_entry)

        self._lista = [ ]
        self._obser = [ ]

        self.show()

    def append_clear(self):

        self._lista.append(self.alteratd.text())
        self._obser.append(self.obsatd.text())

        self.atendimento = self.alteratd.text()
        self.observacao = self.obsatd.text()
        if self.alteratd.text() != '' and self.obsatd.text() != '':
            self.alteratd.clear()
            self.obsatd.clear()
            self.dados_formats = f'{self.atendimento} --- DUPLICADO {self.observacao}'
            self.it = QtGui.QStandardItem(self.dados_formats)
            self.list_entry.appendRow(self.it)
        else:
            print('Dados não podem ser nulos!')

    def alterar_censo(self):
        """
        1º - PASSO: ABRIR MENU DA WARELINE
        menu_ico: faz a verredura e identifica se o mesmo já está aberta, caso sim, moveTo até a posição
        Caso não, abre o executavel do windows, e digita o endereço de .exe
        executa o menu.
        """
        print('Abrindo menu...')
        try:
            menu_ico = pyautogui.locateCenterOnScreen(r'modulos/menu-ico.png', confidence=0.9)
            pyautogui.moveTo(menu_ico[ 0 ], menu_ico[ 1 ], 0.3)
            pyautogui.click()
        except:
            pyautogui.hotkey('win', 'r')
            pyautogui.typewrite('C:\WareWin\menu.exe\n', interval=0.1)

        sleep(5)
        """
        2º - PASSO: ABRIR MODULO ATENDIMENTO
        modulos_atendimento: identifica se o modelo está na tela, caso sim, abre, caso não, para.
        """

        print('Abrindo Modulo...')

        modulo_atendimento = pyautogui.locateCenterOnScreen(r'modulos/atendimento.png', confidence=0.99)
        try:
            if not modulo_atendimento:
                print('Modulo Nao encontrado')
            else:
                pyautogui.moveTo(340, 210, 0.2)
                pyautogui.doubleClick()

                sleep(6)
                print('Logando...')
                """
                # 3º - PASSO: LOGAR COM USUARIO E SENHA
                login: identifica se existe a tela de login
                login: caso apresente erro no login, o mesmo repete a digitacao do login/senha
                """

                login = pyautogui.locateAllOnScreen(r'modulos/login.png', confidence=0.9)
                login_tentava = pyautogui.locateAllOnScreen(r'modulos/login-tentaiva.png', confidence=0.9)

                login_usuario = 'ALEXSANDER'
                login_senha = 'ware2019'
                print(login)

                if not login:
                    print('Não foi possivel realiza o login')
                else:
                    pyautogui.typewrite(login_usuario, interval=0.2)
                    pyautogui.press('enter')
                    pyautogui.typewrite(login_senha, interval=0.2)
                    pyautogui.press('enter')
                    '''
                    if not login_tentava:
                        print('nova tentativa de login não foi realizada com sucesso')
                        pyautogui.moveTo(594, 452, 0.1)
                        pyautogui.doubleClick()
                        pyautogui.typewrite(login_usuario, interval=0.2)
                        pyautogui.press('enter')
                        pyautogui.typewrite(login_senha, interval=0.2)
                        pyautogui.press('enter')
                        print('login realizado com sucesso')
                    '''

                sleep(1)
                print('Atendimento')
                pyautogui.moveTo(43, 35, 0.2)
                pyautogui.click()

                sleep(3)
                print('Filtros')
                pyautogui.moveTo(329, 597, 0.3)
                pyautogui.click()

                pyautogui.moveTo(337, 672, 0.2)
                pyautogui.click()

                # Digita o atendimento nos campos de pesquisa.
                for lista, observacao in zip(self._lista, self._obser):
                    obs = str(observacao)
                    pyautogui.typewrite(lista)
                    pyautogui.press('enter')
                    pyautogui.press('enter')

                    sleep(2)

                    atendimento_externo = pyautogui.locateCenterOnScreen(
                        r'modulos/atendimento-externo.png', confidence=0.9
                    )

                    if not atendimento_externo:
                        pass
                    else:
                        censo_externo = pyautogui.locateCenterOnScreen(r'modulos/censo-externo.png', confidence=0.9)
                        print(censo_externo)

                        if not censo_externo:
                            print('Não identificado')
                            pass
                        else:
                            pyautogui.moveTo(censo_externo[ 0 ] + 3, censo_externo[ 1 ], 0.2)
                            pyautogui.click()

                            pyautogui.press('s')
                            pyautogui.press('s')

                            confirmacao_censo = pyautogui.locateOnScreen(r'modulos/confirmacao-censo.png', confidence=0.9)

                            if not confirmacao_censo:
                                # Botão alterar

                                pyautogui.moveTo(560, 510, 0.2)
                                pyautogui.click()

                                # Seta para motivo de cancelamento
                                pyautogui.moveTo(884, 311, 0.2)
                                pyautogui.click()

                                # Selecionando o Motivo
                                pyautogui.moveTo(557, 458, 0.2)
                                pyautogui.click()

                                # Clicando em descrição e digitando
                                print('Clicando em descrição e digitando')
                                print(obs)
                                pyautogui.moveTo(564, 395, 0.2)
                                pyautogui.doubleClick()
                                sleep(1)
                                pyautogui.typewrite(observacao)

                                # Clicando em Gravar e confirmando
                                print('Clicando em Gravar e confirmando')
                                pyautogui.moveTo(482, 513, 0.2)
                                pyautogui.click()
                                pyautogui.moveTo(726, 430, 0.2)
                                pyautogui.click()

                                # Fechar
                                pyautogui.press('esc')
                                pyautogui.press('s')

                                sleep(1)

                            else:
                                pyautogui.moveTo(707, 441, 0.2)
                                pyautogui.click()
                                # Botão alterar
                                pyautogui.moveTo(560, 510, 0.2)
                                pyautogui.click()

                                # Seta para motivo de cancelamento
                                pyautogui.moveTo(884, 311, 0.2)
                                pyautogui.click()

                                # Selecionando o Motivo
                                pyautogui.moveTo(557, 458, 0.2)
                                pyautogui.click()

                                # Clicando em descrição e digitando
                                print('Clicando em descrição e digitando')
                                print(obs)
                                pyautogui.moveTo(564, 395, 0.2)
                                pyautogui.doubleClick()
                                sleep(1)
                                pyautogui.typewrite(observacao)

                                # Clicando em Gravar e confirmando
                                print('Clicando em Gravar e confirmando')
                                pyautogui.moveTo(482, 513, 0.2)
                                pyautogui.click()
                                pyautogui.moveTo(726, 430, 0.2)
                                pyautogui.click()

                                # Fechar
                                pyautogui.press('esc')
                                pyautogui.press('s')

                                sleep(1)

                    atendimento_ambulatorial = pyautogui.locateCenterOnScreen(
                        r'modulos/atendimento-ambulatorial.png', confidence=0.9
                    )

                    if not atendimento_ambulatorial:
                        pass
                    else:
                        censo_ambulatorial = pyautogui.locateCenterOnScreen(r'modulos/censo.png', confidence=0.9)

                        if not censo_ambulatorial:
                            print('Não identificado')
                            pass
                        else:
                            pyautogui.moveTo(censo_ambulatorial[ 0 ] + 3, censo_ambulatorial[ 1 ], 0.2)
                            pyautogui.click()

                            confirmacao_censo = pyautogui.locateOnScreen(r'modulos/confirmacao-censo.png', confidence=0.9)
                            pyautogui.press('s')
                            pyautogui.press('s')

                            if not confirmacao_censo:
                                # Botão alterar
                                pyautogui.moveTo(560, 510, 0.2)
                                pyautogui.click()

                                # Seta para motivo de cancelamento
                                pyautogui.moveTo(884, 311, 0.2)
                                pyautogui.click()

                                # Selecionando o Motivo
                                pyautogui.moveTo(557, 458, 0.2)
                                pyautogui.click()

                                # Clicando em descrição e digitando
                                print('Clicando em descrição e digitando')
                                print(obs)
                                pyautogui.moveTo(564, 395, 0.2)
                                pyautogui.doubleClick()
                                sleep(1)
                                pyautogui.typewrite(observacao)

                                # Clicando em Gravar e confirmando
                                print('Clicando em Gravar e confirmando')
                                pyautogui.moveTo(482, 513, 0.2)
                                pyautogui.click()
                                pyautogui.moveTo(726, 430, 0.2)
                                pyautogui.click()

                                # Fechar
                                pyautogui.press('esc')
                                pyautogui.press('s')

                                sleep(1)

                            else:
                                pyautogui.moveTo(707, 441, 0.2)
                                pyautogui.click()
                                # Botão alterar
                                pyautogui.moveTo(560, 510, 0.2)
                                pyautogui.click()

                                # Seta para motivo de cancelamento
                                pyautogui.moveTo(884, 311, 0.2)
                                pyautogui.click()

                                # Selecionando o Motivo
                                pyautogui.moveTo(557, 458, 0.2)
                                pyautogui.click()

                                # Clicando em descrição e digitando
                                print('Clicando em descrição e digitando')
                                print(obs)
                                pyautogui.moveTo(564, 395, 0.2)
                                pyautogui.doubleClick()
                                sleep(1)
                                pyautogui.typewrite(observacao)

                                # Clicando em Gravar e confirmando
                                print('Clicando em Gravar e confirmando')
                                pyautogui.moveTo(482, 513, 0.2)
                                pyautogui.click()
                                pyautogui.moveTo(726, 430, 0.2)
                                pyautogui.click()

                                # Fechar
                                pyautogui.press('esc')
                                pyautogui.press('s')

                                sleep(1)
                    atendimento_internacao = pyautogui.locateCenterOnScreen(
                        r'modulos/atendimento-internacao.png', confidence=0.9
                    )

                    if not atendimento_internacao:
                        pass
                    else:
                        censo_internacao = pyautogui.locateCenterOnScreen(r'modulos/censo-internacao.png', confidence=0.9)

                        if not censo_internacao:
                            print('Não identificado')
                            pass
                        else:
                            pyautogui.moveTo(censo_internacao[ 0 ] + 3, censo_internacao[ 1 ], 0.2)
                            pyautogui.click()

                            confirmacao_censo = pyautogui.locateOnScreen(r'modulos/confirmacao-censo.png', confidence=0.9)

                            if not confirmacao_censo:
                                # Botão alterar
                                pyautogui.moveTo(560, 510, 0.2)
                                pyautogui.click()

                                pyautogui.press('s')
                                pyautogui.press('s')

                                # Seta para motivo de cancelamento
                                pyautogui.moveTo(884, 311, 0.2)
                                pyautogui.click()

                                # Selecionando o Motivo
                                pyautogui.moveTo(557, 458, 0.2)
                                pyautogui.click()

                                # Clicando em descrição e digitando
                                print('Clicando em descrição e digitando')
                                print(obs)
                                pyautogui.moveTo(564, 395, 0.2)
                                pyautogui.doubleClick()
                                sleep(1)
                                pyautogui.typewrite(observacao)

                                # Clicando em Gravar e confirmando
                                print('Clicando em Gravar e confirmando')
                                pyautogui.moveTo(482, 513, 0.2)
                                pyautogui.click()
                                pyautogui.moveTo(726, 430, 0.2)
                                pyautogui.click()

                                # Fechar
                                pyautogui.press('esc')
                                pyautogui.press('s')

                                sleep(1)

                            else:
                                pyautogui.moveTo(707, 441, 0.2)
                                pyautogui.click()
                                # Botão alterar
                                pyautogui.moveTo(560, 510, 0.2)
                                pyautogui.click()

                                # Seta para motivo de cancelamento
                                pyautogui.moveTo(884, 311, 0.2)
                                pyautogui.click()

                                # Selecionando o Motivo
                                pyautogui.moveTo(557, 458, 0.2)
                                pyautogui.click()

                                # Clicando em descrição e digitando
                                print('Clicando em descrição e digitando')
                                print(obs)
                                pyautogui.moveTo(564, 395, 0.2)
                                pyautogui.doubleClick()
                                sleep(1)
                                pyautogui.typewrite(observacao)

                                # Clicando em Gravar e confirmando
                                print('Clicando em Gravar e confirmando')
                                pyautogui.moveTo(482, 513, 0.2)
                                pyautogui.click()
                                pyautogui.moveTo(726, 430, 0.2)
                                pyautogui.click()

                                # Fechar
                                pyautogui.press('esc')
                                pyautogui.press('s')

                                sleep(1)

        except FileNotFoundError:
            print(FileNotFoundError)



app = QtWidgets.QApplication(sys.argv)
window = Interface()
app.exec_()