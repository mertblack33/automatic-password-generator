from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import random

baglanti = sqlite3.connect("./sifre.db")
islem = baglanti.cursor()
islem.execute("CREATE TABLE IF NOT EXISTS kayit (kayit TEXT)")
baglanti.commit()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(197, 449)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 191, 441))
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        sorgu = "select * from kayit"
        for eb, r in enumerate(islem.execute(sorgu)):
            for d, i in enumerate(r):
                self.tableWidget.setItem(eb, d, QtWidgets.QTableWidgetItem(i))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Şifreler"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(pencere)
    pencere.show()
    sys.exit(app.exec_())