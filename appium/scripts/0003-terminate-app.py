import time
from appium import webdriver


caps = {"platformName": "Android",
        "platformVersion": "10",                      # adb.exe shell getprop ro.build.version.release
        "deviceName": "emulator-5554",                # adb.exe devices
        "appPackage": "org.chromium.webview_shell",   # adb shell dumpsys activity recents | grep "RecentTaskInfo #0" -A 5 | awk '/baseIntent/{print $(NF-1)}'
        "appActivity": ".WebViewBrowserActivity"}

driver = webdriver.webdriver.WebDriver("http://localhost:4723/wd/hub", desired_capabilities=caps)
time.sleep(5)

# 启动一个app
# adb shell am start -W -n com.android.gallery3d/.app.GalleryActivity
driver.start_activity(app_package='com.android.gallery3d', app_activity='.app.GalleryActivity')


# 关闭一个app(注意: 不是当前app)
# adb shell am force-stop com.android.gallery3d
driver.terminate_app('com.android.gallery3d')


# shell am force-stop org.chromium.webview_shell
time.sleep(3)
driver.quit()
