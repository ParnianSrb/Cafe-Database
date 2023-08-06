from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_generator(object):
    def setupUi(self, generator):
        generator.setObjectName("generator")
        generator.resize(1197, 730)
        generator.setStyleSheet("background-color: black;\n"
"")
        self.centralwidget = QtWidgets.QWidget(generator)
        self.centralwidget.setObjectName("centralwidget")
        self.label_cold = QtWidgets.QLabel(self.centralwidget)
        self.label_cold.setGeometry(QtCore.QRect(740, 450, 291, 161))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(26)
        self.label_cold.setFont(font)
        self.label_cold.setStyleSheet("color: #288990;")
        self.label_cold.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cold.setObjectName("label_cold")
        self.label_warm = QtWidgets.QLabel(self.centralwidget)
        self.label_warm.setGeometry(QtCore.QRect(170, 50, 291, 161))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(26)
        self.label_warm.setFont(font)
        self.label_warm.setStyleSheet("color: #E9190C;")
        self.label_warm.setAlignment(QtCore.Qt.AlignCenter)
        self.label_warm.setObjectName("label_warm")
        self.listWidget_view_cold = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_view_cold.setGeometry(QtCore.QRect(630, 40, 511, 391))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.listWidget_view_cold.setFont(font)
        self.listWidget_view_cold.setStyleSheet("border: 2px solid #F8FFFE;\n"
"color: #F8FFFE;")
        self.listWidget_view_cold.setObjectName("listWidget_view_cold")
        self.listWidget_view_warm = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_view_warm.setGeometry(QtCore.QRect(60, 230, 511, 391))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.listWidget_view_warm.setFont(font)
        self.listWidget_view_warm.setStyleSheet("border: 2px solid #F8FFFE;\n"
"color: #F8FFFE;")
        self.listWidget_view_warm.setObjectName("listWidget_view_warm")
        generator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(generator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1197, 26))
        self.menubar.setObjectName("menubar")
        generator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(generator)
        self.statusbar.setObjectName("statusbar")
        generator.setStatusBar(self.statusbar)

        self.retranslateUi(generator)
        QtCore.QMetaObject.connectSlotsByName(generator)

    def retranslateUi(self, generator):
        _translate = QtCore.QCoreApplication.translate
        generator.setWindowTitle(_translate("generator", "Cafe Menu!"))
        self.label_cold.setText(_translate("generator", "Milkshakes\n"
"&\n"
"Mocktails"))
        self.label_warm.setText(_translate("generator", "Coffee Table\n"
"&\n"
"Herbal Beverages"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    generator = QtWidgets.QMainWindow()
    ui = Ui_generator()
    ui.setupUi(generator)
    generator.show()
    sys.exit(app.exec_())
