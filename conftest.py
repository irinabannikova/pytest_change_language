import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="ru", help="Choose language for testing")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    
    options = webdriver.ChromeOptions() #создаем объект options, который представляет настройки для браузера Chrome
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    #добавили экспериментальную опцию. Устанавили значение intl.accept_languages равным выбранному языку (language), 
    #указываем браузеру, на каком языке отображать веб-страницу.
    
    driver = webdriver.Chrome(options=options) #инициализируем экземпляр браузера Chrome с переданными опциями options,
    
    yield driver #возврат объекта driver в качестве результата функции
    
    driver.quit()

