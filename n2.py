import os

dir_name = "9_2"
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".jpg"):
        os.remove(os.path.join(dir_name, item)) #Удаляет все файлы с расширением .jpg