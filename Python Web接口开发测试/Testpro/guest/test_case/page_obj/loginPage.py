# -*- coding utf-8 -*-
# @author:"zhangJingHua"

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
    '''
    用户登录页面
    '''
    url='/'

    #页面元素位置
    guest_login_text_loc=(By.XPATH,"//h2[text()='Guest System']")  #登陆页面上的Guest System文本位置
    login_username_loc=(By.ID,"inputUsername")   #用户名输入框
    login_password_loc=(By.ID,"inputPassword")   #密码输入框
    login_button_loc=(By.XPATH,"//button[@type='submit']")  #登陆按钮

    #点击登陆按钮后的提示信息元素
    user_or_password_error_hint_loc=(By.XPATH,"//p[contains(text(),'username or password')]")  #用户名或者密码错误信息

    #登陆Action
    def guest_login(self):
        self.find_element(*self.guest_login_text_loc).text()
        sleep(1)
        self.find_element(*self.login_button_loc).click()

    # 输入登陆用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)

    #输入登陆密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)

    #点击登陆按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()


    #定义统一登陆入口
    def user_login(self,username='username',password='password'):
        """获取用户名、密码，登陆"""
        self.open()
        self.guest_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    #用户名或者密码错误提示
    def user_or_password_error_hint(self):
        return self.find_element(*self.user_or_password_error_hint_loc).text




