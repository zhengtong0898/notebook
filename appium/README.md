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
|find_element_by_id|selenium.webdriver.remote.webdriver.WebDriver| [对应于: resource-id 标签](scripts/0006-find-element-by.py#L26) |
|find_element_by_class_name|selenium.webdriver.remote.webdriver.WebDriver| [对应于: class 标签](scripts/0006-find-element-by.py#L36) |
|find_element_by_xpath|selenium.webdriver.remote.webdriver.WebDriver| [按 xpath 规则查找元素](scripts/0006-find-element-by.py#L37) |
|find_element_by_css_selector|selenium.webdriver.remote.webdriver.WebDriver| [按 css_selector 规则查找元素](scripts/0006-find-element-by.py#L38) |
|click|appium.webdriver.webelement.WebElement| [点击控件](scripts/0006-find-element-by.py#L26) |
|send_key|appium.webdriver.webelement.WebElement| [输入内容](scripts/0006-find-element-by.py#L31) |
|get_attribute|appium.webdriver.webelement.WebElement| [获取当前组件的属性值](scripts/0007-get-attribute.py#L22) |
|swipe|[webdriver.extentions.action_helpers.ActionHelpers](https://github.com/appium/python-client/blob/master/appium/webdriver/extensions/action_helpers.py#L111)| [按象数, 有惯性, 支持滑动时长](scripts/0008-scroll.py#L39) |
|scroll|[webdriver.extentions.action_helpers.ActionHelpers](https://github.com/appium/python-client/blob/master/appium/webdriver/extensions/action_helpers.py#L31)| [按元素, 有惯性, 支持滑动时长](scripts/0008-scroll.py#L47) |
|drag_and_drop|[webdriver.extentions.action_helpers.ActionHelpers](https://github.com/appium/python-client/blob/master/appium/webdriver/extensions/action_helpers.py#L58)| [按元素, 无惯性, 不支持滑动时长](scripts/0008-scroll.py#L51) |
|TouchAction.tap|[webdriver.common.touch_action.TouchAction](https://github.com/appium/python-client/blob/master/appium/webdriver/common/touch_action.py#L43)| 轻微触碰, 支持坐标, 类似click |
|TouchAction.press|[webdriver.common.touch_action.TouchAction](https://github.com/appium/python-client/blob/master/appium/webdriver/common/touch_action.py#L66)| [按住](scripts/0009-touch-action.py#L40) |
|TouchAction.long_press|[webdriver.common.touch_action.TouchAction](https://github.com/appium/python-client/blob/master/appium/webdriver/common/touch_action.py#L89)| [长按](scripts/0009-touch-action.py#L32) |
|TouchAction.wait|[webdriver.common.touch_action.TouchAction](https://github.com/appium/python-client/blob/master/appium/webdriver/common/touch_action.py#L111)| [等待](scripts/0009-touch-action.py#L39) |
|TouchAction.move_to|[webdriver.common.touch_action.TouchAction](https://github.com/appium/python-client/blob/master/appium/webdriver/common/touch_action.py#L129)| [移动](scripts/0009-touch-action.py#L41) |
|TouchAction.release|[webdriver.common.touch_action.TouchAction](https://github.com/appium/python-client/blob/master/appium/webdriver/common/touch_action.py#L144)| [松开/释放](scripts/0009-touch-action.py#L46) |
|TouchAction.perform|[webdriver.common.touch_action.TouchAction](https://github.com/appium/python-client/blob/master/appium/webdriver/common/touch_action.py#L154)| [执行](scripts/0009-touch-action.py#L47) |


