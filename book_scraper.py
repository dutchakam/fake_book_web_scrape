# @Time    : 2021/03/30
# @Author  : alexanderdutchak@gmail.com
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup

filename = 'fake_book_scrape.csv'
f = open(filename, 'w')
headers = 'Title,Price,Rating,InStock\n'
f.write(headers)

for page in range(1, 51):
    url = f'http://books.toscrape.com/catalogue/page-{page}.html'

    html_req = requests.get(url)

    page_soup = BeautifulSoup(html_req.text, 'html.parser')

    conTitle = page_soup.findAll('h3')
    titles = []
    for name in conTitle:
        nam = str(name).split('"')
        titles.append(nam[3].replace(',', ''))

    conPrice = page_soup.findAll('p', {'class': 'price_color'})
    prices = []
    for cost in conPrice:
        price = cost.text
        prices.append(price[1:])

    conRating = page_soup.findAll('p', {'class': 'star-rating'})
    ratings = []
    for stars in conRating:
        star = str(stars).split('"')[1]
        star = str(star).split(' ')[1]
        ratings.append(star)

    conStock = page_soup.findAll('p', {'class': 'instock availability'})
    in_stock = []
    for stocked in conStock:
        st = str(stocked.text).split(' ')
        in_stock.append(' '.join(st[12:14])[:-1])

    zipped_list = [(a, b, c, d) for a, b, c, d in zip(titles, prices, ratings, in_stock)]

    for item in zipped_list:
        f.write(item[0] + ',' + item[1] + ',' + item[2] + ',' + item[3] + '\n')

f.close()
