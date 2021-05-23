### 语言切换

1. 找到 'locale' 插件:   
   系统管理(在左侧菜单树) -> 系统管理 -> 插件管理 -> 可选插件 -> 搜索关键字'locale'.

2. 安装 'locale' 插件:  
   点击 checkbox , 勾选 'Locale' 插件;  
   点击 Download now and install after restart 按钮;

3. 到 linux 操作系统中, 重启 jenkins 服务.    
   ```shell
   /etc/init.d/jenkins restart
   ```

4. 将语言设定为英文  
   找到: 系统管理(在左侧菜单树) -> 系统配置 -> 系统配置 -> Locale   
   在 Default Language 处, 填写 'en_US', 点击保存, jenkins 将切换到英文模式.   
   在 Default Language 处, 填写 'zh_CN', 点击保存, jenkins 将切换到英文模式.   
   备注: 需要勾选 'Ignore browser preference and force this language to all users' 这个 Checkbox .   
 
