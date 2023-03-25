# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
seasons_list = ['этот месяц относится к зиме', 'этот месяц относится к весне', 'этот месяц относится к лету', 'этот месяц относится к осени']
seasons_dict = {1 : 'этот месяц относится к зиме', 2 : 'этот месяц относится к весне', 3 : 'этот месяц относится к лету', 4 : 'этот месяц относится к осени'}
month = int(input("Введите номер месяца: "))
if month ==1 or month == 12 or month == 2:
        print(f" Решение через dict: {seasons_dict.get(1)}")
        print(f" Решение через list: {seasons_list[0]}")
elif month == 3 or month == 4 or month ==5:
    print(f" Решение через dict: {seasons_dict.get(2)}")
    print(f" Решение через list: {seasons_list[1]}")
elif month == 6 or month == 7 or month == 8:
    print(f" Решение через dict: {seasons_dict.get(3)}")
    print(f" Решение через list: {seasons_list[2]}")

elif month == 9 or month == 10 or month == 11:
    print(f" Решение через dict: {seasons_dict.get(4)}")
    print(f" Решение через list: {seasons_list[3]}")
else:
        print("Такого месяца не существует")
