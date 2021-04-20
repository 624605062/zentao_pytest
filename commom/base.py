from selenium import webdriver
from selenium.webdriver.support.wait
import WebDriverWait
from selenium.webdriver.support
import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains
import ActionChains

class Base():
    '''基于原生的selenium做二次封装'''
    def __init__(self,driver):#初始化self,driver
        self.driver=driver
        self.timeout=10
        self.t=0.5
    def findElement(self,locator):
        '''定位到元素，返回元素的对象，没定位到，timeout异常'''
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        else:
            print('正在定位元素信息：定位方式->%s,value值—>%s'%(locator[0],locator[1]))#返回一个元组取下标0和1
            ele=WebDriverWait(self.driver,self.timeout,
                              self.t).until(EC.presence_of_element_located(locator))
            return ele
    def findElements(self,locator):
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        else:
            try:
                print('正在定位元素信息：定位方式->%s,value值—>%s'%(locator[0],locator[1]))
                eles=WebDriverWait(self.driver,
                                   self.timeout,
                                   self.t).until(EC.presence_of_element_located(locator))#显性等待方法
                return eles
            except:
                return []
    def sendkeys(self,locator,text=''):
        ele=self.findElement(locator)
        ele.send_keys(text)

    def click(self,locator):#点击方法
        ele=self.findElement(locator)
        ele.click()

    def clear(self,locator):#清除方法
        ele=self.findElement(locator)
        ele.clear()

    def isSelected(self,locator):
        '''判断元素是否被选中，返回bool布尔值'''
        ele=self.findElement(locator)
        r=ele.is_selected()
        return r

    def isElementExist(self,locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def is_title(self,_title=''):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver,
                                 self.timeout,
                                 self.t).until(EC.)
