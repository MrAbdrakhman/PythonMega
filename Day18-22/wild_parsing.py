from bs4 import BeautifulSoup
import requests
import csv

CSV = 'wildpak_nout.csv'
URL = 'https://kg.wildberries.ru/catalog/elektronika/umnyy-dom?sort=popular&page=1&xsubject=6463'
# HOST = 'https://kg.wildberries.ru/'
# HEADERS = {
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
# }

def get_html(url, **params):
    r = requests.get(url, params=params, verify=True)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('div', class_='product-card__wrapper')
    wildpak_nout = []
    for item in items:
        try:
            wildpak_nout.append({
                'Название светильника': item.find('span', class_='goods-name').get_text(
                    strip=True),
                'Цена светильника': item.find('ins', class_='lower-price').get_text(
                    strip=True),
                    })
        except:
            wildpak_nout.append({
                'Название светильника': item.find('span', class_='goods-name').get_text(
                    strip=True),
                'Цена светильника': 'no lower price'})
    return wildpak_nout

def save(items, csv_):
    with open(csv_, 'w') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название светильника', 'Цена светильника'])
        for item in items:
            writer.writerow([item['Название светильника'], item['Цена светильника']])

def pagination():
    PAGENATION = int(input('Введите кол-во страниц: '))
    wildpak_nout = []
    for page in range(1, PAGENATION+1):
        print(f'Страница {page} готова')
        html = get_html(URL, params={'page' : page})
        wildpak_nout.extend(get_content(html.text))
    save(wildpak_nout, CSV)
    print('Готово')


if __name__ == '__main__':
    pagination()