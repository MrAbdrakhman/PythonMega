from bs4 import BeautifulSoup
import requests
import csv
list_laptop = []

def get_content(r):
    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.findAll('div', class_='goods-tiles')
    for item in items:
        list_laptop.append({
            'Название ноутбука': item.find(
                'div', class_='listbox_title oh').get_text(strip=True),
            'Описание ноутбука': item.find(
                'div', class_='product_text pull-left').get_text(strip=True),
            'Цена ноутбука': item.find(
                'div', class_='listbox_price text-center').get_text(strip=True),
        })

    return list_laptop
def save():
    with open('tv.csv', 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название ноутбука', 'Описание ноутбука', 'Цена ноутбука'])
        for item in list_laptop:
            writer.writerow([item['Название ноутбука'], item['Описание ноутбука'], item['Цена ноутбука']])


def pagenation():
    page = int(input('Сколько страниц спарсить: '))
    for i in range(2, page + 1):
        PAGENATOR = f'https://www.sulpak.kg/f/led_oled_televizoriy?page={i}'
        r = requests.get(PAGENATOR)
        get_content(r)
        print(f'Страница номер {i} готова')
        save()

if __name__ == '__main__':
    pagenation()