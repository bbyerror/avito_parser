'''This module is main module for parser'''
import json
from selenium import webdriver
from fake_useragent import UserAgent
from avito_funcs import AvitoSearcher


class Parser:
    '''main class to guide parser'''     
    def __init__(self,
                 link:str,
                 min_price: int,
                 max_price: int,
                 search_items: int,
                 search_pages: int,
                 title_file: str):

        self.link = link
        self.title_file=title_file
        self.search_items = search_items
        self.search_pages = search_pages
        self.max_price = int(max_price)
        self.min_price = int(min_price)
        self.data = []
        self.driver = self.__driver_setup()

    def __driver_setup(self):
        """_webdriver and its options_
        """
        options = webdriver.ChromeOptions()
        options.add_argument(f'user-agent={UserAgent().random}')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        return self.driver
    def __driver_get_url(self):
        """__driver_get_url_
        """
        self.driver.get(self.link)

    def next_page(self):
        """_finds next page btn_
        """
        return self.driver.find_element(*AvitoSearcher.NEXT_PAGE_BTN)

    def get_items(self):
        """_finds items on the page_
        """
        return self.driver.find_elements(*AvitoSearcher.ITEMS)

    def get_info(self, item) -> dict:
        """_item to dict_
        """
        link = item.find_element(*AvitoSearcher.LINK).get_attribute('href')
        item_name = item.find_element(*AvitoSearcher.NAME)
        description = item.find_element(*AvitoSearcher.DESCRIPTION)
        price = item.find_element(
            *AvitoSearcher.PRICE).get_attribute('content')
        self.min_price=int(price)
        return {'item_name': item_name.text,
                'price': price,
                'description': description.text,
                'link': link}
    def write_info(self,info:dict):
        """_write info_
        """
        with open(f'{self.title_file}.txt', 'a', encoding='utf-8') as file:
            file.write('\n')
            json.dump(info, file, ensure_ascii=False)

    def pasrse_page(self) -> list:
        """_parse page_
        """
        items = self.get_items()
        for item in items:
            info = self.get_info(item)
            self.write_info(info=info)
    def parse_avito(self):
        """_fn parser runner_
        """
        self.__driver_get_url()
        item_cnt = 1
        page_cnt = 1
        while page_cnt <= self.search_pages and item_cnt <= self.search_items and self.min_price <= self.max_price:
            page_cnt += 1
            self.pasrse_page()
            item_cnt += 1
            if self.next_page():
                self.next_page().click()
            else:
                break

    def close_parser(self):
        """_parser close_
        """
        self.driver.quit()


if __name__ == '__main__':
    parser = Parser(search_items=1000,
                    search_pages=1000,
                    link='https://www.avito.ru/',
                    title_file='parsed_data',
                    max_price=50000,
                    min_price=20000)
    try:
        parser.parse_avito()
    except Exception as ex:
        print(ex)
    finally:
        parser.close_parser()
