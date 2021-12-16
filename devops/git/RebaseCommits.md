### 如何合并多个`commit`?

```shell
# 查看commits
$ git log
 
commit 470ad5948fbd3f8fce93a2674c640831eef19dd8 (HEAD -> main, origin/main, origin/HEAD)
Author: zhengtong0898 <zhengtong0898@aliyun.com>
Date:   Wed Oct 20 10:26:40 2021 +0800

    algorithms: Python源码剖析

commit d4d21baf8f34ae6d90d79f1807552793f363c19a
Author: zhengtong0898 <zhengtong0898@aliyun.com>
Date:   Wed Oct 20 07:51:54 2021 +0800

    algorithms: wz-course-week-1: essence-8

commit 48f6e9a9dcf290cf26bac5d778b60479ec7c5b0c
Author: zhengtong0898 <zhengtong0898@aliyun.com>
Date:   Tue Oct 19 07:15:12 2021 +0800

    algorithms: wz-course-week-1: code-review-4

commit d841f20740b551c625d84469e71dd2cb0315ea23
Author: zhengtong0898 <zhengtong0898@aliyun.com>
Date:   Mon Oct 18 13:39:46 2021 +0800

    algorithms: wz-course-week-1: code-review-3

commit 0d88e3d1227cc10bec15efad13946d3624bc7f05
Author: zhengtong0898 <zhengtong0898@aliyun.com>
Date:   Mon Oct 18 13:06:49 2021 +0800

    algorithms: wz-course-week-1: code-review-2


# 合并 
# 470ad5948fbd3f8fce93a2674c640831eef19dd8
# d4d21baf8f34ae6d90d79f1807552793f363c19a
# 48f6e9a9dcf290cf26bac5d778b60479ec7c5b0c
# d841f20740b551c625d84469e71dd2cb0315ea23
$ git rebase -i 0d88e3d1227cc10bec15efad13946d3624bc7f05

pick d841f20 algorithms: wz-course-week-1: code-review-3
squash 48f6e9a algorithms: wz-course-week-1: code-review-4
squash d4d21ba algorithms: wz-course-week-1: essence-8
squash 470ad59 algorithms: Python源码剖析

:wq!
```