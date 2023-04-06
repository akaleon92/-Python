# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

my_file = open('task2.txt', 'r')
content = my_file.read()
print(f'Текст файла: \n {content}')
my_file = open('task2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в тексте: {len(content)}')
my_file = open('task2.txt', 'r')
content = my_file.readlines()
my_file = open('task2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Всего слов в тексте: {len(content)}')
my_file.close()
