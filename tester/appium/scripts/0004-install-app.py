import os
import time
from appium import webdriver


driver = webdriver.webdriver.WebDriver("http://localhost:4723/wd/hub", desired_capabilities={"platformName": "Android"})
time.sleep(5)


# 检查app是否已安装.
# adb shell dumpsys package com.example.myapplication
is_installed = driver.is_app_installed(bundle_id="com.example.myapplication")


# 如果app已经安装, 删除掉它.
# adb uninstall com.example.myapplication
if is_installed: driver.remove_app(app_id="com.example.myapplication")


# 安装app.
# adb install -r app_path
abspath = os.path.abspath(os.curdir)
abspath = os.path.join(abspath, "0004-app-debug.apk")
driver.install_app(app_path=abspath)


# shell am force-stop org.chromium.webview_shell
time.sleep(3)
driver.quit()
