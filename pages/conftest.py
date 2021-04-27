import pytest
from selenium import webdriver
from pages.loginpage import login

@pytest.fixture(scope='session')
def driver(request):
    driver=webdriver.Chrome()
    #先调用login函数登录
    login(driver)
    def end():
        driver.quit()
    request.addfinalizer(end)#终结函数
    return driver