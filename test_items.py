from selenium.webdriver.common.by import By
import pytest
import time

def test_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR,"button.btn-add-to-basket")
    
    assert add_to_cart_button.is_displayed(), "кнопка добавления в корзину не видна"