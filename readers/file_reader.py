"""Чтение файлов"""


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
    return lines