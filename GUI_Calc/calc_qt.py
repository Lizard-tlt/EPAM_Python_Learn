import sys
from PyQt5 import QtWidgets
import qtForm


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        self.operations = {"+": lambda a, b: a + b,
                           "-": lambda a, b: a - b,
                           "*": lambda a, b: a * b,
                           "/": lambda a, b: a / b,
                           "^": lambda a, b: a ** b}

        super(MainApp, self).__init__()

        self.ui = qtForm.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_calc.clicked.connect(self.calc_pressed)

        for k in self.operations:
            self.ui.cbx_oper.addItem(k)

        self.ui.cbx_oper.currentIndexChanged.connect(self.cb_changed)

    def calc_pressed(self):
        func = self.operations.get(self.ui.cbx_oper.currentText())
        try:
            result = func(self.ui.lineEditA.value(), self.ui.lineEditB.value())
        except ZeroDivisionError:
            self.ui.label_result.setText("Fool")
        except Exception as e:
            self.ui.label_result.setText(e)
        else:
            self.ui.label_result.setText(f"Результат : {result}")


    def cb_changed(self, idx):
        self.calc_pressed()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
