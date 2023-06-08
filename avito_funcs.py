'''special class for searching elements on Avito.'''
from selenium.webdriver.common.by import By

class AvitoSearcher:
    """Set of supported searcher strategies."""
    NEXT_PAGE_BTN = (By.CSS_SELECTOR, '[data-marker="pagination-button/nextPage"]')
    ITEMS = (By.CSS_SELECTOR, "[data-marker='item']")
    NAME = (By.CSS_SELECTOR, "[itemprop='name']")
    DESCRIPTION = (By.CSS_SELECTOR, "[class*='item-description']")
    LINK = (By.CSS_SELECTOR, "[data-marker='item-title']")
    PRICE = (By.CSS_SELECTOR, "[itemprop='price']")
    TOTAL_VIEWS = (By.CSS_SELECTOR, "[data-marker='item-view/total-views']")
    DATE_PUBLIC = (By.CSS_SELECTOR, "[data-marker='item-view/item-date']")
    SELLER_NAME = (By.CSS_SELECTOR, "[data-marker='seller-info/label']")
    COMPANY_NAME = (By.CSS_SELECTOR, "[data-marker='seller-link/link']")
    COMPANY_NAME_TEXT = (By.CSS_SELECTOR, "span")