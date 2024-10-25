# Создайте программу, которая читает файл `synonyms.txt`, содержащий слова и их синонимы в формате: слово - синоним1, синоним2, синоним3.
# Позвольте пользователю вводить слово и получать список его синонимов.


import logging

logging.basicConfig(
    filename='app5.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='UTF-8',
    level=logging.DEBUG
)

file_path_read = 'synonyms.txt'
data = {}


# читаем из файла данные
def load_file(file):
    try:
        with open(file, 'r', encoding="utf-8") as f:
            for line in f:
                tmp_arr = line.rstrip().split('-')
                word = tmp_arr[0].strip()
                synonyms = tmp_arr[1].rstrip().split(',')

                data[word] = synonyms
                logging.info(f'Файл {file_path_read} прочитан')
    except FileNotFoundError as e:
        logging.error(f"Файл {file_path_read} не найден:")
        raise e
    except Exception as e:
        logging.error(f"При чтении файла {file_path_read} произошла ошибка: {e}")
        raise e


# Поиск
def get_synonyms(word):
    result = data.get(word)
    logging.info(f"Поиск синонимов к слову '{word}': {result}")
    return result


# Вывод сотрудников на печать
def print_result(word, result_arr):
    print(f"\"{word}\"")
    print('Синонимы', end=' ')
    for (i, syn) in enumerate(result_arr, start=1):
        print(f'{i}.{syn}', end=' ')
    print('\n')

try:
    load_file(file_path_read)

    while True:
        word = input('Введите слово для поиска синонима:')
        word = word.strip().lower()

        result = get_synonyms(word)
        if result:
            print_result(word, result)
        else:
            print('Синоним не найден')
except Exception as e:
    print(f'Ошибка! При выполнении задания произошла ошибка!')
    raise e
