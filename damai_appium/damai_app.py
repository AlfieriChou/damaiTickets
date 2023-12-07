# -*- coding: UTF-8 -*-
"""
__Author__ = "WECENG"
__Version__ = "1.0.0"
__Description__ = "大麦app抢票自动化"
__Created__ = 2023/10/26 10:27
"""
from time import sleep

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from config import Config
from ocr import capture_and_ocr
import random
# 加载配置信息
config = Config.load_config()

device_app_info = AppiumOptions()
# 操作系统
device_app_info.set_capability('platformName', 'Android')
# 操作系统版本
device_app_info.set_capability('platformVersion', '14')
# 设备名称
device_app_info.set_capability('deviceName', '69b6b7a4')
# app package
device_app_info.set_capability('appPackage', 'cn.damai')
# app activity name
device_app_info.set_capability('appActivity', '.launcher.splash.SplashMainActivity')
# 使用unicode输入
device_app_info.set_capability('unicodeKeyboard', True)
# 隐藏键盘
device_app_info.set_capability('resetKeyboard', True)
# 不重置app
device_app_info.set_capability('noReset', True)
# 超时时间
device_app_info.set_capability('newCommandTimeout', 6000)

# 使用uiautomator2驱动
device_app_info.set_capability('automationName', 'UiAutomator2')


# 连接appium server，server地址查看appium启动信息
driver = webdriver.Remote(config.server_url, options=device_app_info)

# sleep(5)

# 设置等待时间，等待1s
driver.implicitly_wait(0.5)
# 空闲时间10ms,加速
driver.update_settings({"waitForIdleTimeout": 10})

# # 点击搜索框
# driver.find_element(by=By.ID, value='homepage_header_search_btn').click()

# # 输入搜索关键词
# driver.find_element(by=By.ID, value='header_search_v2_input').send_keys(config.keyword)

# # 点击第一个搜索结果
# driver.find_element(by=By.XPATH,
#                     value='//androidx.recyclerview.widget.RecyclerView[@resource-id="cn.damai:id/search_v2_suggest_recycler"]/android.widget.RelativeLayout[1]').click()

# # 点击结果列表的第一个
# driver.find_element(by=By.XPATH,
#                     value='(//android.widget.LinearLayout[@resource-id="cn.damai:id/ll_search_item"])[1]').click()

# if driver.find_elements(by=By.XPATH,
#                         value='//android.widget.FrameLayout[@resource-id="cn.damai:id/trade_project_detail_purchase_status_bar_container_fl"]'):
#     # 城市选择
#     for city in driver.find_elements(by=By.ID, value='tv_tour_city'):
#         if config.city in city.text:
#             city.click()
#             break
#     # 日期选择
#     for date in driver.find_elements(by=By.ID, value='tv_tour_time'):
#         if config.date in date.text:
#             date.click()
#             break

