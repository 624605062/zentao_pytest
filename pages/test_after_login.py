from commom.base import Base
import pytest
import time

host='http://127.0.0.1:80'
url_hou=host+'/zentao/admin.html'
#进入后台页面测试
loc_h=('link text','后台')

loc_about_1=('id','proversion')
loc_about_2=('id','official')
loc_about_3=('id','changelog')
loc_about_4=('id','license')
loc_about_5=('id','extnsion')

class TestHouTai():
    @pytest.fixture(scope='function')
    def open_houtai(self,driver):
        '''每次用例回到后台一级界面首页'''
        self.hou=Base(driver)
        driver.get(url_hou)

    def test_01(self,driver,open_houtai):
        '''关于禅道——升级专业版本'''
        t1=self.hou.get_text(loc_about_1)
        assert t1=='升级专业版本'

    def test_02(self,open_houtai):
        '''关于禅道-官方网站'''
        t1=self.hou.get_text(loc_about_2)
        assert t1=='官方网站'


if __name__ == '__main__':
    pytest.main(['-v','test_after_login.py'])