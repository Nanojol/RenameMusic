import os

path = r'C:\Users\NevO\Desktop\Музыка'
count = 2
for root, dirs, files in os.walk(path):
    for _file in files:
        # print(_file)
        os.rename(root + "\\" + _file, root + "\\" + str(count) + ". " + _file)
        # print(_file)
        count += 2

