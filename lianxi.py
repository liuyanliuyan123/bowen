# !/usr/bin/python
# -*-coding:UTF8-*-
# from appium import webdriver
#
#
#AaA
# from appium import webdriver
# desired_cap={
#     'platformName':'Android',
#     'platformVersion':'5.1.1',
#     'deviceName':'127.0.0.1:62001',
#     'appPackage':'com.tal.kaoyan',
#     'appActivity':'com.tal.kaoyan.ui.activity.SplashActivity',
#     'noReset':False
# }
# driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
# driver.implicitly_wait(3)
#
# def agree_powerl():
#     driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()
# def agree_picture():
#     driver.find_element_by_id('com.tal.kaoyan:id/tip_commit').click()
#
# agree_powerl()
# agree_picture()


from appium import webdriver



from appium import webdriver
desired_cap={
    'platformName':'Android',
    'platformVersion':'5.1.1',
    'deviceName':'127.0.0.1:62001',
    'appPackage':'com.tal.kaoyan',
    'appActivity':'com.tal.kaoyan.ui.activity.SplashActivity',
    'noReset':False
}
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
driver.implicitly_wait(3)

def agree_powerl():
    try:
        power1=driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except:
        print('no power1')
    else:
        power1.click()

def agree_picture():
    try:
        power2=driver.find_element_by_id('com.tal.kaoyan:id/tip_commit')
    except:
        print('no power2')
    else:
        power2.click()
def agree_zhuce():
    driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
def agree_touxiang():
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()

agree_powerl()
agree_picture()
agree_zhuce()
agree_touxiang()






