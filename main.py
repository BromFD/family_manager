from days_subtruction import subtract_days
from binary_search import binary_search
from shell_sort import shell_sort
from convert_to_values import *

path = str(input("Дорогой пользователь, пожалуйста, укажите полный путь к вашей таблице формата .csv:\n"))
if not path.endswith(".csv"):
    raise ValueError("Программа работает только с файлами с разрешением .csv")
option = int(input("Пожалуйста, укажите какой опцией программы семейный менеджер вы хотели бы воспользоваться?"
                   "\n1) Вывод списка задач выданных за прошедшие N-дней"
                   "\n2) Вывод всех задач члена семьи имеющих статус 'провалено'"
                   "\n3) Вывод списка всех задач, находящихся на исполнении\n"))

#Конвертация csv таблицы в список словарей задач
try:
    raw_file = open(path, 'r').read().split('\n')
except:
    raise FileNotFoundError("Укажите правильный путь к файлу")

file = [task.split(',') for task in raw_file]
task_data = []
task_amount = len(file) - 1
headers_amount = len(file[0])
headers = file.pop(0)
task_template = {}

for header in headers:
    task_template[header] = None

try:
    for task in range(task_amount):
        task_info = task_template.copy()
        for header in range(headers_amount):
            task_info[headers[header]] = file[task][header]
        task_data.append(task_info)
except:
    raise ValueError("Ошибка в составлении таблицы (количество заголовков не соответствует количеству значений)")

if option == 1:
    #Тип отчёта 1
    current_date = str(input("Введите текущую дату (формат ввода YYYY-MM-DD): "))
    N = int(input("Введите количество прошедших дней: "))
    if N > 0:
        N_date = subtract_days(current_date, N)
        current_date_value = convert_date_to_value(current_date) + 2400 # 2400 это максимальное значение часов и минут, добавлено для того, чтобы вывод был с текущим днём включительно.
        N_date_value = convert_date_to_value(N_date)
        datetime_values = [convert_datetime_to_value(task["Дата_и_время_начала"]) for task in task_data]
        status_values = [convert_status_to_value(task["Статус"]) for task in task_data]
        sorted_task_data = shell_sort(task_data, datetime_values, status_values)
        high_slice = binary_search(datetime_values, current_date_value, 'last')
        low_slice = binary_search(datetime_values, N_date_value, 'first')
        cut_sorted_task_data = sorted_task_data[low_slice:high_slice][::-1] # Сортировка идёт по возрастанию, поэтому список инвертируется, списки будут инвертироваться по этой же причине

        for task in range(high_slice - low_slice):
            print(cut_sorted_task_data[task])
    else:
        raise ValueError("Введено не натуральное значение N")

elif option == 2:
    name = str(input("Введите члена семьи: "))
    failed_tasks = [task for task in task_data if task["Статус"] == 'провалена' and task["Исполнитель"] == name]
    datetime_values = [convert_datetime_to_value(task["Дата_и_время_окончания"]) for task in failed_tasks]
    description_values = [convert_sentence_to_value(task["Описание"], True) for task in failed_tasks]
    sorted_failed_tasks = shell_sort(failed_tasks, datetime_values, description_values)[::-1]

    for task in sorted_failed_tasks:
        print(task)

elif option == 3:
    processing_tasks = [task for task in task_data if task["Статус"] == 'в процессе' or task["Статус"] == 'получена']
    datetime_values = [convert_datetime_to_value(task["Дата_и_время_окончания"]) for task in processing_tasks]
    name_values = [convert_sentence_to_value(task["Исполнитель"]) for task in processing_tasks]
    sorted_processing_tasks = shell_sort(processing_tasks, name_values, datetime_values)

    for task in sorted_processing_tasks:
        print(task)

else:
    raise ValueError("Выбрана несуществующая опция")