while driver.find_elements(by=By.XPATH,
                           value='//android.widget.FrameLayout[@resource-id="cn.damai:id/trade_project_detail_purchase_status_bar_container_fl"]'):
    # buy_btnList = driver.find_elements(by=By.XPATH, value='//*[contains(@text, "立即购买")]')
    # buy_btnList =driver.find_elements(by=AppiumBy.ANDROID_UIAUTOMATOR,value='new UiSelector().text("立即购买")')
    # buy_btn = driver.find_element(by=By.XPATH,
    #                               value='//android.widget.TextView[@resource-id="cn.damai:id/tv_left_main_text"]').text
    # print('aaaaaaaaaaa',buy_btnList)
    # bot_btn_list=driver.find_elements(by=By.XPATH,
    #                         value='//android.widget.FrameLayout[@resource-id="cn.damai:id/trade_project_detail_purchase_status_bar_container_fl"]')
    # 定义需要截取的区域的坐标
    left, top, right, bottom = 560, 2290, 650, 2350

    # 调用函数获取文字
    bot_btn= capture_and_ocr(driver, left, top, right, bottom)
    # print('bbbb',bot_btn)
    # print('bbbbtext',bot_btn.text) 
    # print('bbbbtag_name',bot_btn.tag_name)
    # print('bbbb href',bot_btn.get_attribute('href'))
    
    
    # 立即购买
    if '立' in bot_btn or '缺' in bot_btn:
        # 点击立即购买
        # driver.find_element(by=By.XPATH,
        #                     value='//android.widget.FrameLayout[@resource-id="cn.damai:id/trade_project_detail_purchase_status_bar_container_fl"]/android.widget.LinearLayout').click()
        # 生成随机坐标
        random_x = random.randint(left, right)
        random_y = random.randint(top, bottom)

        # 在 Appium 中点击随机坐标
        driver.tap([(random_x, random_y)])

        # 票价选择
        if driver.find_elements(by=By.ID, value='project_detail_perform_price_flowlayout'):
            driver.find_element(by=By.XPATH,value='(//android.widget.TextView[@resource-id="cn.damai:id/item_text"])[{}]'.format(config.priceList[0])).click()
            print('config.priceList[0]',config.priceList[0])            
            # for price in driver.find_elements(by=By.XPATH,
            #                                   value='//android.widget.TextView[@resource-id="cn.damai:id/item_text"]'):
            #     print('pricesss',price.text)
            #     if config.price in price.text:
            #         price.click()
            #         print('price_select')

        # 数量选择
        if driver.find_elements(by=By.ID, value='layout_num') and config.users is not None:
            for i in range(len(config.users) - 1):
                driver.find_element(by=By.ID, value='img_jia').click()
                print('num_select')
            
        comfirm=False
        priceIndex=0
        # 确认
        while not comfirm:
            if driver.find_elements(by=By.ID, value='btn_buy'):
                # buy_btn=driver.find_element(by=By.ID, value='btn_buy')
                buy_btn=driver.find_element(by=By.XPATH, value='//android.widget.LinearLayout[@resource-id="cn.damai:id/btn_buy"]/android.widget.TextView')
                print('btn_buyssssssssss',buy_btn)
                if buy_btn.text !='提交缺货登记':
                    buy_btn.click()
                    comfirm=True
                else:
                    priceIndex= (priceIndex+1) % len(config.priceList)
                    # print('priceIndex',priceIndex)
                    index=config.priceList[priceIndex]
                    print(index)
                    # 票价选择
                    if driver.find_elements(by=By.ID, value='project_detail_perform_price_flowlayout'):
                        driver.find_element(by=By.XPATH,
                                                         value='(//android.widget.TextView[@resource-id="cn.damai:id/item_text"])[{}]'.format(index)).click()
                        
                        print('price_select2')
                        # for price in driver.find_elements(by=By.XPATH,
                        #                                 value='//android.widget.TextView[@resource-id="cn.damai:id/item_text"]'):
                        #     # print('pricesss',price.text)
                        #     if config.priceList[priceIndex] in price.text:
                        #         price.click()
                        #         print('price_select2')

                    # 数量选择
                    if driver.find_elements(by=By.ID, value='layout_num') and config.users is not None:
                        for i in range(len(config.users) - 1):
                            driver.find_element(by=By.ID, value='img_jia').click()
                            print('num_select2')
                
        if comfirm:
            print('comfirm')
            # 选择人员
            if driver.find_elements(by=By.ID, value='recycler_main') and config.users is not None:
                identity_elements = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("身份证")')
                parent_elements = [element.parent for element in identity_elements]
                for user in config.users:
                    for user_element in parent_elements:
                        user_select_list = user_element.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,
                                                                    'new UiSelector().textContains("' + str(user) + '")')
                        for user_select in user_select_list:
                            user_select.click()
                            print('user_select')
                            break
                        break
            # 提交订单
            if config.if_commit_order:
                if driver.find_elements(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                    value='new UiSelector().text("提交订单")'):
                    print('handleOrder')
                    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("提交订单")').click()
    # if  '抢' in bot_btn:
    #     # 预约购票
    #     driver.find_element(by=By.XPATH,
    #                         value='//android.widget.FrameLayout[@resource-id="cn.damai:id/trade_project_detail_purchase_status_bar_container_fl"]/android.widget.LinearLayout').click()

    #     # 日期选择
    #     if driver.find_elements(by=By.ID, value='project_detail_perform_flowlayout'):
    #         for date in driver.find_elements(by=By.XPATH,
    #                                           value='//android.widget.TextView[@resource-id="cn.damai:id/item_text"]'):
    #             if config.date in date.text:
    #                 date.click()
    #                 break

    #     # 票价选择
    #     if driver.find_elements(by=By.ID, value='project_detail_perform_price_flowlayout'):
    #         for price in driver.find_elements(by=By.XPATH,
    #                                           value='//android.widget.TextView[@resource-id="cn.damai:id/item_text"]'):
    #             if config.price in price.text:
    #                 price.click()
    #                 break
    #     # 提交
    #     if driver.find_elements(by=By.ID, value='btn_buy_bottom_div_line'):
    #         driver.find_element(by=By.XPATH,
    #                             value='//android.view.View[@resource-id="cn.damai:id/btn_buy_bottom_div_line"]/..').click()
    # if '已' in bot_btn:
    #     # 已预约
    #     break
    else:
        # 模拟下拉刷新
        driver.swipe(500, 400, 500, 2000, 300)
        sleep(0.5)

driver.quit()
