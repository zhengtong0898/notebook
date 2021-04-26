from appium import webdriver


driver = webdriver.webdriver.WebDriver("http://localhost:4723/wd/hub",
                                       desired_capabilities={"platformName": "Android"})


# 启动京东app
driver.activate_app("com.jingdong.app.mall")


# 获取搜索文本框组件, 采用多层级递进写法.
# api:     '/wd/hub/session/${session-id}/elements'
# params:  '{"using": "xpath",
#            "value": "//android.widget.ViewFlipper//android.widget.LinearLayout//android.widget.TextView"}'
ss = driver.find_element_by_xpath("//android.widget.ViewFlipper//android.widget.LinearLayout//android.widget.TextView")


# 获取当前节点的属性值, 本例通过'content-desc'获得文本信息, 也可以通过'bounds'获取坐标信息.
# api:     '/wd/hub/session/${session-id}/element/${element-id}/attribute/content-desc'
# params:  '{"name": "content-desc", "id": "${element-id}"}'
content = ss.get_attribute("content-desc")
bounds = ss.get_attribute("bounds")
