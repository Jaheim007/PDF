# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/pdf.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 639)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 831, 651))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(0, 0, 831, 641))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/Static/wallpaper.webp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.page)
        self.tableWidget.setGeometry(QtCore.QRect(60, 80, 661, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(220)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.refresh_btn = QtWidgets.QPushButton(self.page)
        self.refresh_btn.setGeometry(QtCore.QRect(50, 520, 121, 51))
        self.refresh_btn.setObjectName("refresh_btn")
        self.register_btn = QtWidgets.QPushButton(self.page)
        self.register_btn.setGeometry(QtCore.QRect(180, 520, 181, 51))
        self.register_btn.setObjectName("register_btn")
        self.open_pdf_btn = QtWidgets.QPushButton(self.page)
        self.open_pdf_btn.setGeometry(QtCore.QRect(370, 520, 141, 51))
        self.open_pdf_btn.setObjectName("open_pdf_btn")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 831, 641))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/Static/wallpaper.webp"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.page_2)
        self.frame.setGeometry(QtCore.QRect(230, 40, 371, 551))
        self.frame.setStyleSheet("background-color: #C2DFFF;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(100, 20, 171, 51))
        self.label_3.setStyleSheet("font: 20pt \"Avenir\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.nom = QtWidgets.QLineEdit(self.frame)
        self.nom.setGeometry(QtCore.QRect(20, 100, 331, 41))
        self.nom.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nom.setObjectName("nom")
        self.prenom = QtWidgets.QLineEdit(self.frame)
        self.prenom.setGeometry(QtCore.QRect(20, 180, 331, 41))
        self.prenom.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.prenom.setObjectName("prenom")
        self.email = QtWidgets.QLineEdit(self.frame)
        self.email.setGeometry(QtCore.QRect(20, 260, 331, 41))
        self.email.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.email.setObjectName("email")
        self.mdp = QtWidgets.QLineEdit(self.frame)
        self.mdp.setGeometry(QtCore.QRect(20, 340, 331, 41))
        self.mdp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mdp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mdp.setObjectName("mdp")
        self.cmdp = QtWidgets.QLineEdit(self.frame)
        self.cmdp.setGeometry(QtCore.QRect(20, 420, 331, 41))
        self.cmdp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cmdp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cmdp.setObjectName("cmdp")
        self.saveuser_btn = QtWidgets.QPushButton(self.frame)
        self.saveuser_btn.setGeometry(QtCore.QRect(110, 490, 161, 41))
        self.saveuser_btn.setStyleSheet("QPushButton{\n"
"background-color:rgb(255,255,255)\n"
"}")
        self.saveuser_btn.setObjectName("saveuser_btn")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Prenom"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Email"))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))
        self.register_btn.setText(_translate("MainWindow", "Enregister une personne "))
        self.open_pdf_btn.setText(_translate("MainWindow", "Ouvir un PDF"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">S\'Inscrire </span></p></body></html>"))
        self.nom.setPlaceholderText(_translate("MainWindow", "Nom"))
        self.prenom.setPlaceholderText(_translate("MainWindow", "Prenom"))
        self.email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.mdp.setPlaceholderText(_translate("MainWindow", "Mot de passe "))
        self.cmdp.setPlaceholderText(_translate("MainWindow", "Confirmez le mot de passe"))
        self.saveuser_btn.setText(_translate("MainWindow", "Enregister"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
