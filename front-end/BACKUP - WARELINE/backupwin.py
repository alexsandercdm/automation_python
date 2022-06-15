# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backup.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
import datetime
import shutil
import os
import time

class Ui_main_backup(object):

    def backupStart(self):

        try:
            _path = Path('c:/Users/Gestor-ti/Documents/Novo')

            dir = Path('c:/Users/Gestor-ti/Documents/TESTES')
            arquivos = os.listdir(dir)
            arqui = []

            diretorio = Path('c:/Users/Gestor-ti/Documents/TESTES/')

            for x in arquivos:
                arqui.append(x)
            print(len(arqui))

        except:
            print('Primeira Fase')

        try:
            print(diretorio)

            dadosArquivo = []

            for y in arqui:
                arquivo = diretorio / f'{y}'
                print(arquivo.stat().st_size)
                arquivoResultado = arquivo.stat().st_mtime
                time_str = datetime.datetime.fromtimestamp(arquivoResultado).strftime('%d/%m/%Y')
                dadosArquivo.append(time_str)

            datahj = datetime.date.today()
            _datahj = datahj - datahj.replace(day=1)
            dataFinal = f'{_datahj.days}/{datahj.month}/{datahj.year}'

        except:
            print('Segunda Fase')

        print(dataFinal)
        print(dadosArquivo)

        try:
            self.progressBarValue = 0

            for nome, data in zip(arqui, dadosArquivo):
                shutil.copyfile(
                    f'c:/Users/Gestor-ti/Documents/TESTES/{nome}',
                    os.path.join(f'{_path}', f'{nome}'))
                self.progressBarValue += 1
                time.sleep(0.1)
                self.progressBarBackup.setValue(self.progressBarValue)
                print('Finalizado')



        except FileNotFoundError:
            print(FileNotFoundError, 'Terceira Fase')


    def setupUi(self, main_backup):
        main_backup.setObjectName("main_backup")
        main_backup.setWindowModality(QtCore.Qt.NonModal)
        main_backup.resize(350, 110)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_backup.sizePolicy().hasHeightForWidth())
        main_backup.setSizePolicy(sizePolicy)
        main_backup.setMinimumSize(QtCore.QSize(350, 110))
        main_backup.setMaximumSize(QtCore.QSize(2048, 1080))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        main_backup.setFont(font)
        self.centralwidget_layout = QtWidgets.QWidget(main_backup)
        self.centralwidget_layout.setMinimumSize(QtCore.QSize(300, 100))
        self.centralwidget_layout.setObjectName("centralwidget_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget_layout)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_base = QtWidgets.QWidget(self.centralwidget_layout)
        self.widget_base.setObjectName("widget_base")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_base)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_back = QtWidgets.QFrame(self.widget_base)
        self.frame_back.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_back.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_back.setObjectName("frame_back")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_back)
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.campoUpdate = QtWidgets.QLineEdit(self.frame_back)
        self.campoUpdate.setMinimumSize(QtCore.QSize(0, 25))
        self.campoUpdate.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgba(120,120,120,60);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgba(30,30,30,100);\n"
"}")
        self.campoUpdate.setInputMask("")
        self.campoUpdate.setText("")
        self.campoUpdate.setObjectName("campoUpdate")
        self.verticalLayout.addWidget(self.campoUpdate)
        self.iniciarBackup = QtWidgets.QPushButton(self.frame_back)
        self.iniciarBackup.setMinimumSize(QtCore.QSize(0, 40))
        self.iniciarBackup.setStyleSheet("QPushButton{    \n"
"    \n"
"    font: 20pt \"Humanst521 Lt BT\";\n"
"    color: rgb(200,200,200);\n"
"    background-color: rgb(100,100,100);\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(110,110,110);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(120,120,120);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background-color: rgb(191,0,0);\n"
"}")
        self.iniciarBackup.setObjectName("iniciarBackup")
        self.iniciarBackup.clicked.connect(self.backupStart)
        self.verticalLayout.addWidget(self.iniciarBackup)
        self.lineSeparacao = QtWidgets.QFrame(self.frame_back)
        self.lineSeparacao.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSeparacao.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSeparacao.setObjectName("lineSeparacao")
        self.verticalLayout.addWidget(self.lineSeparacao)
        self.progressBarBackup = QtWidgets.QProgressBar(self.frame_back)
        self.progressBarBackup.setMinimumSize(QtCore.QSize(5, 0))
        self.progressBarBackup.setProperty("value", 0)
        self.progressBarBackup.setObjectName("progressBarBackup")
        self.verticalLayout.addWidget(self.progressBarBackup)
        self.horizontalLayout_3.addWidget(self.frame_back)
        self.frame_rolagem = QtWidgets.QFrame(self.widget_base)
        self.frame_rolagem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_rolagem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_rolagem.setObjectName("frame_rolagem")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_rolagem)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.frame_rolagem)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout_2.addWidget(self.verticalScrollBar)
        self.horizontalLayout_3.addWidget(self.frame_rolagem)
        self.horizontalLayout.addWidget(self.widget_base)
        main_backup.setCentralWidget(self.centralwidget_layout)

        self.retranslateUi(main_backup)
        QtCore.QMetaObject.connectSlotsByName(main_backup)

    def retranslateUi(self, main_backup):
        _translate = QtCore.QCoreApplication.translate
        main_backup.setWindowTitle(_translate("main_backup", "BACKUP - WARELINE"))
        self.campoUpdate.setPlaceholderText(_translate("main_backup", "Digite qualquer coisa aqui!"))
        self.iniciarBackup.setText(_translate("main_backup", "INICIAR BACKUP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_backup = QtWidgets.QMainWindow()
    ui = Ui_main_backup()
    ui.setupUi(main_backup)
    main_backup.show()
    sys.exit(app.exec_())
