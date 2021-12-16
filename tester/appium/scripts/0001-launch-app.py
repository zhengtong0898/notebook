import time
from appium import webdriver


caps = {"platformName": "Android",
        "platformVersion": "10",                      # adb.exe shell getprop ro.build.version.release
        "deviceName": "emulator-5554",                # adb.exe devices
        "appPackage": "org.chromium.webview_shell",   # adb shell dumpsys activity recents | grep "RecentTaskInfo #0" -A 5 | awk '/baseIntent/{print $(NF-1)}'
        "appActivity": ".WebViewBrowserActivity"}


# webdriver.webdriver.WebDriver == webdriver.Remote
# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=caps)
driver = webdriver.webdriver.WebDriver("http://localhost:4723/wd/hub", desired_capabilities=caps)
time.sleep(5)

driver.quit()
