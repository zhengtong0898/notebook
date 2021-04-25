import time
from appium import webdriver


state_map = {0: "app尚未安装",
             1: "app尚未运行",
             2: "app在后台运行中或暂停状态",               # TODO: 待处理.
             3: "app在后台运行中",
             4: "app在屏幕前运行中"}


driver = webdriver.webdriver.WebDriver("http://localhost:4723/wd/hub",
                                       desired_capabilities={"platformName": "Android"})


state_en = driver.query_app_state("com.android.settings")
state_cn = state_map[state_en]
print("com.android.settings: state_cn: ", state_cn, "; state_en: ", state_en)


# 启动一个app
driver.activate_app("com.android.settings")

# 点击搜索框
driver.find_element_by_id("com.android.settings:id/search_action_bar_title").click()


# TODO: 这里为什么会报(An element could not be located on the page using the given search parameters)错?
# driver.find_element_by_id("android:id/search_src_text").send_keys("battery")


# 找到输入框, 输入battery;       xpath语法: https://www.w3school.com.cn/xpath/xpath_syntax.asp
# TODO: 所有查找元素指令的提交, appium-server都没有打印adb相关日志, 需通过打印remote提交的内容观察背后在做什么, 待处理.
driver.find_element_by_class_name("android.widget.EditText").send_keys("battery")        # class_name
driver.find_element_by_xpath("//android.widget.EditText[@class='android.widget.EditText']").send_keys("battery") # xpath
driver.find_element_by_css_selector("#search_src_text").send_keys("battery")             # css_selector 找 id
driver.find_element_by_css_selector(".android.widget.EditText").send_keys("battery")     # css_selector 找 class_name
