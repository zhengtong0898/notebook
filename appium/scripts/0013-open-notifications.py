from appium import webdriver


driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",
                          desired_capabilities={"platformName": "Android"})


driver.implicitly_wait(10)


# 打开通知栏
driver.open_notifications()


# 找到并点击第一个通知项
jindong_notification = driver.find_element_by_xpath("//android.widget.TextView[@text='用新版京东是怎样的体验？']")
jindong_notification.click()
