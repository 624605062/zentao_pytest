from selenium import webdriver
from commom.base import Base
import pytest
host='http://127.0.0.1:80'
url=host+'/zentao/user-login-L3plbnRhby8=.html'
#-------定位元素信息--------#
loc1=('id','account')
loc2=('css selector','[name="password"]')
loc3=('xpath',"//*[@id='submit']")

def login(driver,user='admin',psw='123456'):
    '''普通登录函数'''
    zen=Base(driver)
    driver.get(url)
    zen.sendkeys(loc1,user)
    zen.sendkeys(loc2,psw)
    zen.click(loc3)

if __name__ == '__main__':
    driver=webdriver.Chrome()
    login(driver)
