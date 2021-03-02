# -*- coding utf-8 -*-
# @author:"zhangJingHua"

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class GuestManageSystem(Page):
    '''Guest Manage System页面'''

    # 定位页面元素
    guest_manage_system_text_loc=(By.XPATH,"//div//a[@href='/event_manage/']")  #Guest Manage System文本位置
    choose_event_loc=(By.XPATH,"//div[@id='navbar']//ul[1]//li[1]/a") #选择event列表选项卡位置
    choose_guest_loc=(By.XPATH,"//div[@id='navbar']//ul[1]//li[2]//a")  #选择guest列表选项卡位置
    guest_username_text_loc = (By.XPATH, "//div[@id='navbar']//ul[2]//li[1]//a")  # 登录用户名的文本显示位置
    logout_user_loc = (By.XPATH, "//div[@id='navbar']//ul[2]//li[2]//a")  # 退出登录位置
    event_search_loc=(By.NAME,'name') #event搜索框位置
    event_search_button=(By.CSS_SELECTOR,'button') #搜索按钮位置

    #获取用户名
    def login_success_username(self):
        return self.find_element(*self.guest_username_text_loc).text  #获取用户名文本