import os
import pathlib
from pathlib import Path
def file_operations():
    """
    operations on file
    :return:
    """
    try:
        # file = open('data.txt', 'r')
        # file = open('data.txt', 'w')
        file = open('data.txt', 'a')
        print('successfully opened file')
        print('file name :', file.name)
        print('file mode:', file.mode)
        print('file readable:', file.readable())
        # content = file.read()
        # for line in content:
        #     print(line, end='')
        #
        file.write("Akash More \n")

    except Exception as ex:
        raise ex
    finally:
        file.close()

# print(file_operations())


def write_line(file , mode, list_str):
    """
    to write list data line by line
    :param file:
    :param mode:
    :param list_str:
    :return:
    """
    try:
        file = open(file, mode)
        file.writelines(list_str)
    except Exception as ex:
        raise ex
    finally:
        file.close()

# data = ["shrikant\n", "Manoj\n", "Vinay\n"]
# write_line('data.txt', 'a', data)


def read_lines(filename):
    """
    read file line by line
    :param filename:
    :return:
    """
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        for line in lines:
            print(line, end='')
    except Exception as ex:
        raise ex
    finally:
        file.close()

# read_lines("data.txt")


def read_file(filename):
    """
    seek() and tell() functions
    :param filename:
    :return:
    """
    try:
        file = open(filename, 'r')
        print(file.readline())
        print(file.tell())
        file.seek(20)
        print(file.readline())
        print(file.tell())

    except FileNotFoundError as err:
        raise err
    finally:
        file.close()
        print("Completed")

# read_file("data.txt")


def file_exists(filename):
    try:
        print(os.path.exists(filename))
        print(os.path.isfile(filename))
        print(Path(filename).resolve())
    except Exception as ex:
        raise ex
    finally:
        print("Completed")

# file_exists('data.txt')


def line_word_char(filename):
    lcount = wcont = ccount = 0
    try:
        file = open(filename, 'r')
        for line in file:
            lcount += 1
            wcont += len(line.split())
            for char in line.split():
                ccount += len(char)
        print(lcount, wcont, ccount)

    except Exception as ex:
        raise ex
line_word_char('data.txt')