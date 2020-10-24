# Задание 9.1 - Context Manager
# Реализовать контекстный менеджер, выводящий в файл (указанный при конструировании менеджера)
# информацию по возникшей ошибке (в коде, обернутом контекстным менеджером),
# дате, времени выполнения кода. Выше ошибка прокидывается (происходит reraise)
from datetime import datetime


class my_context_manager:
    def __init__(self, log_file_name):
        self.file_name = log_file_name

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.file_name, 'a') as f:
            f.write(f'{datetime.now()} exception text: {exc_val} \n')
        # return True


with my_context_manager('log.txt'):
    raise ValueError("Приплыли...")
    # 1 / 0

