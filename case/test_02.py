import pytest
import time
from selenium import webdriver
def test_baidu(driver):
    driver=webdriver.Chrome()
    driver.get('https://www.baidu.com')
    time.sleep(3)
    t=driver.title
    print('测试结果：%s'%t)
    assert '百度一下' in t,'失败原因：打开百度失败'

if __name__ == '__main__':
    pytest.main(['-v','test_02.py'])

