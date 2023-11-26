from metroparser.collect_pages import get_source_html
from metroparser.parse_data import get_page_in_html, \
    parse_to_json, get_list_of_products
from metroparser.init_data import ALL_CENTERS, CITIES


def main():
    url = 'https://online.metro-cc.ru/category/chaj-kofe-kakao/kofe'

    for city in CITIES:
        for center in ALL_CENTERS[city]:
            get_source_html(
                url,
                center,
                city,
            )

            soup = get_page_in_html(
                f'../html/{city}/index_{center}.html'
            )
            parse_to_json(get_list_of_products(soup), city, center)


if __name__ == '__main__':
    main()
