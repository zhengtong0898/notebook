import time
from appium import webdriver


state_map = {0: "app尚未安装",
             1: "app尚未运行",
             2: "app在后台运行中或暂停状态",               # TODO: 待处理.
             3: "app在后台运行中",
             4: "app在屏幕前运行中"}


driver = webdriver.webdriver.WebDriver("http://localhost:4723/wd/hub", desired_capabilities={"platformName": "Android"})
time.sleep(5)


# 获取指定app的状态
# TODO: 尚未确定返回值是依据哪个文本特征, 待处理
#       adb shell dumpsys window displays
#       adb shell pgrep -f \(\[\[:blank:\]\]\|\^\)com\.example\.myapplication\(\[\[:blank:\]\]\|\$\)
app_state = driver.query_app_state(app_id="com.example.myapplication")
print(state_map[app_state])


# 将屏幕前的app置于后台5秒, 然后再将其返回到屏幕前.
# Pressing the HOME button: adb shell input keyevent 3;
driver.background_app(5)


# shell am force-stop org.chromium.webview_shell
time.sleep(3)
driver.quit()
