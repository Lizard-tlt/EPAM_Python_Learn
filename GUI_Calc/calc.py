"""
Необходимо сделать простой калькулятор, поддерживающий операции (*+-/^)на двух числах
"""

import tkinter as tk
from tkinter import ttk


class CalcCombobox(ttk.Combobox):
    """Класс для работы с значением и функцией калькулятора"""
    def __init__(self, master, cnf={}, **options):

        self.dict = None

        if 'values' in options:
            if isinstance(options.get('values'), dict):
                self.dict = options.get('values')
                options['values'] = sorted(self.dict.keys())

        super(CalcCombobox, self).__init__(master, **options)

        self.bind('<<ComboboxSelected>>', self.on_select)

    def on_select(self, event):
        return self.get_value()

    def get(self):
        """Получение ключа значения из словаря"""
        if self.dict:
            return self.dict[ttk.Combobox.get(self)]

    def get_key(self):
        """Получение значения из словаря"""
        return ttk.Combobox.get(self)


class FloatEntry(tk.Entry):
    """Класс для задания операндов операции в калькуляторе"""
    def __init__(self, master=None, cnf={}, **kw):
        super(FloatEntry, self).__init__(master, cnf, **kw)
        self['validatecommand'] = (self.register(self.test_val), '%P', '%d')

    def test_val(self, in_str, act_typ):
        """Валидация"""
        if act_typ == '1':
            try:
                float(in_str)
            except ValueError:
                return False
            else:
                return True

    def get_float(self):
        value = self.get()
        return float(value if value != "" else 0)


class CalcForm:
    """Класс формы калькулятора"""
    def __init__(self):
        operations = {"+": lambda a, b: a + b,
                      "-": lambda a, b: a - b,
                      "*": lambda a, b: a * b,
                      "/": lambda a, b: a / b,
                      "^": lambda a, b: a ** b}

        root = tk.Tk()
        root.resizable(False, False)
        root.title("Python GUI Калькулятор")

        root.geometry("+{}+{}".format(int(root.winfo_screenwidth() / 2 - root.winfo_reqwidth() / 2),
                                      int(root.winfo_screenheight() / 2 - root.winfo_reqheight() / 2)))

        tk.Label(root, text="Первое число:").grid(row=0, column=0)
        tk.Label(root, text="Второе число:").grid(row=0, column=2)
        tk.Label(root, text="Выберите операцию:").grid(row=0, column=1)

        self.cb = CalcCombobox(root, state='readonly', values=operations)
        self.cb.grid(row=1, column=1)
        self.cb.set(list(operations.keys())[0])
        self.cb.bind('<<ComboboxSelected>>', self.on_select)

        self.entry_a = FloatEntry(root, validate="key")
        self.entry_a.grid(row=1, column=0)

        self.entry_b = FloatEntry(root, validate="key")
        self.entry_b.grid(row=1, column=2)

        self.result_label = tk.Label(root, text="Результат :")
        self.result_label.grid(row=3, column=1)

        btn_calc = tk.Button(root, text="Calc", width=30)
        btn_calc.config(command=self.change)
        btn_calc.grid(row=4, column=1)

        root.mainloop()

    def on_select(self, event):
        self.change()

    def change(self):
        try:
            result = self.cb.get()(self.entry_a.get_float(), self.entry_b.get_float())
        except ZeroDivisionError :
            self.result_label["text"] = "Fool"
        except Exception as e:
            self.result_label["text"] = f"Результат : {e}"
        else:
            self.result_label["text"] = f"Результат : {result}"


if __name__ == "__main__":
    CalcForm()
