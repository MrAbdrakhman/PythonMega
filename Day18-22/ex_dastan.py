from bs4 import BeautifulSoup
import requests
import csv

CSV = 'sulpak_nout.csv'
URL = 'https://www.sulpak.kg/f/noutbuki'
HOST = 'https://www.sulpak.kg'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

def get_html(url, headers, **params):
    r = requests.get(url, headers=headers, params=params, verify=False)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('div', class_='goods-tiles')
    list_laptops = []
    for item in items:
        list_laptops.append({
            'Название ноута': item.find('h3', class_='title').get_text(
                strip=True),
            'Ссылка ноута': HOST + item.find('a').get('href'),
            'Цена ноута': item.find('div', class_='price').get_text(
                strip=True),
        })
    return list_laptops

def save(items, csv_):
    with open(csv_, 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название ноута', 'Ссылка ноута', 'Цена ноута'])
        for item in items:
            writer.writerow([item['Название ноута'], item['Ссылка ноута'], item['Цена ноута']])

def pagination():
    PAGENATION = int(input('Введите кол-во страниц: '))
    new_list = []
    for page in range(1, PAGENATION+1):
        print(f'Страница {page} готова')
        html = get_html(URL, HEADERS, params={'page' : page})
        new_list.extend(get_content(html.text))
    save(new_list, CSV)
    print('Готово')


if __name__ == '__main__':
    pagination()