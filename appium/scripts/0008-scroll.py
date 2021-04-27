import time
import json
from appium import webdriver


driver = webdriver.webdriver.WebDriver("http://localhost:4723/wd/hub",
                                       desired_capabilities={"platformName": "Android"})


# 隐式等待10秒
driver.implicitly_wait(10)


# 启动京东app
driver.activate_app("com.jingdong.app.mall")


# 京东超市图标
element_top = driver.find_elements_by_id("com.jingdong.app.mall:id/gw")[0]


# 取京东超市图标的右下角的 y 坐标.
bounds = element_top.get_attribute("bounds")
bounds_json = json.loads("".join(["[", bounds.replace("][", "],["), "]"]))
y_top = bounds_json[1][1]


# 立即登录按钮
element_bottom = driver.find_element_by_id("com.jingdong.app.mall:id/ie")


# 取立即登录按钮的右下角的 x, y 坐标.
bounds = element_bottom.get_attribute("bounds")
bounds_json = json.loads("".join(["[", bounds.replace("][", "],["), "]"]))
x_bottom, y_bottom = bounds_json[1]


# 按象数, 有惯性, 从下往上滑动.
driver.swipe(x_bottom, y_bottom, x_bottom, y_top)


# 按象数, 无惯性, 从上往下滑动(duration时间越长, 惯性越小).
driver.swipe(x_bottom, y_top, x_bottom, y_bottom, duration=5000)


# 按元素, 有惯性, 从下往上滑动
driver.scroll(element_bottom, element_top, duration=5000)


# 按元素, 无惯性, 从上往下滑动
driver.drag_and_drop(element_top, element_bottom)


time.sleep(3)
driver.quit()
