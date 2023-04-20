#  Написать функцию для перевода доллара в евро c округлением до 2х знаков после запятой,
#  если известно, что текущий курс составляет 1.17 долларов за один евро.

def dollars_to_euros(dollars):
    euros = dollars / 1.17
    return round(euros, 2)
print(dollars_to_euros(100))
