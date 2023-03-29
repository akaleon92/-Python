#
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль


def my_func (x, y):
    try:
        z = x / y
        print("резултьтат деления:")
        return z
    except ZeroDivisionError:
        return "делить на 0 незаконно"
    except ValueError:
        return "требуется ввести число"
print(my_func(int(input("x = ")), int(input("y = "))))
