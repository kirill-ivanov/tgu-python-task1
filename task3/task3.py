# Разработайте программу для ведения списка задач (To-Do List), которые сохраняются в текстовый файл `tasks.txt`.


import logging

logging.basicConfig(
    filename='app3.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='UTF-8',
    level=logging.DEBUG
)

file = 'tasks.txt'
data = []


# читаем из файла данных
def init_from_file():
    data = []
    try:
        with open(file, 'r', encoding="utf-8") as f:
            for line in f:
                if line.strip() != '':
                    data.append(line.strip())
        return data
    except FileNotFoundError as e:
        logging.warning(f"Файл {file} не найден (ранее не было создано ни одного задания TODO)")
    except Exception as e:
        logging.error(f"При чтении файла {file} произошла ошибка: {e}")
        raise e


# сохраняем данные в файл
def save_file():
    try:
        with open(file, 'w', encoding="utf-8") as f:
            for item in data:
                f.write(f'{item}\n')
    except Exception as e:
        logging.error(f"При сохранении в файл произошла ошибка: {e}")
        raise e


# Добавить задание
def add_item(data, item):
    data.append(newItem)
    save_file()
    logging.info(f'Добавление задания. Задание {item} добавлено')


# удаление задания
def remove_item(data, item):
    if item in data:
        data.remove(item)
        save_file()
        logging.info(f'Удаление задания. Задание {item} удалено')
    else:
        print('Задание не было найдено')
        logging.warning(f'Удаление задания. Задание {item} не найдено')


# Вывести список задач
def print_data(data):
    if len(data) > 0:
        for (i, item) in enumerate(data, start=1):
            print(f'{i}. {item}', end='\n')
    else:
        print('Список заданий пуст')


###################################################
try:
    data = init_from_file()
except Exception as e:
    # Если по какой-то причине не считали из файла, инициализируем как новый список
    data = []

while True:
    action = input("\nВыберите операцию со списком (1-показать, 2-добавить, 3-удалить):")

    try:
        if action not in ['1', '2', '3']:
            raise ValueError(f'Выбрана неверная операция: {action}')

        match action:
            case '1':
                print_data(data)
            case '2':
                newItem = input("Введите новое задание:")
                add_item(data, newItem.strip())
            case '3':
                delItem = input("Введите задание на удаление:")
                remove_item(data, delItem.strip())
            case _:
                raise ValueError(f'Выбрана неверная операция: {action}')
    except ValueError as e:
        print(f'{e}')
        logging.error(f'{e}')
    except Exception as e:
        print(f'Ошибка! При выполнении задания произошла ошибка: {e}')
        logging.error(f'{e}')
