from PyQt5 import QtCore, QtGui, QtWidgets
import math
import form2
from PyQt5.QtWidgets import QMessageBox
import re

# pyuic5 form_bonds2.ui -o form2.py    команда для создания .py файла из QTDesigner

# из .py в .exe
# зайти в папку с кодом. Открыть cmd из этой папки и написать pyinstaller --onefile file.py (имя файла.py)
# создаст папку "dist" в ней будет exe-файл


class Ui_Dialog(QtWidgets.QMainWindow, form2.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.calcucate)

    def calcucate(self):
        price = self.lineEdit.text()
        p_now = self.lineEdit_2.text()
        ticket = self.lineEdit_3.text()
        y = self.textEdit.toPlainText()
        m = self.textEdit_2.toPlainText()
        period = self.textEdit_3.toPlainText()
        nkd = self.lineEdit_4.text()

        try:
            price = float(re.sub(',', '.', price))
            p_now = float(re.sub(',', '.', p_now))
            ticket = float(re.sub(',', '.', ticket))
            if not y:
                y = 0
            else: y = int(y)
            if not m:
                m = 0
            else: m = int(m)
            period = int(period)
            nkd = float(re.sub(',', '.', nkd))

            close = y * 12 + m
            per_month = ((math.ceil(close / period)) * ticket + price - nkd - p_now) / close
            percent = per_month * 12 / 10
            a = float('{:.3f}'.format(percent))

            if a > 20:
                warn = QMessageBox()
                warn.setWindowTitle('Подозрительно выгодно')
                warn.setText('Слишком хороший процент по облигации!')
                warn.setIcon(QMessageBox.Information)
                warn.setDetailedText('Стоит проверить данные. Если все верно: либо '
                                        'задуматься об эмитенте, либо скорее покупать :)')
                a = str(a)
                self.lineEdit_6.setText(a)
                warn.exec_()
            else:
                a = str(a)
                self.lineEdit_6.setText(a)

        except:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Проверьте введенные данные')
            error.setIcon(QMessageBox.Warning)
            #error.setStandardButtons(QMessageBox.Close|QMessageBox.Ok)
            #error.setInformativeText("")
            error.setDetailedText('Некоторые значения не были введены или введены с ошибкой')
            error.exec_()


        # Простой вывод окна ошибки
        # except:
        #     QMessageBox.critical(self, "Ошибка ", "Выделите элемент который хотите изменить", QMessageBox.Cancel)

app = QtWidgets.QApplication([])
window = Ui_Dialog()
window.show()
app.exec()
