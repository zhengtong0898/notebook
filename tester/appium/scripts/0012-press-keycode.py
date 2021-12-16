import time
from appium import webdriver


# KeyCode:  https://blog.csdn.net/feizhixuan46789/article/details/16801429
driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",
                          desired_capabilities={"platformName": "Android"})


driver.implicitly_wait(10)


# 启动京东app
driver.activate_app("com.jingdong.app.mall")


# 找到京东超市图标
jdcs_element = driver.find_elements_by_id("com.jingdong.app.mall:id/gw")[0]
jdcs_element.click()


# KeyCode: 4-返回键
# adb.exe shell input keyevent 4                # 备注: 在 Appium 的日志中没有找到相关的adb命令.
time.sleep(5)
driver.press_keycode(4)


# KeyCode: 3-Home键
# adb.exe shell input keyevent 3                # 备注: 在 Appium 的日志中没有找到相关的adb命令.
time.sleep(5)
driver.press_keycode(3)
