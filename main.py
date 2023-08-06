from PyQt5 import QtCore, QtGui, QtWidgets
from warm_drinks import Ui_warm_drinks
from cool_drinks import Ui_cool_drinks
from generate_menu import Ui_generator
import database_config
import mysql.connector


class Ui_main(object):
    def open_window_generate_menu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_generator()
        self.ui.setupUi(self.window)
        self.window.show()

        connection = mysql.connector.connect(**database_config.config)
        c = connection.cursor()
        c.execute('SELECT category, type, topping, price FROM cool_drinks')
        rows = c.fetchall()
        # print(rows)

        for row in rows:
            string = ' '
            for i in range(0, len(row)):
                string = string + str(row[i]) + '       '
            self.ui.listWidget_view_cold.addItem(string)

        c.execute('SELECT category, name, size, price FROM warm_drinks')
        rows = c.fetchall()
        print(rows)

        for row in rows:
            string = ' '
            for i in range(0, len(row)):
                string = string + str(row[i]) + '       '
            self.ui.listWidget_view_warm.addItem(string)

        connection.commit()
        connection.close()

    def open_window_warm_drinks(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_warm_drinks()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_window_cool_drinks(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_cool_drinks()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(1197, 730)
        main.setAutoFillBackground(False)
        main.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.label_cafe_menu = QtWidgets.QLabel(self.centralwidget)
        self.label_cafe_menu.setGeometry(QtCore.QRect(180, 50, 851, 91))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_cafe_menu.setFont(font)
        self.label_cafe_menu.setStyleSheet("color: #FF9904;")
        self.label_cafe_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_cafe_menu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cafe_menu.setObjectName("label_cafe_menu")
        self.label_category = QtWidgets.QLabel(self.centralwidget)
        self.label_category.setGeometry(QtCore.QRect(460, 230, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_category.setFont(font)
        self.label_category.setStyleSheet("color: #F8FFFE;")
        self.label_category.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_category.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_category.setLineWidth(1)
        self.label_category.setAlignment(QtCore.Qt.AlignCenter)
        self.label_category.setObjectName("label_category")
        self.button_warm_drinks = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.open_window_warm_drinks())
        self.button_warm_drinks.setGeometry(QtCore.QRect(400, 340, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(20)
        self.button_warm_drinks.setFont(font)
        self.button_warm_drinks.setStyleSheet("color: #F8FFFE;\n"
"border: 2px solid #F8FFFE;")
        self.button_warm_drinks.setObjectName("button_warm_drinks")
        self.button_cool_drinks = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.open_window_cool_drinks())
        self.button_cool_drinks.setGeometry(QtCore.QRect(640, 340, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(20)
        self.button_cool_drinks.setFont(font)
        self.button_cool_drinks.setStyleSheet("color: #F8FFFE;\n"
"border: 2px solid #F8FFFE;")
        self.button_cool_drinks.setObjectName("button_cool_drinks")
        self.label_generate = QtWidgets.QLabel(self.centralwidget)
        self.label_generate.setGeometry(QtCore.QRect(280, 520, 661, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(18)
        self.label_generate.setFont(font)
        self.label_generate.setStyleSheet("color: #E9190C;")
        self.label_generate.setAlignment(QtCore.Qt.AlignCenter)
        self.label_generate.setObjectName("label_generate")
        self.button_generate = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.open_window_generate_menu())
        self.button_generate.setGeometry(QtCore.QRect(540, 570, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_generate.setFont(font)
        self.button_generate.setStyleSheet("color: #E9190C;")
        self.button_generate.setObjectName("button_generate")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1197, 26))
        self.menubar.setObjectName("menubar")
        main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Cafe Menu Generator"))
        self.label_cafe_menu.setText(_translate("main", "Get Ready To Create Your Desired Cafe Menu!"))
        self.label_category.setText(_translate("main", "Choose the Category"))
        self.button_warm_drinks.setText(_translate("main", "Warm Drinks"))
        self.button_cool_drinks.setText(_translate("main", "Cool Ones!"))
        self.label_generate.setText(_translate("main", "After Creating All Tables, You Can Generate Your Cafe Menu Here... "))
        self.button_generate.setText(_translate("main", "Generate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
