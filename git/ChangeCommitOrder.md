### 如何调整 `commit` 顺序?
1. 查看当前 `commit` 日志
```shell
$ git log

commit e71bbe67cbb107665b2fda3f800b28e5aaf52a15 (HEAD -> main, origin/main, origin/HEAD)
Author: zhengtong0898 <zhengtong0898@aliyun.com>
Date:   Fri Oct 8 13:57:25 2021 +0800

    algorithms: wz-course-week-1

commit 3ddc369d83e1f3eccc4a43988a1253beba558a79
Author: zhengtong0898 <zhengtong0898@aliyun.com>
Date:   Fri Oct 8 10:54:16 2021 +0800

    git: how to modify committed message?

commit 5566d540c4a50fc13fb832d1fb9a0859ee5f6e5f
Author: zhengtong0898 <zhengtong0898@aliyun.com>
Date:   Thu Oct 7 16:39:54 2021 +0800

    add Big-O-Complexity-Chart

commit bd4cbbee793f32c85d6ca2d6205a3ae444f79efe
Author: zhengtong0898 <zhengtong0898@aliyun.com>
Date:   Wed Sep 29 03:50:27 2021 +0800

    layout tips
```

2. 调整 `commit` 顺序   
将 `algorithms: wz-course-week-1` 和 `git: how to modify committed message?` 这两个 `commit` 顺序替换一下.
```shell
$ git rebase -i 5566d540c4a50fc13fb832d1fb9a0859ee5f6e5f

# 将这两个 pick 调换一下位置, 下面这个是原始记录
pick 3ddc369 git: how to modify committed message?
pick e71bbe6 algorithms: wz-course-week-1
# 变更为
pick e71bbe6 algorithms: wz-course-week-1
pick 3ddc369 git: how to modify committed message?
# 然后 :wq 保存并退出.

# 这里需要强制推送到 forked 仓库才算完成了更改.
$ git push --force
```

3. 查看调整后的结果
```shell
commit 8a5b479a2b8025e509e4cdc27fde4f363466d268 (HEAD -> main, origin/main, origin/HEAD)
Author: zhengtong0898 <zhengtong0898@aliyun.com>
Date:   Fri Oct 8 10:54:16 2021 +0800

    git: how to modify committed message?

commit c730938c64842ffbc68696ace30191e57143accd
Author: zhengtong0898 <zhengtong0898@aliyun.com>
Date:   Fri Oct 8 13:57:25 2021 +0800

    algorithms: wz-course-week-1

commit 5566d540c4a50fc13fb832d1fb9a0859ee5f6e5f
Author: zhengtong0898 <zhengtong0898@aliyun.com>
Date:   Thu Oct 7 16:39:54 2021 +0800

    add Big-O-Complexity-Chart

commit bd4cbbee793f32c85d6ca2d6205a3ae444f79efe
Author: zhengtong0898 <zhengtong0898@aliyun.com>
Date:   Wed Sep 29 03:50:27 2021 +0800

    layout tips
```


&nbsp;  
&nbsp;  
### 附加案例  
如何将 `5566d540c4a50fc13fb832d1fb9a0859ee5f6e5f` 这个 `commit message` 的 `add Big-O-Complexity-Chart` 改为 `add Big-O-Complexity-Chart amend` ?

1. 调整顺序, 将 `5566d540c4a50fc13fb832d1fb9a0859ee5f6e5f` 调整到最上方(即: 它是 head).  
```shell
$ git rebase -i bd4cbbee793f32c85d6ca2d6205a3ae444f79efe

# 将 5566d54 挪到最下面(表示它将变为 head)
pick 5566d54 add Big-O-Complexity-Chart
pick c730938 algorithms: wz-course-week-1
pick 8a5b479 git: how to modify committed message?
# 变更为
pick c730938 algorithms: wz-course-week-1
pick 8a5b479 git: how to modify committed message?
pick 5566d54 add Big-O-Complexity-Chart

# 然后 :wq 保存并退出.
```
2. 修改代码的 `message`.
```shell
$ git commit --amend

# message
add Big-O-Complexity-Chart
# 变更为
add Big-O-Complexity-Chart amend

# 然后 :wq 保存并退出.

```
3. 恢复原来的顺序
```shell
$ git rebase -i bd4cbbee793f32c85d6ca2d6205a3ae444f79efe

pick c730938 algorithms: wz-course-week-1
pick 8a5b479 git: how to modify committed message?
pick 5566d54 add Big-O-Complexity-Chart
# 变更为
pick 5566d54 add Big-O-Complexity-Chart
pick c730938 algorithms: wz-course-week-1
pick 8a5b479 git: how to modify committed message?

# 然后 :wq 保存并退出.

# 这里需要强制推送到 forked 仓库才算完成了更改.
$ git push --force
```
4. 查看最终效果   
验收条件:   
1). commit 顺序保持不变.  
2). `5566d540c4a50fc13fb832d1fb9a0859ee5f6e5f` 的 `commit message` 追加 `amend` 字符串.
```shell
commit 06155b4fc876b81541f312048007160a85c33a3a (HEAD -> main)
Author: zhengtong0898 <zhengtong0898@aliyun.com>
Date:   Fri Oct 8 10:54:16 2021 +0800

    git: how to modify committed message?

commit ccb432db56c0f0b2e01ba8787edf8bc1ea251ccf
Author: zhengtong0898 <zhengtong0898@aliyun.com>
Date:   Fri Oct 8 13:57:25 2021 +0800

    algorithms: wz-course-week-1

commit fee08c27ac5300761d42398ea2f197168b12707f
Author: zhengtong0898 <zhengtong0898@aliyun.com>
Date:   Thu Oct 7 16:39:54 2021 +0800

    add Big-O-Complexity-Chart amend

commit bd4cbbee793f32c85d6ca2d6205a3ae444f79efe
Author: zhengtong0898 <zhengtong0898@aliyun.com>
Date:   Wed Sep 29 03:50:27 2021 +0800

    layout tips
```