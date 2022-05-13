from bs4 import BeautifulSoup
import requests
import csv
#
list_appart = []
page = int(input('Сколько страниц спарсить: '))


# # def pagenation()
for i in range(0, page):
    PAGENATOR = f'https://stroka.kg/kupit-kvartiru/?&p={i}#paginator'
    r = requests.get(PAGENATOR, verify=True)
#
#     #get_content()
#     #save()
#
#     # #def get_content()
    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.findAll('tr', class_='topics-item-tr topics-item-tr-title')
    for item in items:
        apartment_cost = item.find(
                'td', class_='topics-item-topic_cost topics-item-td')
        if apartment_cost is None:
            apartment_cost = item.find('td', class_='topics-item-topic_cost topics-item-td som')

        list_appart.append({
            'Стоимость квартиры': apartment_cost,
            'Количество комнат': item.find(
                'td', class_='topics-item-td topics-item-topic_rooms').get_text(strip=True),
            'Площадь': item.find(
                'td', class_='topics-item-topic_area topics-item-td').get_text(strip=True),
            'Серия': item.find(
                'td', class_='topics-item-topic_series topics-item-td').get_text(strip=True),
            'Описание': item.find(
                'td', class_='topics-item-topic_name topics-item-td').get_text(strip=True)
            })
    print(f'Страница номер {i} готова')

# # def save()
with open('appart.csv', 'w') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Стоимость квартиры', 'Количество комнат', 'Площадь', 'Серия', 'Описание'])
    for item in list_appart:
        writer.writerow([item['Стоимость квартиры'], item['Количество комнат'], item['Площадь'],item['Серия'],item['Описание']])


if __name__ == '__main__':
    pass