# -*- coding utf-8 -*-
# @author:"zhangJingHua"

from time import sleep
import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from guest.test_case.models import myunit,function
from guest.test_case.page_obj.loginPage import login
from guest.test_case.page_obj.GuestManageSystemPage import GuestManageSystem

class loginTest(myunit.Mytest)
    '''社区登陆测试'''

    #测试用户登陆
    def user_login_verify(self,usesrname="",password=""):
        login(self.driver).user_login(self.username,self.password)

    def test_login1(self):
        ''''''
        login(self.driver).user_login(username,password)

    def test_login2(self):
        login(self.driver).user_login(username,password)

    def test_login3(self):
        login(self.driver).user_login(username,password)


