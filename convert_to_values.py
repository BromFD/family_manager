#Этот файл конвертирует значения таблицы в пригодные для сортировки
from value_validator import *


def convert_datetime_to_value(datetime):
    try:
        date, time = datetime.split(' ')
        year, month, day = date.split('-')
        hour, minute = time.split(':')
    except:
        raise ValueError("Неверный формат даты-времени")
    if validate_datetime(year, month, day, hour, minute):
        value = (int(year) * 10 ** 8) + (int(month) * 10 ** 6) + (int(day) * 10 ** 4) + (int(hour) * 10 ** 2) + int(minute)
        return value
    else:
        raise ValueError("Неверный формат даты-времени")


def convert_date_to_value(date):
    try:
        year, month, day = date.split('-')

    except:
        raise ValueError("Неверный формат даты")
    if validate_date(year, month, day):
        value = (int(year) * 10 ** 8) + (int(month) * 10 ** 6) + (int(day) * 10 ** 4)
        return value
    else:
        raise ValueError("Неверный формат даты")


def convert_status_to_value(status):
    match status:
        case "успешно выполнена":
            return 3
        case 'в процессе':
            return 2
        case 'получена':
            return 1
        case 'провалена':
            return 0
        case _:
            return ValueError("Неизвестный статус")


def convert_sentence_to_value(sentence, reverse=False):
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.lower()
    sentence = sentence.lower()
    if reverse:
        alphabet = alphabet[::-1]
    try:
        return alphabet.index(sentence[0])
    except:
        raise ValueError("Данного символа нет в русском алфавите")