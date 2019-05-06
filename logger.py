# Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, 
# аргументы, с которыми вызвалась и возвращаемое значение.

from datetime import datetime
from inspect import signature


def logger(some_function):

    def log_function(*args, **kwargs):

        now = datetime.now()
        function_name = some_function.__name__

        sig = signature(some_function)
        ba = sig.bind(*args, **kwargs)
        args = ba.args
        kwargs = ba.kwargs

        function_return = some_function(*args, **kwargs)

        f = open('out.txt', 'w')
        f.write(str(now) + '\t' + str(function_name) + '\t' + 
                str(args) + str(kwargs) + '\t' + 
                str(function_return) + '\t' + '\n')
        f.close()
        return

    return log_function


@logger
def say_something(*args, **kwargs):
    return 'func_result'
    

say_something('Hello!', 'Bay', name='John')
