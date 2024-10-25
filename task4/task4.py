# У вас есть файл `employees.txt`, содержащий информацию о сотрудниках: имя, возраст, должность и зарплата, разделенные запятыми.
# Пример строки: Иван Иванов,30,Инженер,70000 Мария Петрова,28,Аналитик,80000
# Необходимо обработать эти данные и вывести список сотрудников, чья зарплата выше среднего.


import logging

logging.basicConfig(
    filename='app4.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='UTF-8',
    level=logging.DEBUG
)

AVERAGE_SALARY = 80_000  # Средняя зарплата
file_path_read = 'employees.txt'
file_path_write = 'high_earners.txt'


# читаем из файла данные
def load_file(file):
    data = []

    try:
        with open(file, 'r', encoding="utf-8") as f:
            for line in f:
                tmp_arr = line.rstrip().split(',')

                data.append({'employee': tmp_arr[0], 'age': int(tmp_arr[1]), 'position': tmp_arr[2],
                             'salary': float(tmp_arr[3])})
                logging.info(f'Файл {file_path_read} прочитан')

            return data
    except FileNotFoundError as e:
        logging.error(f"Файл {file_path_read} не найден:")
        raise e
    except Exception as e:
        logging.error(f"При чтении файла {file_path_read} произошла ошибка: {e}")
        raise e


# Фильтрация только сотрудников с зарплатой равно и выше средней
def filter_employees(data):
    return list(filter(lambda item: item['salary'] >= AVERAGE_SALARY, data))


# Расчет средней зарплаты
def calculate_average(data):
    return sum(item['salary'] for item in data) / len(data)


# Сохранение сотрудников в файл
def save_employees(data, file):
    with open(file, 'w', encoding="utf-8") as f:
        for item in data:
            f.write(f'{item["employee"]},{item["age"]},{item["position"]},{item["salary"]}\n')


# Вывод сотрудников на печать
def print_employee(data):
    for item in data:
        print(f"{item['employee']} - {item['position']} - {item['salary']}")


# сравнение зарплат с заданной зарплатой
def compare_salary(data, compare_salary):
    for item in data:
        if item['salary'] > compare_salary:
            print(f"{item['employee']} - {item['salary']} -> з/п ВЫШЕ")
        elif item['salary'] == compare_salary:
            print(f"{item['employee']} - {item['salary']} -> з/п РАВНА")
        else:
            print(f"{item['employee']} - {item['salary']} -> з/п НИЖЕ")


try:
    data = load_file(file_path_read)
    high_earners = filter_employees(data)

    save_employees(high_earners, file_path_write)
    print("=== ВЫСОКИЕ ЗАРПЛАТЫ ===")
    print_employee(high_earners)

    average_salary = calculate_average(data)
    print(f'\nСредняя зарплата: {average_salary}')
    print("=== Сравнение зарплат со средней ===")
    compare_salary(data, average_salary)

    logging.info(f"Файл обработан успешно. Количество сотрудников: {len(data)}, отфильтровано: {len(high_earners)}")
except Exception as e:
    print(f'Ошибка! При выполнении задания произошла ошибка!')