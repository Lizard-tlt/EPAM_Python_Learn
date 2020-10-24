import sys
from PyQt5 import QtWidgets
import PyQt5.QtCore
import operator
from qtForm import CalcWindow


class MainApp(QtWidgets.QMainWindow, CalcWindow):
    def __init__(self):
        # Текущее состояние калькулятора
        self.READY = 0
        self.INPUT = 1

        super().__init__()

        self.stack = [0]
        self.state = self.READY
        self.last_operation = None
        self.current_op = None
        self.input_str = ""

        self.setupUi(self)

        for n in range(0, 10):
            getattr(self, 'btn_%s' % n).pressed.connect(lambda v=n: self.input_number(v))

        self.btn_clear.clicked.connect(self.reset)
        self.btn_add.pressed.connect(lambda: self.operation(operator.add))
        self.btn_div.pressed.connect(lambda: self.operation(operator.truediv))
        self.btn_multy.pressed.connect(lambda: self.operation(operator.mul))
        self.btn_power.pressed.connect(lambda: self.operation(operator.pow))
        self.btn_minus.pressed.connect(lambda: self.operation(operator.sub))
        self.btn_calc.pressed.connect(self.calculate)
        # self.btn_comma.pressed.connect(self.add_comma)

    def add_comma(self):
        if self.state == self.READY:
            self.state = self.INPUT
            self.input_str = str(self.input_str) + "0."
        else:
            if self.input_str.find(".") == -1:
                self.input_str = str(self.input_str) + "."

    def input_number(self, value):
        if self.state == self.READY:
            self.state = self.INPUT
            self.stack[-1] = value
        else:
            self.stack[-1] = self.stack[-1] * 10 + value

        self.display()

    def reset(self):
        self.state = self.READY
        self.stack = [0]
        self.last_operation = None
        self.current_op = None
        self.display()

    def operation(self, op):
        if self.current_op:
            self.calculate()

        self.stack.append(0)
        self.input_str = ""
        self.state = self.INPUT
        self.current_op = op

    def display(self):
        try:
            self.lcd.display(self.stack[-1])
        except Exception:
            self.lcd.display("OVER")

    def calculate(self):
        """Вычисление значения"""
        # Повторение последней операции. Добавление в стек для повторного вычисления
        if self.state == self.READY and self.last_operation:
            s, self.current_op = self.last_operation
            self.stack.append(s)

        if self.current_op:
            self.last_operation = self.stack[-1], self.current_op

            try:
                self.stack = [self.current_op(*self.stack)]
            except ZeroDivisionError:
                self.lcd.display("Fool")
                self.stack = [0]
            except Exception:
                self.lcd.display("ERROR")
                self.stack = [0]
            else:
                self.current_op = None
                self.state = self.READY
                self.display()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
