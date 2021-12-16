from appium import webdriver
from appium.webdriver.extensions.android.network import Network


driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",
                          desired_capabilities={"platformName": "Android"})


driver.implicitly_wait(10)


# 获取当前手机的网络模式, 同时发送三条指令
# adb.exe shell settings get global airplane_mode_on
# adb.exe shell settings get global wifi_on
# adb.exe shell settings get global mobile_data
#
# 返回结果
# Possible values:
# +--------------------+------+------+---------------+
# | Value (Alias)      | Data | Wifi | Airplane Mode |
# +====================+======+======+===============+
# | 0 (None)           | 0    | 0    | 0             |
# +--------------------+------+------+---------------+
# | 1 (Airplane Mode)  | 0    | 0    | 1             |
# +--------------------+------+------+---------------+
# | 2 (Wifi only)      | 0    | 1    | 0             |
# +--------------------+------+------+---------------+
# | 4 (Data only)      | 1    | 0    | 0             |
# +--------------------+------+------+---------------+
# | 6 (All network on) | 1    | 1    | 0             |
# +--------------------+------+------+---------------+
network_map = {0: None,
               1: "Airplane",
               2: "Wifi only",
               4: "Data only",
               6: "All network on"}
network_connection = driver.network_connection
assert network_connection == 6
assert network_map[network_connection] == network_map[6]


# 更改手机网络模式为 "Data only"
driver.set_network_connection(4)
network_connection = driver.network_connection
assert network_connection == 4
assert network_map[network_connection] == network_map[4]
print(network_connection, network_map[network_connection])


# toggle_wifi 指的是, 不管当前是什么网络类型, 当前操作只负责 wifi 这一项数据的 toggle.
# 场景-1: 假设 network-connection = 0(0-0-0); 执行 gogle_wifi() 后; network-connection = 2(0-1-0)
# 场景-2: 假设 network-connection = 1(0-0-1); 执行 gogle_wifi() 会报错, 因为不允许即是飞行模式的同时也是wifi模式.
# 场景-3: 假设 network-connection = 2(0-1-0); 执行 gogle_wifi() 后; network-connection = 0(0-0-0)
# 场景-4: 假设 network-connection = 4(1-0-0); 执行 gogle_wifi() 后; network-connection = 6(1-1-0)
# 场景-5: 假设 network-connection = 6(1-1-0); 执行 gogle_wifi() 后; network-connection = 4(1-0-0)
driver.toggle_wifi()
network_connection = driver.network_connection
assert network_connection == 6
assert network_map[network_connection] == network_map[6]
