from selenium import webdriver as wd
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as bs
import time
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from pathlib import Path

from metroparser.init_data import ENCODING, TIME_DELAY, ALL_CENTERS, CITIES


def count_pages(driver) -> int:
    """Returns number of pages"""

    try:
        try:
            catalog_paginate = driver.find_element(
                By.XPATH,
                '//*[@id="catalog-wrapper"]/main/div[2]/nav/ul'
            ).get_attribute('outerHTML')
        except NoSuchElementException:
            catalog_paginate = driver.find_element(
                By.XPATH,
                '//*[@id="catalog-wrapper"]/main/div[3]/nav/ul'
            ).get_attribute('outerHTML')
        soup = bs(catalog_paginate, 'lxml')
    except Exception as e:
        print(e)

    return int(soup.find_all('li')[-2].text)


def get_pages(driver, num_of_pages, city, center):
    """Goes through all the pages and gets the html code"""

    try:
        for i in range(1, num_of_pages + 1):
            if i == num_of_pages:

                fle = Path(f'../html/{city}/index_{center}.html')
                fle.touch()

                with open(
                    f'../html/{city}/index_{center}.html',
                    'w',
                    encoding=ENCODING
                ) as file:
                    file.write(driver.page_source)
                break

            try:
                find_more_button = driver.find_element(
                    By.CSS_SELECTOR,
                    '#catalog-wrapper > main > div:nth-child(2) > button > span'
                )
            except NoSuchElementException:
                find_more_button = driver.find_element(
                    By.CSS_SELECTOR,
                    '#catalog-wrapper > main > div:nth-child(3) > button > span'
                )

            driver.execute_script(
                "arguments[0].click();", find_more_button)

            time.sleep(TIME_DELAY)

    except Exception as e:
        print(e)


def get_city(driver, city_xpath):
    """Changes city"""

    try:
        change_city = driver.find_element(
            By.XPATH,
            (
                '//*[@id="__layout"]/div/div/div[1]/'
                'header/div[2]/div[1]/div[2]/button'
            )
        )
        change_city.click()
        time.sleep(TIME_DELAY)

        pickup = driver.find_element(
            By.CSS_SELECTOR,
            "body > div.dialog-root > div > div > div"
            " > div.receipt-order > div:nth-child(1)"
            " > div.receipt-order__types > div"
            " > label:nth-child(2) > span > span > span"
        )
        pickup.click()
        time.sleep(TIME_DELAY)

        city_input = driver.find_element(
            By.CSS_SELECTOR,
            "body > div.dialog-root > div > div > div"
            " > div.receipt-order > div:nth-child(1)"
            " > div.pickup > div.pickup__select"
            " > div:nth-child(1) > div > div.multiselect__select"
        )
        city_input.click()
        time.sleep(TIME_DELAY)

        choose_city = driver.find_element(By.CSS_SELECTOR, city_xpath)
        choose_city.click()
        time.sleep(TIME_DELAY)

        save = driver.find_element(
            By.CSS_SELECTOR,
            "body > div.dialog-root > div > div > div"
            " > div.receipt-order > div:nth-child(1)"
            " > div.pickup > div.pickup__select"
            " > div.pickup__apply-btn-desk > button > span"
        )
        save.click()
        time.sleep(TIME_DELAY)

    except Exception as e:
        print(e)


def get_center(driver, center_xpath):
    """Changes center"""

    try:
        show_centers = driver.find_element(
            By.XPATH,
            (
                '//*[@id="__layout"]/div/div/div[1]/'
                'header/div[2]/div[1]/div[2]/button'
            )
        )
        show_centers.click()
        time.sleep(TIME_DELAY)

        pickup = driver.find_element(
            By.CSS_SELECTOR,
            "body > div.dialog-root > div > div > div"
            " > div.receipt-order > div:nth-child(1)"
            " > div.receipt-order__types > div"
            " > label:nth-child(2) > span > span > span"
        )
        pickup.click()
        time.sleep(TIME_DELAY)

        open_centers = driver.find_element(
            By.CSS_SELECTOR,
            (
                'body > div.dialog-root > div > div'
                ' > div > div.receipt-order > div:nth-child(1)'
                ' > div.pickup > div.pickup__select'
                ' > div:nth-child(2) > div > div.multiselect__select'
            )
        )
        open_centers.click()
        time.sleep(TIME_DELAY)

        choose_center = driver.find_element(By.CSS_SELECTOR, center_xpath)
        choose_center.click()
        time.sleep(TIME_DELAY)

        save = driver.find_element(
            By.CSS_SELECTOR,
            "body > div.dialog-root > div > div > div"
            " > div.receipt-order > div:nth-child(1)"
            " > div.pickup > div.pickup__select"
            " > div.pickup__apply-btn-desk > button > span"
        )
        save.click()
        time.sleep(TIME_DELAY)

    except Exception as e:
        print(e)


def get_source_html(url: str, center: str, city: str) -> None:
    """Get full html code"""

    useragent = UserAgent()

    service = Service(
        executable_path="../driver/driver"
    )

    options = Options()
    options.add_argument(f"user-agent={useragent.chrome}")
    driver = wd.Chrome(service=service, options=options)
    driver.maximize_window()

    try:
        driver.get(url=url)
        get_city(driver, CITIES[city])
        get_center(driver, ALL_CENTERS[city][center])
        get_pages(
            driver,
            count_pages(driver),
            city,
            center
        )

    except Exception as e:
        print(e)

    finally:
        driver.close()
        driver.quit()
