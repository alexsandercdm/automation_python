# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'automacao-frontend-v1.0.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import sys


class Ui_automacao_atendimento(object):

    def setupUi(self, automacao_atendimento):
        automacao_atendimento.setObjectName("automacao_atendimento")
        automacao_atendimento.setWindowModality(QtCore.Qt.NonModal)
        automacao_atendimento.resize(400, 300)
        automacao_atendimento.setMaximumSize(QtCore.QSize(400, 300))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        automacao_atendimento.setFont(font)
        automacao_atendimento.setIconSize(QtCore.QSize(24, 24))
        automacao_atendimento.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        automacao_atendimento.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(automacao_atendimento)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 391, 251))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_alterarcenso = QtWidgets.QWidget()
        self.tab_alterarcenso.setObjectName("tab_alterarcenso")
        self.atdcancelar = QtWidgets.QLabel(self.tab_alterarcenso)
        self.atdcancelar.setGeometry(QtCore.QRect(10, 10, 111, 20))
        self.atdcancelar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.atdcancelar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.atdcancelar.setObjectName("atdcancelar")
        self.atdobservacao = QtWidgets.QLabel(self.tab_alterarcenso)
        self.atdobservacao.setGeometry(QtCore.QRect(10, 40, 131, 21))
        self.atdobservacao.setObjectName("atdobservacao")
        self.dadoobservacao = QtWidgets.QLineEdit(self.tab_alterarcenso)
        self.dadoobservacao.setGeometry(QtCore.QRect(140, 40, 113, 20))
        self.dadoobservacao.setObjectName("dadoobservacao")
        self.exibirdados = QtWidgets.QListView(self.tab_alterarcenso)
        self.exibirdados.setGeometry(QtCore.QRect(10, 70, 371, 151))
        self.exibirdados.setObjectName("exibirdados")
        self.dadoscancelamento = QtWidgets.QLineEdit(self.tab_alterarcenso)
        self.dadoscancelamento.setGeometry(QtCore.QRect(140, 10, 113, 20))
        self.dadoscancelamento.setObjectName("dadoscancelamento")
        self.alterarcenso = QtWidgets.QPushButton(self.tab_alterarcenso)
        self.alterarcenso.setGeometry(QtCore.QRect(270, 10, 111, 51))
        self.alterarcenso.setObjectName("alterarcenso")
        self.tabWidget.addTab(self.tab_alterarcenso, "")
        self.tab_alterarplano = QtWidgets.QWidget()
        self.tab_alterarplano.setObjectName("tab_alterarplano")
        self.tabWidget.addTab(self.tab_alterarplano, "")
        automacao_atendimento.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(automacao_atendimento)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 23))
        self.menubar.setMaximumSize(QtCore.QSize(400, 300))
        self.menubar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuCENSO = QtWidgets.QMenu(self.menubar)
        self.menuCENSO.setObjectName("menuCENSO")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        automacao_atendimento.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(automacao_atendimento)
        self.statusbar.setObjectName("statusbar")
        automacao_atendimento.setStatusBar(self.statusbar)
        self.actionSair = QtWidgets.QAction(automacao_atendimento)
        self.actionSair.setObjectName("actionSair")
        self.menuCENSO.addAction(self.actionSair)
        self.menubar.addAction(self.menuCENSO.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(automacao_atendimento)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(automacao_atendimento)

    def retranslateUi(self, automacao_atendimento):
        _translate = QtCore.QCoreApplication.translate
        automacao_atendimento.setWindowTitle(_translate("automacao_atendimento", "Automação - Atendimento"))
        self.atdcancelar.setText(_translate("automacao_atendimento", "ATD. P/ CANCELAR"))
        self.atdobservacao.setText(_translate("automacao_atendimento", "ATD P/ OBSERVAÇÕES"))
        self.alterarcenso.setText(_translate("automacao_atendimento", "INICIAR EXECUÇÃO"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_alterarcenso), _translate("automacao_atendimento", "Alterar Censo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_alterarplano), _translate("automacao_atendimento", "Alterar Plano"))
        self.menuCENSO.setTitle(_translate("automacao_atendimento", "Arquivo"))
        self.menuHelp.setTitle(_translate("automacao_atendimento", "Help"))
        self.actionSair.setText(_translate("automacao_atendimento", "Sair"))

'''    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.window.show()
        self.app.exec_()
'''
