import re
import csv

# 1 задание

def find_words(filename='task1-ru.txt'):
    # Примем за слово комбинацию с двух и более букв подряд
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    words = text.lower().split()

    words_starting_with_s = [word for word in words if re.fullmatch(r'[с][а-я]+', word)]
    words_after_i = []

    for i in range(1, len(words)):
        if words[i - 1] == 'и' and re.fullmatch(r'[а-я]+', words[i]):  # Проверка на 2 и более букв подряд
            words_after_i.append(words[i])
    print('Задание №1:')
    print("Слова, начинающиеся с буквы 'с':", words_starting_with_s)
    print("Слова, перед которыми стоит 'и':", words_after_i)

find_words()


# 2 задание

def extract_font_names(filename='task2.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Регулярное выражение для поиска имен шрифтов.  Обрабатывает различные варианты:
    # font-family: 'Название шрифта', "Название шрифта", Название шрифта
    font_pattern = r"font-family\s*:\s*['\"]?([a-zA-Z0-9\s,-]+)['\"]?"

    font_names = re.findall(font_pattern, html_content, re.IGNORECASE)

    # Удаляем дубликаты и лишние пробелы
    unique_font_names = list(set([name.strip() for name in font_names]))
    return unique_font_names

font_names = extract_font_names()
if font_names:
    print('Задание №2:')
    print('Имена шрифтов:', font_names)


# 3 задание

def normalize_data(filename="task3.txt", output_filename="Normalized_table.csv"):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # Извлечение данных с помощью более robust регулярных выражений
    date_pattern = r'\d{4}-\d{2}-\d{2}'  # Общий вид для дат
    url_pattern = r'https?://\S+'  # Общий вид для URL
    surname_pattern = r'[A-Z][a-z]+(?:[\s-][A-Z][a-z]+)*'  # Общий вид для фамилий
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'  # Общий вид для почты

    dates = re.findall(date_pattern, text)
    urls = re.findall(url_pattern, text)
    surnames = re.findall(surname_pattern, text)
    emails = re.findall(email_pattern, text)

    # Проверка на корректное количество данных
    if len(dates) != len(urls) != len(surnames) != len(emails):
        print("Ошибка: количество данных в файле не соответствует ожидаемому.")
        return

    # Генерация ID (более надёжный способ)
    ids = [str(i + 1) for i in range(len(dates))]

    # Запись в CSV-файл
    with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Фамилия', 'Почта', 'URL', 'Дата регистрации'])
        for row in zip(ids, surnames, emails, urls, dates):
            writer.writerow(row)
    print('Задание №3:')
    print(f"Данные успешно сохранены в '{output_filename}'.")

normalize_data()


# Дополнительное задание:
print('Дополнительное задание:')

def extract_data(filename="task_add.txt"):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    date_pattern = r'\s(\d{4}[-\/\.]\d{1,2}[-\/\.]\d{1,2}|\d{1,2}[-\/\.]\d{1,2}[-\/\.]\d{4}|\d{1,2}[-\/\.]\d{4}[-\/\.]\d{1,2})'
    email_pattern = r'\s([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
    url_pattern = r'\s(https?://\S+)'

    dates = re.findall(date_pattern, text)
    emails = re.findall(email_pattern, text)
    urls = re.findall(url_pattern, text)

    print("Найденные даты:", dates)
    print("Найденные email-адреса:", emails)
    print("Найденные URL:", urls)

    return dates, emails, urls

extract_data()
