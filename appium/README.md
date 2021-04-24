### adb

adb 全名 Android Debug Bridge, 是一个调试工具.


|参数|说明|
|---|---|
|install| 安装apk |
|uninstall| 卸载apk |
|push| 将本地文件推送到手机 |
|pull| 将手机文件拉取到本地 |
|shell am| Activity(界面) Manager |
|shell dumpsys window windows| 获取当前界面信息 |
|shell dumpsys activity recents| 从最近打开的界面中找到当前页面 |
|shell getprop ro.build.version.release| 获取`platformVersion`版本号 |
|logcat| 获取日志信息 |
|devices| 查看当前所有已连接的设备 |


### appium api

|方法|模块|说明|
|---|---|---|
|start_activity|appium.webdriver.extensions.android.activities.Activities| [启动一个app](./scripts/0002-get-package-and-activity.py#L18) |
|current_activity|appium.webdriver.extensions.android.activities.Activities| [获取当前界面名](./scripts/0002-get-package-and-activity.py#L28) |
|current_package|appium.webdriver.extensions.android.common.Common| [获取当前包名](./scripts/0002-get-package-and-activity.py#L23) |
|terminate_app|appium.webdriver.extensions.applications.Applications| [关闭一个app](./scripts/0003-terminate-app.py#L23) |
|is_app_installed|appium.webdriver.extensions.applications.Applications| [检查app是否已安装](./scripts/0004-install-app.py#L12) |
|install_app|appium.webdriver.extensions.applications.Applications| [安装一个app](./scripts/0004-install-app.py#L24) |
|remove_app|appium.webdriver.extensions.applications.Applications| [卸载一个app](./scripts/0004-install-app.py#L17) |
|query_app_state|appium.webdriver.extensions.applications.Applications| [查询一个app的状态](scripts/0005-app-state-and-background.py#L20) |
|background_app|appium.webdriver.extensions.applications.Applications| [长按 `Home` 键, 将app放置后台(单位: 秒), 然后再回到屏幕前](scripts/0005-app-state-and-background.py#L26) |


