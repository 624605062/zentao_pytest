from selenium import webdriver
from commom.base import Base
import pytest
#-------------定位元素------------------#
loc1=('id','account')
loc2=('css selector','[name="password"]')
loc3=('xpath',"//*[@id='submit']")
login_user=('css selector','#ueseMenu>a')#登录后的用户名
class TestZenTaoLogin():
    driver=webdriver.Chrome()
    zen=Base(driver)
    url='http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html'

    def setup(self):
        self.driver.get(self.url)

    def teardown(self):
        '''数据清理'''
        print('清空cookies,退出登录状态')
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def teardown_class(self):
        '''用例执行完成最后退出'''
        print('teardown_class：用例执行完成，关闭浏览器')
        self.driver.quit()

    def test_login_1(self):
        '''登录成功用例：账户->admin,密码->123456'''
        self.zen.sendkeys(loc1,'admin')
        self.zen.sendkeys(loc2,'123456')
        self.zen.click(loc3)
        result=self.zen.get_text(login_user)
        print('登录结果，获取到用户名：%s'%result)
        assert  result=='admin'

    def test_login_2(self):
        '''登录失败用例：账户->admin,密码->111'''
        self.zen.sendkeys(loc1, 'admin')
        self.zen.sendkeys(loc2, '111')
        self.zen.click(loc3)
        result = self.zen.get_text(login_user)
        print('登录结果，获取到用户名：%s' % result)
        assert result == ""
if __name__ == '__main__':
    pytest.main(['-v','test_login.py'])