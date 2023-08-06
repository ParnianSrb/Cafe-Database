from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql import connector
from mysql.connector import errorcode
import database_config


class Ui_warm_drinks(object):
    def delete(self):
        # get the current row index and take it from list-widget
        clicked = self.listWidget_view.currentRow()

        # get the id of this row to delete from database
        clicked_id = self.listWidget_view.currentItem().text()[0]

        self.listWidget_view.takeItem(clicked)

        connection = mysql.connector.connect(**database_config.config)
        c = connection.cursor()
        c.execute('DELETE FROM warm_drinks WHERE id = ' + clicked_id)

        connection.commit()
        connection.close()

    def view(self):
        self.listWidget_view.clear()

        connection = mysql.connector.connect(**database_config.config)
        c = connection.cursor()
        c.execute('SELECT id, category, name, size, price FROM warm_drinks')
        rows = c.fetchall()
        # print(rows)

        for row in rows:
            string = f'{row[0]} :  '
            for i in range(1, len(row)):
                string = string + str(row[i]) + '       '
            self.listWidget_view.addItem(string)

        connection.commit()
        connection.close()

    def submit(self):
        self.category = self.lineEdit_category.text()
        self.name = self.lineEdit_name.text()
        self.size = self.lineEdit_size.text()
        self.price = self.lineEdit_price.text()
        try:
            connection = mysql.connector.connect(**database_config.config)
            c = connection.cursor()
            c.execute('CREATE DATABASE IF NOT EXISTS cafe_menu')

            c.execute("""CREATE TABLE IF NOT EXISTS warm_drinks (
                category VARCHAR(50),
                name VARCHAR(50),
                size VARCHAR(10),
                price SMALLINT,
                id int NOT NULL AUTO_INCREMENT PRIMARY KEY
                )""")

            c.execute('INSERT INTO warm_drinks (category, name, size, price) VALUES (%s, %s, %s, %s)',
                      (self.category, self.name, self.size, self.price))
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
        self.lineEdit_name.clear()
        self.lineEdit_size.clear()
        self.lineEdit_price.clear()

    def setupUi(self, warm_drinks):
        warm_drinks.setObjectName("warm_drinks")
        warm_drinks.resize(1197, 730)
        warm_drinks.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(warm_drinks)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(30, 60, 291, 161))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(26)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: #E9190C;")
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
        self.label_category.setStyleSheet("color: #288990;")
        self.label_category.setAlignment(QtCore.Qt.AlignCenter)
        self.label_category.setObjectName("label_category")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(570, 60, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(18)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("color: #288990;")
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.label_size = QtWidgets.QLabel(self.centralwidget)
        self.label_size.setGeometry(QtCore.QRect(780, 60, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(18)
        self.label_size.setFont(font)
        self.label_size.setStyleSheet("color: #288990;")
        self.label_size.setAlignment(QtCore.Qt.AlignCenter)
        self.label_size.setObjectName("label_size")
        self.label_price = QtWidgets.QLabel(self.centralwidget)
        self.label_price.setGeometry(QtCore.QRect(990, 60, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(18)
        self.label_price.setFont(font)
        self.label_price.setStyleSheet("color: #288990;")
        self.label_price.setAlignment(QtCore.Qt.AlignCenter)
        self.label_price.setObjectName("label_price")
        self.button_submit = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.submit())
        self.button_submit.setGeometry(QtCore.QRect(50, 330, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(16)
        self.button_submit.setFont(font)
        self.button_submit.setStyleSheet("color: #FF9904;\n"
"border: 2px solid #F8FFFE;\n"
"")
        self.button_submit.setObjectName("button_submit")
        self.button_view = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.view())
        self.button_view.setGeometry(QtCore.QRect(50, 420, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(16)
        self.button_view.setFont(font)
        self.button_view.setStyleSheet("color: #FF9904;\n"
"border: 2px solid #F8FFFE;")
        self.button_view.setObjectName("button_view")
        self.button_delete = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.delete())
        self.button_delete.setGeometry(QtCore.QRect(640, 580, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(16)
        self.button_delete.setFont(font)
        self.button_delete.setStyleSheet("color: #E9190C;\n"
"border: 2px solid #F8FFFE;")
        self.button_delete.setObjectName("button_delete")
        self.lineEdit_category = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_category.setGeometry(QtCore.QRect(350, 150, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.lineEdit_category.setFont(font)
        self.lineEdit_category.setStyleSheet("border: 2px solid #F8FFFE;\n"
"color: #F6D59F;")
        self.lineEdit_category.setText("")
        self.lineEdit_category.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_category.setObjectName("lineEdit_category")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(570, 150, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("border: 2px solid #F8FFFE;\n"
"color: #F6D59F;")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_size = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_size.setGeometry(QtCore.QRect(780, 150, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.lineEdit_size.setFont(font)
        self.lineEdit_size.setStyleSheet("border: 2px solid #F8FFFE;\n"
"color: #F6D59F;")
        self.lineEdit_size.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_size.setObjectName("lineEdit_size")
        self.lineEdit_price = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_price.setGeometry(QtCore.QRect(990, 150, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.lineEdit_price.setFont(font)
        self.lineEdit_price.setStyleSheet("border: 2px solid #F8FFFE;\n"
"color: #F6D59F;")
        self.lineEdit_price.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.listWidget_view = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_view.setGeometry(QtCore.QRect(350, 250, 821, 291))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.listWidget_view.setFont(font)
        self.listWidget_view.setStyleSheet("border: 2px solid #F8FFFE;\n"
"color: #F6D59F;")
        self.listWidget_view.setItemAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_view.setObjectName("listWidget_view")
        warm_drinks.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(warm_drinks)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1197, 26))
        self.menubar.setObjectName("menubar")
        warm_drinks.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(warm_drinks)
        self.statusbar.setObjectName("statusbar")
        warm_drinks.setStatusBar(self.statusbar)

        self.retranslateUi(warm_drinks)
        QtCore.QMetaObject.connectSlotsByName(warm_drinks)

    def retranslateUi(self, warm_drinks):
        _translate = QtCore.QCoreApplication.translate
        warm_drinks.setWindowTitle(_translate("warm_drinks", "Warm Drinks"))
        self.label_title.setText(_translate("warm_drinks", "Coffee Table\n"
"&\n"
"Herbal Beverages"))
        self.label_category.setText(_translate("warm_drinks", "Category\n"
"Coffee/Herbal"))
        self.label_name.setText(_translate("warm_drinks", "Name"))
        self.label_size.setText(_translate("warm_drinks", "Size\n"
"S/M/L"))
        self.label_price.setText(_translate("warm_drinks", "Price"))
        self.button_submit.setText(_translate("warm_drinks", "Submit"))
        self.button_view.setText(_translate("warm_drinks", "View"))
        self.button_delete.setText(_translate("warm_drinks", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    warm_drinks = QtWidgets.QMainWindow()
    ui = Ui_warm_drinks()
    ui.setupUi(warm_drinks)
    warm_drinks.show()
    sys.exit(app.exec_())
