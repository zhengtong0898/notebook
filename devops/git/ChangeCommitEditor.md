### 选择编辑器引擎  

在 `ubuntu` 操作系统中, `git commit --amend` 默认使用的是 `nano` 编辑器引擎.  
要将编辑器引擎变更为`vim`, 需要对 `git` 的配置做一下调整:  
```shell
$ git config --global core.editor "vim"
```

[参考资料](https://www.codegrepper.com/code-examples/shell/change+git+commit+editor+to+vim)