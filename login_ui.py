# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Admin\Desktop\Sidebar\logo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 375)
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, 6, 10, -1)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.central_picture = QtWidgets.QVBoxLayout()
        self.central_picture.setSpacing(15)
        self.central_picture.setObjectName("central_picture")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.central_picture.addItem(spacerItem)
        self.name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.central_picture.addWidget(self.name)
        self.picture = QtWidgets.QLabel(self.centralwidget)
        self.picture.setMaximumSize(QtCore.QSize(300, 200))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("C:\\Users\\Admin\\Desktop\\Sidebar\\logo_view/logo.svg"))
        self.picture.setScaledContents(True)
        self.picture.setObjectName("picture")
        self.central_picture.addWidget(self.picture)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.central_picture.addItem(spacerItem1)
        self.gridLayout.addLayout(self.central_picture, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(47, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.central_sign_in = QtWidgets.QVBoxLayout()
        self.central_sign_in.setObjectName("central_sign_in")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.central_sign_in.addItem(spacerItem3)
        self.sing_in_welcome = QtWidgets.QVBoxLayout()
        self.sing_in_welcome.setSpacing(8)
        self.sing_in_welcome.setObjectName("sing_in_welcome")
        self.welcome = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.welcome.setFont(font)
        self.welcome.setObjectName("welcome")
        self.sing_in_welcome.addWidget(self.welcome)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sing_in_welcome.addItem(spacerItem4)
        self.error_msg = QtWidgets.QLabel(self.centralwidget)
        self.error_msg.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        self.error_msg.setFont(font)
        self.error_msg.setStyleSheet("background-color: rgba(255, 115, 92, 50);\n"
"")
        self.error_msg.setObjectName("error_msg")
        self.sing_in_welcome.addWidget(self.error_msg)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sing_in_welcome.addItem(spacerItem5)
        self.sign_in = QtWidgets.QVBoxLayout()
        self.sign_in.setObjectName("sign_in")
        self.login = QtWidgets.QHBoxLayout()
        self.login.setObjectName("login")
        self.user = QtWidgets.QLabel(self.centralwidget)
        self.user.setMaximumSize(QtCore.QSize(14, 14))
        self.user.setText("")
        self.user.setPixmap(QtGui.QPixmap("C:\\Users\\Admin\\Desktop\\Sidebar\\logo_view/user1.svg"))
        self.user.setScaledContents(True)
        self.user.setWordWrap(False)
        self.user.setObjectName("user")
        self.login.addWidget(self.user)
        self.loginEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.loginEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.loginEdit.setFont(font)
        self.loginEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(26, 46, 53);\n"
"border:none;")
        self.loginEdit.setInputMask("")
        self.loginEdit.setText("")
        self.loginEdit.setObjectName("loginEdit")
        self.login.addWidget(self.loginEdit)
        self.sign_in.addLayout(self.login)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.sign_in.addWidget(self.line)
        self.password = QtWidgets.QHBoxLayout()
        self.password.setObjectName("password")
        self.lock = QtWidgets.QLabel(self.centralwidget)
        self.lock.setMaximumSize(QtCore.QSize(14, 14))
        self.lock.setText("")
        self.lock.setPixmap(QtGui.QPixmap("C:\\Users\\Admin\\Desktop\\Sidebar\\logo_view/lock_black.svg"))
        self.lock.setScaledContents(True)
        self.lock.setObjectName("lock")
        self.password.addWidget(self.lock)
        self.passwordEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.passwordEdit.setFont(font)
        self.passwordEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(26, 46, 53);\n"
"border:none;")
        self.passwordEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.passwordEdit.setInputMask("")
        self.passwordEdit.setText("")
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.password.addWidget(self.passwordEdit)
        self.sign_in.addLayout(self.password)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.sign_in.addWidget(self.line_2)
        self.sing_in_welcome.addLayout(self.sign_in)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sing_in_welcome.addItem(spacerItem6)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(75, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 115, 92);\n"
"color: rgb(255, 255, 255);\n"
"border : none;\n"
"border-radius: 5px;")
        self.pushButton.setObjectName("pushButton")
        self.sing_in_welcome.addWidget(self.pushButton)
        self.central_sign_in.addLayout(self.sing_in_welcome)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.central_sign_in.addItem(spacerItem7)
        self.gridLayout.addLayout(self.central_sign_in, 0, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 0, 4, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.loginEdit.textEdited['QString'].connect(self.user.hide) # type: ignore
        self.loginEdit.editingFinished.connect(self.user.show) # type: ignore
        self.passwordEdit.textEdited['QString'].connect(self.lock.hide) # type: ignore
        self.passwordEdit.editingFinished.connect(self.lock.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HotelChain"))
        self.name.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:400; color:#ff735c;\">H</span><span style=\" font-size:16pt; font-weight:400; color:#1a2e35;\">otelChain</span></p></body></html>"))
        self.welcome.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#1a2e35;\">Добро пожаловать!</span></p></body></html>"))
        self.error_msg.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600; color:#ff735c;\">Неправильный логин <br/>или пароль</span></p></body></html>"))
        self.loginEdit.setPlaceholderText(_translate("MainWindow", "Логин"))
        self.passwordEdit.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.pushButton.setText(_translate("MainWindow", "Войти"))