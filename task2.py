# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def my_func(name, surname, birth_year, city, email, phone):
    print(name, surname, birth_year, city, email, phone)

my_func(name= 'Сергей', surname='Орлов', birth_year=1992, city='Москва', email='python@gb.ru', phone='+71234567')
