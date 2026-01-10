#Этот файл конвертирует значения таблицы в пригодные для сортировки
def convert_datetime_to_value(datetime):
    date, time = datetime.split(' ')
    year, month, day = date.split('-')
    hour, minute = time.split(':')
    value = (int(year) * 10 ** 8) + (int(month) * 10 ** 6) + (int(day) * 10 ** 4) + (int(hour) * 10 ** 2) + int(minute)
    return value


def convert_date_to_value(date):
    year, month, day = date.split('-')
    value = (int(year) * 10 ** 8) + (int(month) * 10 ** 6) + (int(day) * 10 ** 4)
    return value


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
    return alphabet.index(sentence[0])