
1. 在 linux 服务器上生成公钥和密钥文件.
   ```shell
   [root@localhost ~]# mkdir ssh-key
   [root@localhost ~]# cd ssh-key
   [root@localhost ssh-key]# ssh-keygen -t rsa -N '' -f id_rsa
   [root@localhost ssh-key]# ls
   id_rsa  id_rsa.pub
   
   [root@localhost ssh-key]# cat id_rsa.pub
   ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDQAyBPzLEAkPFCpUoSVT+tybEplLiRLYqxgu6aijhKwI4VI7CoG7xws4PSJegjyRnnJYO6+2OcS
           exZUH1S6eGDP3D6m+nK2N2evMmh67Az+Urr9/aiPCNlLYfKBtDezeWjHoM/iPumigjJ/L8wQlNiQ2+8TNNYbiz+oeBHKXDWbCOHNxi43O
           K84nkqyFos9OKObmBYZW1fdoSOEnPQlNNJ34LT6iO7pTF2g9uxgKEWEPY9S+XofRVtzEzY3+Bd0YbxAC6+m9d7iByoRnASM3zXLcrtAZ2
           0rgXmtwhuC6OW0/ipTkxsA+U/Ca91iqOxTnWuwljXV3Zs2MtL/YlGtUe3 root@localhost.localdomain
   ```

2. 将公钥文本(id_rsa.pub)添加到jenkins-credentials中.   
   1). 复制公钥文本(id_rsa.pub).   
   2). 找到添加凭证位置: Manage Jenkins -> Security -> Manage Credentials -> Store scoped to Jenkins -> global   
   3). 进入添加凭证界面: Add credentials(菜单左侧)   
   4). 填写凭证信息.   
   