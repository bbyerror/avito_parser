from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent


# target url
url='https://www.avito.ru/nizhniy_novgorod/noutbuki/apple-ASgCAQICAUCo5A0U9Nlm?cd=1&f=ASgCAQECAUCo5A0U9NlmAUXGmgwVeyJmcm9tIjoyMDAwMCwidG8iOjB9&s=1'

# user-agent
ua=UserAgent()
fake_ua=f'user-agent={ua.random}'

# webdriver options
options=webdriver.ChromeOptions()
options.add_argument(fake_ua)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--headless')

driver=webdriver.Chrome(options=options)

try:
    driver.get(url=url)
#    print('shit, here we go again')
    driver.implicitly_wait(40)
 
    while driver.find_element(By.CSS_SELECTOR, "[data-marker*='pagination-button/next']"):
# count items
        num=1
        items=driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")

        for item in items:
            link=item.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
            item_name=item.find_element(By.CSS_SELECTOR, "[itemprop='name']")
            description=item.find_element(By.CSS_SELECTOR, "[class*='item-description']")
            price=item.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute('content')
            print(f'Item № {num} info parsed.')
# writeing item's info
            items_to_write=f''' \n{num}
            item_name : {item_name.text}
            price: {price}
            description': {description.text}
            link: {link}
            '''
# writeing item's info in file
            with open('avito.txt','a',encoding='utf-8') as file: 
                file.write(f'''{items_to_write}
                ''')
                print('item info writed.')
            num+=1

        driver.find_element(By.CSS_SELECTOR, "[data-marker*='pagination-button/next']").click()
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()