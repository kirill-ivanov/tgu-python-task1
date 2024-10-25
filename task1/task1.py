# Задание 1: Анализ данных из текстового файла
# Условие: У вас есть текстовый файл `data.txt`, содержащий информацию о продажах товаров.
# Каждая строка файла содержит три поля, разделенных запятыми: название товара, количество проданных единиц и цену за единицу.
# Пример строки: Товар1,10,99.99 Товар2,5,149.50

import logging

logging.basicConfig(
    filename='app1.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='UTF-8',
    level=logging.DEBUG
)

HIGH_LEVEL_RESULT = 1_000_000  # Выше этой суммы - высокие продажи
file_path = 'data.txt'


# читаем из файла данные
def load_file(file):
    data = []
    try:
        with open(file, 'r', encoding="utf-8") as f:
            for line in f:
                tmp_arr = line.split(',')
                data.append({'product': tmp_arr[0], 'count': int(tmp_arr[1]), 'price': float(tmp_arr[2])})
            logging.info(f'Файл {file_path} прочитан')

            return data
    except FileNotFoundError as e:
        logging.error(f"Файл {file_path} не найден:")
        raise e
    except Exception as e:
        logging.error(f"При чтении файла {file_path} произошла ошибка: {e}")
        raise e


# Подсчет итогов - возвращаем измененный массив с итогами + общий итог
def calc_result(data):
    total = 0

    for item in data:
        total += item['count'] * item['price']
        item['total'] = item['count'] * item['price']
    return data, total


# Вывод результата на экран
def print_result(data, total):
    for item in data:
        print(f'{item["product"]} \t {item["count"]} \t {item["price"]:.2f} \t {item["total"]:.2f}')
    print('==========================')
    print(f'TOTAL: {total:.2f}')

    if total > HIGH_LEVEL_RESULT:
        print(f'Ура! Достигнуты высокие продажи!')


try:
    data = load_file(file_path)
    calc_data, total = calc_result(data)
    print_result(calc_data, total)
except Exception as e:
    print(f'Ошибка! При выполнении задания произошла ошибка!')
