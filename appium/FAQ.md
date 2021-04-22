### Unable to find an active device or emulator with OS 11
报错原因是: "platformVersion" 参数值 于实际的手机或模拟器的Android版本不一致. 

&nbsp;  
&nbsp;  
### 如何设置 android_home 和 java_home ?
1. `android_home` 填写的是 `Android SDK` 的路径.
2. `java_home` 可以填写 `jre` 的路径.   
![android_home_and_java_home](./imgs/android_home_and_java_home.jpg)   


&nbsp;  
&nbsp;  
### 找不到 mFocusedApp
一般情况下使用: `adb shell dumpsys window windows` 指令, 可以列出当前`包名`和`界面名`.   
然而`Android Q`版本的窗体响应中不再包含`mFocusedApp`信息, 解决办法是:  
`adb shell dumpsys window displays | grep -i "mFocusedApp"`   
