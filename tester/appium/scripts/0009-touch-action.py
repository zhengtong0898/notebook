import json
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


# 需要先给手机设定一个屏幕解锁(pattern)密码


# 唤醒屏幕: adb shell am start -n io.appium.settings/.Unlock
#                             -c android.intent.category.LAUNCHER
#                             -a android.intent.action.MAIN
driver = webdriver.webdriver.WebDriver("http://localhost:4723/wd/hub",
                                       desired_capabilities={"platformName": "Android"})
driver.implicitly_wait(10)


# 找到底部元素, 获取坐标
bottom_element = driver.find_element_by_id("com.android.systemui:id/ambient_indication_container")
bottom_coords = json.loads("".join(["[", bottom_element.get_attribute("bounds").replace("][", "],["), "]"]))
bottom_y = int(bottom_coords[0][1] + ((bottom_coords[1][1] - bottom_coords[0][1]) / 2))
bottom_x = int(bottom_coords[0][0] + ((bottom_coords[1][0] - bottom_coords[0][0]) / 2))


# 找到锁元素, 获取坐标
top_element = driver.find_element_by_id("com.android.systemui:id/lock_icon")
top_coords = json.loads("".join(["[", top_element.get_attribute("bounds").replace("][", "],["), "]"]))
top_x, top_y = top_coords[0]


# 向上滑动, 进入解锁(pattern)界面, TODO: 这里使用 press 无法触发向上滑动.
touch_action = TouchAction(driver)
touch_action.long_press(x=bottom_x, y=bottom_y, duration=100) \
            .move_to(x=top_x, y=top_y)                        \
            .release()                                        \
            .perform()


# 解锁, TODO: 这里使用 long_press 无法完成解锁动作.
touch_action.wait(ms=200)                            \
            .press(x=252, y=973)                     \
            .move_to(x=820, y=978)                   \
            .move_to(x=820, y=1257)                  \
            .move_to(x=254, y=1257)                  \
            .move_to(x=254, y=1539)                  \
            .move_to(x=820, y=1539)                  \
            .release()                               \
            .perform()

driver.quit()
