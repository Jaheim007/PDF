# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pdf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(830, 639)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 831, 651))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 831, 641))
        self.label.setPixmap(QPixmap(u":/images/Static/wallpaper.webp"))
        self.label.setScaledContents(True)
        self.tableWidget = QTableWidget(self.page)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(60, 80, 661, 421))
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(220)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.refresh_btn = QPushButton(self.page)
        self.refresh_btn.setObjectName(u"refresh_btn")
        self.refresh_btn.setGeometry(QRect(50, 520, 121, 51))
        self.register_btn = QPushButton(self.page)
        self.register_btn.setObjectName(u"register_btn")
        self.register_btn.setGeometry(QRect(180, 520, 181, 51))
        self.open_pdf_btn = QPushButton(self.page)
        self.open_pdf_btn.setObjectName(u"open_pdf_btn")
        self.open_pdf_btn.setGeometry(QRect(370, 520, 141, 51))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 831, 641))
        self.label_2.setPixmap(QPixmap(u":/images/Static/wallpaper.webp"))
        self.label_2.setScaledContents(True)
        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(230, 40, 371, 551))
        self.frame.setStyleSheet(u"background-color: #C2DFFF;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 20, 171, 51))
        self.label_3.setStyleSheet(u"font: 20pt \"Avenir\";\n"
"")
        self.nom = QLineEdit(self.frame)
        self.nom.setObjectName(u"nom")
        self.nom.setGeometry(QRect(20, 100, 331, 41))
        self.nom.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.prenom = QLineEdit(self.frame)
        self.prenom.setObjectName(u"prenom")
        self.prenom.setGeometry(QRect(20, 180, 331, 41))
        self.prenom.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.email = QLineEdit(self.frame)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(20, 260, 331, 41))
        self.email.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.mdp = QLineEdit(self.frame)
        self.mdp.setObjectName(u"mdp")
        self.mdp.setGeometry(QRect(20, 340, 331, 41))
        self.mdp.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.mdp.setEchoMode(QLineEdit.Password)
        self.cmdp = QLineEdit(self.frame)
        self.cmdp.setObjectName(u"cmdp")
        self.cmdp.setGeometry(QRect(20, 420, 331, 41))
        self.cmdp.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cmdp.setEchoMode(QLineEdit.Password)
        self.saveuser_btn = QPushButton(self.frame)
        self.saveuser_btn.setObjectName(u"saveuser_btn")
        self.saveuser_btn.setGeometry(QRect(110, 490, 161, 41))
        self.saveuser_btn.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(255,255,255)\n"
"}")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Prenom", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.refresh_btn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.register_btn.setText(QCoreApplication.translate("MainWindow", u"Enregister une personne ", None))
        self.open_pdf_btn.setText(QCoreApplication.translate("MainWindow", u"Ouvir un PDF", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">S'Inscrire </span></p></body></html>", None))
        self.nom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.prenom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prenom", None))
        self.email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.mdp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mot de passe ", None))
        self.cmdp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirmez le mot de passe", None))
        self.saveuser_btn.setText(QCoreApplication.translate("MainWindow", u"Enregister", None))
    # retranslateUi

