# Дан текстовый файл `students.txt`, содержащий информацию о студентах и их оценках по разным предметам.
# Каждая строка файла содержит имя студента и его оценки, разделенные запятыми.
# Пример строки: Иван Иванов,5,4,3,5 Мария Петрова,4,4,5,5


import logging

logging.basicConfig(
    filename='app2.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='UTF-8',
    level=logging.DEBUG
)

MARK_LEVEL_NORM = 4.1  # Выше этой оценки - "хорошие студенты"
file_path_read = 'students.txt'
file_path_write = 'top_students.txt'


# читаем из файла данные
def load_file(file):
    calc_average_mark = lambda arr: sum(arr) / len(arr)
    data = []

    try:
        with open(file, 'r', encoding="utf-8") as f:
            for line in f:
                tmp_arr = line.rstrip().split(',')

                name = tmp_arr[0]
                marks = list(map(int, tmp_arr[1:]))

                data.append({'student': name, 'averageMark': calc_average_mark(marks)})
            logging.info(f'Файл {file_path_read} прочитан')

            return data
    except FileNotFoundError as e:
        logging.error(f"Файл {file_path_read} не найден:")
        raise e
    except Exception as e:
        logging.error(f"При чтении файла {file_path_read} произошла ошибка: {e}")
        raise e


# Получить список студентов со средней оценкой выше заданной
def get_top_student(data, mark_compare):
    return list(filter(lambda item: item['averageMark'] >= mark_compare, data))


# Сохранить массив студентов в файл
def save_student(data, file):
    with open(file, 'w', encoding="utf-8") as f:
        for item in data:
            f.write(f"{item['student']}\t{item['averageMark']}\n")


# Вывести список студентов на печать
def print_student(data):
    for item in data:
        print(f"{item['student']}\t{item['averageMark']}")


try:
    data = load_file(file_path_read)
    top_students = get_top_student(data, MARK_LEVEL_NORM)
    save_student(top_students, file_path_write)
    print_student(top_students)

    logging.info(f"Файл обработан успешно. Количество студентов: {len(data)}")
except Exception as e:
    print(f'Ошибка! При выполнении задания произошла ошибка!')
