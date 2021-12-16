### 如何将`A分支的某个commit`合并到`B分支`?

```shell
# 查看所有分支
$ git branch --list
  branch_b
* main

# 分别查看两个分支的commit
$ git log -5 --pretty=format:"%h"             # main 分支
470ad59
d4d21ba
48f6e9a
d841f20
0d88e3d

$ git checkout branch_b
$ git log -5 --pretty=format:"%h"             # branch_b 分支
470ad59

# 将 main 分支的 d841f20 合并到 branch_b 分支
$ git checkout branch_b
$ git cherry-pick d841f20
```