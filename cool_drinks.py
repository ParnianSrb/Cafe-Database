from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql import connector
from mysql.connector import errorcode
import database_config


class Ui_cool_drinks(object):
    def delete(self):
        # get the current row index and take it from list-widget
        clicked = self.listWidget_view.currentRow()

        # get the id of this row to delete from database
        clicked_id = self.listWidget_view.currentItem().text()[0]

        self.listWidget_view.takeItem(clicked)

        connection = mysql.connector.connect(**database_config.config)
        c = connection.cursor()
        c.execute('DELETE FROM cool_drinks WHERE id = ' + clicked_id)

        connection.commit()
        connection.close()

    def view(self):
        self.listWidget_view.clear()

        connection = mysql.connector.connect(**database_config.config)
        c = connection.cursor()
        c.execute('SELECT id, category, type, topping, price FROM cool_drinks')
        rows = c.fetchall()
        print(rows)

        for row in rows:
            string = f'{row[0]} :  '
            for i in range(1, len(row)):
                string = string + str(row[i]) + '       '
            self.listWidget_view.addItem(string)

        connection.commit()
        connection.close()

    def submit(self):
        self.category = self.lineEdit_category.text()
        self.type = self.lineEdit_type.text()
        self.topping = self.lineEdit_topping.text()
        self.price = self.lineEdit_price.text()
        try:
            connection = mysql.connector.connect(**database_config.config)
            c = connection.cursor()
            c.execute('CREATE DATABASE IF NOT EXISTS cafe_menu')

            c.execute("""CREATE TABLE IF NOT EXISTS cool_drinks (
                category VARCHAR(50),
                type VARCHAR(50),
                topping VARCHAR(50),
                price SMALLINT,
                id int NOT NULL AUTO_INCREMENT PRIMARY KEY
                )""")

            c.execute('INSERT INTO cool_drinks (category, type, topping, price) VALUES (%s, %s, %s, %s)',
                      (self.category, self.type, self.topping, self.price))
            connection.commit()

        except connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with Username or Password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            connection.close()

        self.lineEdit_category.clear()
        self.lineEdit_type.clear()
        self.lineEdit_topping.clear()
        self.lineEdit_price.clear()

    def setupUi(self, cool_drinks):
        cool_drinks.setObjectName("cool_drinks")
        cool_drinks.resize(1197, 730)
        cool_drinks.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(cool_drinks)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_category = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_category.setGeometry(QtCore.QRect(350, 150, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.lineEdit_category.setFont(font)
        self.lineEdit_category.setStyleSheet("border: 2px solid #F8FFFE;\n"
"color: #F8FFFE;")
        self.lineEdit_category.setText("")
        self.lineEdit_category.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_category.setObjectName("lineEdit_category")
        self.lineEdit_topping = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_topping.setGeometry(QtCore.QRect(780, 150, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.lineEdit_topping.setFont(font)
        self.lineEdit_topping.setStyleSheet("border: 2px solid #F8FFFE;\n"
"color: #F8FFFE;")
        self.lineEdit_topping.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_topping.setObjectName("lineEdit_topping")
        self.lineEdit_price = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_price.setGeometry(QtCore.QRect(990, 150, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.lineEdit_price.setFont(font)
        self.lineEdit_price.setStyleSheet("border: 2px solid #F8FFFE;\n"
"color: #F8FFFE;")
        self.lineEdit_price.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.label_type = QtWidgets.QLabel(self.centralwidget)
        self.label_type.setGeometry(QtCore.QRect(570, 60, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(18)
        self.label_type.setFont(font)
        self.label_type.setStyleSheet("color: #FF9904;")
        self.label_type.setAlignment(QtCore.Qt.AlignCenter)
        self.label_type.setObjectName("label_type")
        self.button_delete = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.delete())
        self.button_delete.setGeometry(QtCore.QRect(640, 580, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(16)
        self.button_delete.setFont(font)
        self.button_delete.setStyleSheet("color: #E9190C;\n"
"border: 2px solid #F8FFFE;")
        self.button_delete.setObjectName("button_delete")
        self.listWidget_view = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_view.setGeometry(QtCore.QRect(350, 250, 821, 291))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.listWidget_view.setFont(font)
        self.listWidget_view.setStyleSheet("border: 2px solid #F8FFFE;\n"
"color: #F8FFFE;")
        self.listWidget_view.setItemAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_view.setObjectName("listWidget_view")
        self.label_topping = QtWidgets.QLabel(self.centralwidget)
        self.label_topping.setGeometry(QtCore.QRect(780, 60, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(18)
        self.label_topping.setFont(font)
        self.label_topping.setStyleSheet("color: #FF9904;")
        self.label_topping.setAlignment(QtCore.Qt.AlignCenter)
        self.label_topping.setObjectName("label_topping")
        self.label_price = QtWidgets.QLabel(self.centralwidget)
        self.label_price.setGeometry(QtCore.QRect(990, 60, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(18)
        self.label_price.setFont(font)
        self.label_price.setStyleSheet("color: #FF9904;")
        self.label_price.setAlignment(QtCore.Qt.AlignCenter)
        self.label_price.setObjectName("label_price")
        self.lineEdit_type = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_type.setGeometry(QtCore.QRect(570, 150, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.lineEdit_type.setFont(font)
        self.lineEdit_type.setStyleSheet("border: 2px solid #F8FFFE;\n"
"color: #F8FFFE;")
        self.lineEdit_type.setText("")
        self.lineEdit_type.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_type.setObjectName("lineEdit_type")
        self.button_submit = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.submit())
        self.button_submit.setGeometry(QtCore.QRect(50, 330, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(16)
        self.button_submit.setFont(font)
        self.button_submit.setStyleSheet("color: #F6D59F;\n"
"border: 2px solid #F8FFFE;\n"
"")
        self.button_submit.setObjectName("button_submit")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(30, 60, 291, 161))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(26)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: #288990;")
        self.label_title.setObjectName("label_title")
        self.label_category = QtWidgets.QLabel(self.centralwidget)
        self.label_category.setGeometry(QtCore.QRect(350, 60, 181, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_category.sizePolicy().hasHeightForWidth())
        self.label_category.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(18)
        self.label_category.setFont(font)
        self.label_category.setStyleSheet("color: #FF9904;")
        self.label_category.setAlignment(QtCore.Qt.AlignCenter)
        self.label_category.setObjectName("label_category")
        self.button_view = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.view())
        self.button_view.setGeometry(QtCore.QRect(50, 420, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(16)
        self.button_view.setFont(font)
        self.button_view.setStyleSheet("color: #F6D59F;\n"
"border: 2px solid #F8FFFE;")
        self.button_view.setObjectName("button_view")
        cool_drinks.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cool_drinks)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1197, 26))
        self.menubar.setObjectName("menubar")
        cool_drinks.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(cool_drinks)
        self.statusbar.setObjectName("statusbar")
        cool_drinks.setStatusBar(self.statusbar)

        self.retranslateUi(cool_drinks)
        QtCore.QMetaObject.connectSlotsByName(cool_drinks)

    def retranslateUi(self, cool_drinks):
        _translate = QtCore.QCoreApplication.translate
        cool_drinks.setWindowTitle(_translate("cool_drinks", "Cool Drinks"))
        self.label_type.setText(_translate("cool_drinks", "Type"))
        self.button_delete.setText(_translate("cool_drinks", "Delete"))
        self.label_topping.setText(_translate("cool_drinks", "Topping"))
        self.label_price.setText(_translate("cool_drinks", "Price"))
        self.button_submit.setText(_translate("cool_drinks", "Submit"))
        self.label_title.setText(_translate("cool_drinks", "Milkshakes\n"
"&\n"
"Mocktails"))
        self.label_category.setText(_translate("cool_drinks", "Category\n"
"Milkshake/Mocktail"))
        self.button_view.setText(_translate("cool_drinks", "View"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cool_drinks = QtWidgets.QMainWindow()
    ui = Ui_cool_drinks()
    ui.setupUi(cool_drinks)
    cool_drinks.show()
    sys.exit(app.exec_())
