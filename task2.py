import requests
from bs4 import BeautifulSoup


def collect_data(url):
    names = []
    while True:
        html_page = requests.get(url).text
        bs = BeautifulSoup(html_page, 'lxml')
        animals = bs.find('div', class_='mw-category mw-category-columns').find_all('li')

        # заполняем список с названиями животных
        for animal in animals:
            names.append(animal.text)

        # вывод кол-ва записей, чтобы понимать что программа работает (НЕОБЯЗАТЕЛЬНО)
        print(f'Идет сбор информации. Количество записей: {len(names)}')

        # поиск ссылки на следующую страницу
        links = bs.find('div', id='mw-pages').find_all('a')
        for a in links:
            if a.text == 'Следующая страница':
                url = 'https://ru.wikipedia.org/' + a.get('href')
                break

        # если ссылка на следующую страницу не найдена можно прерывать цикл и начинать подсчет
        else:
            break

    # подсчет кол-ва животных на каждую букву алфавита
    # википедия в общем списке так же отдает названия животных на латыни, при желании можно и их сосчитать
    for i in range(ord('А'), ord('Я')):
        counter = 0
        for name in names:
            if name[0] == chr(i):
                counter += 1
        print(f'{chr(i)}: {counter}')


if __name__ == '__main__':
    collect_data('https://inlnk.ru/jElywR')
