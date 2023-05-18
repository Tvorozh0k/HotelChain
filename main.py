import sys

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QMainWindow, QApplication, QButtonGroup, QTableWidget, QTableWidgetItem
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5 import QtGui, QtCore, QtWidgets, QtTest, QtSql

import login_ui
import sidebar_ui

from employee import Employee
from room_description import RoomDescription

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = login_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        # click -> check user's login
        self.ui.pushButton.clicked.connect(self.check_login)

        # initially we hide error message
        self.ui.error_msg.hide()

        # go to main menu
        self.menu = None

        # accounts info
        self.accounts = dict()

        # query in order to get accounts info
        query = QSqlQuery()
        query.exec_("SELECT Login, Password FROM Account")

        while query.next():
            self.accounts[query.value(0)] = query.value(1)

    def check_login(self):

        login, password = self.ui.loginEdit.text(), self.ui.passwordEdit.text()

        if login not in self.accounts or password != self.accounts[login]:
            self.ui.error_msg.hide()
            QtTest.QTest.qWait(100)
            self.ui.error_msg.show()
        else:

            # get fio
            query = QSqlQuery()

            query.exec_(
                """
                SELECT Employee.ID_Employee, Last_Name, First_Name, 
                Patronymic, ID_Hotel FROM Account, Employee
                WHERE Account.ID_Employee = Employee.ID_Employee AND Login = \'%s\'
                """ % login
            )

            query.next()

            self.menu = MenuWindow(Employee(query.value(0), query.value(1), query.value(2),
                                            query.value(3), query.value(4), login, password))

            self.menu.show()
            self.hide()


class MenuWindow(QMainWindow):
    def __init__(self, employee):
        super().__init__()

        self.ui = sidebar_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        # main page
        self.ui.stackedWidget.setCurrentIndex(0)

        # set fio
        self.employee = employee
        self.ui.fio_label.setText(self.employee.get_fio())

        # connect buttons and activities
        self.ui.main_btn.clicked.connect(self.home_page)
        self.ui.booking_btn.clicked.connect(self.booking_page)
        self.ui.search_btn.clicked.connect(self.booking_page)
        self.ui.accommodation_btn.clicked.connect(self.living_page)
        self.ui.services_btn.clicked.connect(self.service_page)
        self.ui.money_btn.clicked.connect(self.money_page)
        self.ui.user_btn.clicked.connect(self.user_page)
        self.ui.tabWidget.currentChanged.connect(self.room_description_info)
        self.ui.room_description.currentIndexChanged.connect(self.get_room_info)

        # menu buttons
        self.left_buttons = QButtonGroup()
        self.left_buttons.addButton(self.ui.main_btn)
        self.left_buttons.addButton(self.ui.booking_btn)
        self.left_buttons.addButton(self.ui.accommodation_btn)
        self.left_buttons.addButton(self.ui.services_btn)
        self.left_buttons.addButton(self.ui.money_btn)

        # today date
        self.ui.booking_date.setDate(QDate.currentDate())
        self.ui.checkin_date.setDate(QDate.currentDate())
        self.ui.checkout_date.setDate(QDate.currentDate())

        self.room_descriptions = []
        self.view = None

    def home_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.user_btn.setChecked(False)

    def booking_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.user_btn.setChecked(False)
        fio_cond = self.ui.fio_editor.text()

        self.view = QTableWidget()
        self.view.setColumnCount(8)
        self.view.setHorizontalHeaderLabels(['ID', 'ФИО', 'Дата заезда', 'Дата выезда',
                                             'Тип номера', 'Вместимость', 'Балкон', 'Статус'])

        # all bookings
        query = QSqlQuery()
        query.exec_(
            """
            EXEC Booking_Info %d, \'%s\'
            SELECT * FROM ##BookingInfo
            GO
            """ % (self.employee.id_hotel, fio_cond)
        )

        while query.next():
            rows = self.view.rowCount()
            self.view.setRowCount(rows + 1)
            self.view.setItem(rows, 0, QTableWidgetItem(str(query.value(0))))
            self.view.setItem(rows, 1, QTableWidgetItem(query.value(1)))
            self.view.setItem(rows, 2, QTableWidgetItem(str(query.value(2))))
            self.view.setItem(rows, 3, QTableWidgetItem(str(query.value(3))))
            self.view.setItem(rows, 4, QTableWidgetItem(query.value(4)))
            self.view.setItem(rows, 5, QTableWidgetItem(str(query.value(5))))
            self.view.setItem(rows, 6, QTableWidgetItem(query.value(6)))
            self.view.setItem(rows, 7, QTableWidgetItem(query.value(7)))

        self.view.verticalHeader().setVisible(False)
        self.view.resizeColumnsToContents()
        self.ui.gridLayout_booking.addWidget(self.view, 0, 0)

    def room_description_info(self):
        if self.ui.tabWidget.currentIndex() == 1:

            # all room descriptions
            query = QSqlQuery()
            query.exec_(
                """
                EXEC Room_Description_Info 
                SELECT * FROM ##RoomDescriptionInfo
                GO
                """
            )

            while query.next():
                self.room_descriptions.append(RoomDescription(query.value(1), query.value(2), query.value(3),
                                                              query.value(4), query.value(5)))

                self.ui.room_description.addItem(query.value(0))

            self.get_room_info()

    def get_room_info(self):
        ind = self.ui.room_description.currentIndex()

        self.ui.room_type_editor.setText(self.room_descriptions[ind].room_type)
        self.ui.room_price_editor.setText(str(self.room_descriptions[ind].price))
        self.ui.room_capacity_editor.setText(str(self.room_descriptions[ind].capacity))
        self.ui.room_balcony_editor.setText(self.room_descriptions[ind].balcony)

    def living_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.user_btn.setChecked(False)

    def service_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.user_btn.setChecked(False)

    def money_page(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.user_btn.setChecked(False)

    def user_page(self):
        self.ui.stackedWidget.setCurrentIndex(5)

        self.left_buttons.setExclusive(False)

        self.ui.main_btn.setChecked(False)
        self.ui.booking_btn.setChecked(False)
        self.ui.accommodation_btn.setChecked(False)
        self.ui.services_btn.setChecked(False)
        self.ui.money_btn.setChecked(False)

        self.left_buttons.setExclusive(True)


# pyuic5.exe C:\Users\Admin\Desktop\Sidebar\sidebar.ui -o C:\Users\Admin\PycharmProjects\HotelChain\sidebar_ui.py


if __name__ == "__main__":
    # connect db
    db = QSqlDatabase.addDatabase('QODBC')

    db.setDatabaseName('DRIVER={SQL Server};SERVER=%s;DATABASE=%s;Trusted_Connection=yes'
                       % ('DESKTOP-Q79K1H4\\SQLEXPRESS',
                          'HotelChain'))
    db.open()

    # app
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('C:\\Users\\Admin\\Desktop\\Sidebar\\logo_view\\logo_icon.svg'))

    window = LoginWindow()
    window.show()

    sys.exit(app.exec())
