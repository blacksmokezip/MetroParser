import json
from bs4 import BeautifulSoup as bs
from pathlib import Path

from metroparser.init_data import ENCODING


def get_page_in_html(path_to_html: str) -> bs:
    """Gets BS4 page from html file"""

    with open(path_to_html, 'r', encoding=ENCODING) as file:
        index_html = file.read()

    return bs(index_html, 'lxml')


def get_list_of_products(soup: bs) -> dict:
    """Returns dictionary of products"""

    elements = soup.find_all(attrs={'data-sku': True})

    products = {}

    for e in elements:

        #check if product is available
        if e.find(
                'p',
                class_='product-title catalog-2-level-product' +
                       '-card__title style--catalog-2-level-product-card'
        ) is not None:
            continue

        name = e.find('span', class_='product-card-name__text').text.strip()
        products[name] = {}
        products[name]['id'] = e['data-sku']
        url = 'https://online.metro-cc.ru' + e.find(
            'a',
            attrs={'href': True}
        )['href']
        products[name]['url'] = url

        if e.find(
                'div',
                class_='product-unit-prices__old-wrapper'
        ).find('span', class_='product-price__sum-rubles') is None:
            actual_price = e.find(
                'div',
                class_='product-unit-prices__actual-wrapper'
            ).find(
                'span',
                class_='product-price__sum-rubles'
            ).text.replace('\xa0', '')
            products[name]['regular-price'] = actual_price
            products[name]['promo-price'] = 'None'

        else:
            actual_price = e.find(
                'div',
                class_='product-unit-prices__actual-wrapper'
            ).find(
                'span',
                class_='product-price__sum-rubles'
            ).text.replace('\xa0', '')

            old_price = e.find(
                'div',
                class_='product-unit-prices__old-wrapper'
            ).find(
                'span',
                class_='product-price__sum-rubles'
            ).text.replace('\xa0', '')

            products[name]['regular-price'] = old_price
            products[name]['promo-price'] = actual_price

        brand = 'None'

        for b in get_all_brands(soup):
            if b in name.lower():
                brand = b.capitalize()

        products[name]['brand'] = brand

    return products


def get_all_brands(soup: bs) -> list:
    """Returns all brands"""

    brands = soup.find(
        'div',
        class_='catalog-checkbox-group'
    ).text.replace('\n', '').strip().lower().split('            ')

    return brands


def parse_to_json(data, city, center):
    """Parse data to json file"""

    fle = Path(f'../result/{city}/data_{center}.json')
    fle.touch()

    with open(
        f'../result/{city}/data_{center}.json',
        'w',
        encoding=ENCODING
    ) as file:
        return json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4, sort_keys=True
        )
