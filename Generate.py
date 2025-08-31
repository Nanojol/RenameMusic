# Добавляет цифры в префикс
# import os
#
# path = r'C:\Users\NevO\Desktop\rename'
# count = 2
# for root, dirs, files in os.walk(path):
#     for _file in files:
#         os.rename(root + "\\" + _file, root + "\\" + str(count) + ". " + _file)
#         count += 2
# print("конец")


# Удаляет числа из префикса
# import os
# import re
#
# path = r'C:\Users\NevO\Desktop\Ренэйм'
# # Исходный путь к файлу
# for root, dirs, files in os.walk(path):
#     for _file in files:
#         old_path = root + "\\" + _file
#
#         # Получаем директорию и имя файла
#         directory, filename = os.path.split(old_path)
#
#         # Разделяем имя файла и расширение
#         name, ext = os.path.splitext(filename)
#
#         # Удаляем числовой префикс в начале имени файла
#         new_name = re.sub(r'^\d+\.\s*', '', name)
#
#         # Формируем новое имя файла
#         new_filename = new_name + ext
#
#         # Полный путь для нового файла
#         new_path = os.path.join(directory, new_filename)
#
#         # Переименование файла
#         os.rename(old_path, new_path)
# print("конец")

# Добавляет числа из списка в префикс файла

import os
import random

path = r'C:\Users\NevO\Desktop\rename'
# Количество элементов в папке
count = 297
count_list = [x for x in range(1, count+1, 1)]
# print(count_list)
random.shuffle(count_list)

# print(number)

for root, dirs, files in os.walk(path):
    for _file in files:
        number = count_list.pop(0)
        os.rename(root + "\\" + _file, root + "\\" + str(number) + ". " + _file)

print("конец")