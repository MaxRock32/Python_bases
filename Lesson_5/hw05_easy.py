# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys


def make_dir(dir):
    dir_path = os.path.join(os.getcwd(), '%s' % (dir))
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir))
    except FileExistsError:
        print('директория {} уже существует'.format(dir))


def remove_dir(dir):
    dir_path = os.path.join(os.getcwd(), '%s' % (dir))
    try:
        os.rmdir(dir_path)
        print('директория {} удалена'.format(dir))
    except FileExistsError:
        print('директория {} не существует'.format(dir))


do = {"mkdir": make_dir,
      'rmdir': remove_dir}
try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        for _ in range(1, 10):
            do[key]('dir_%s' % (_))
    else:
        print("Задан неверный ключ")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
#ТОЛЬКО ПАПКИ, А НЕ ФАЙЛЫ!

import os
import sys


def print_help():
    print("help - получение справки")
    print("folders <dir_name> - список папок в директории")


def subfolders():
    dir_path = os.path.join(dir)
    folders = [f.name for f in os.scandir(dir_path) if f.is_dir()]
    print(folders)


do = {'help': print_help,
      'folders': subfolders}
try:
    dir = sys.argv[2]
except IndexError:
    dir = os.getcwd()
try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key]()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# ИСПОЛЬЗОВАТЬ ТОЛЬКО МОДУЛЬ OS


import os
import shutil
def copy_scrypt():
	file_name=__file__.split('/')[-1:][0][0:len(__file__.split('/')[-1:][0])-3]
	newfile=file_name+'(copy).py'
	shutil.copy(__file__,newfile)
copy_scrypt()