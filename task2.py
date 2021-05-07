def decorator(function_to_decorate):
    def wrapper(arg1, arg2):
        if arg2 == 0:
            return 'Ошибка'
        elif type(arg1) == int and type(arg2)==int:
            return f'Результат: {function_to_decorate(arg1, arg2)}'
        else:
            return 'Проверьте на правильность'
        return wrapper

@decorator
def divide(a, b):
    return a/b


print(divide(1, 2))