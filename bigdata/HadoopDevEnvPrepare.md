### 开发环境准备
1. 安装 anaconda, [参考这里](https://docs.anaconda.com/anaconda/install/mac-os/)
2. 创建 venv 虚拟环境  
   ```shell
   $ mkdir ~/.conda/
   $ chmod -R 775 ~/.conda/ 
   $ conda create --name learn_staff python=3.7
   $ conda activate learn_staff
   $ conda install -c conda-forge libhdfs3
   ```
3. 替换 pycharm 的 venv 虚拟环境
   ```shell
   $ cd ~/PycharmProjects/learn_staff/
   
   $ pwd
   /Users/zt/PycharmProjects/learn_staff
   
   $ mv venv venv-bak
   $ ln -s 
   $ ln -s /Users/zt/opt/anaconda3/envs/learn_staff venv
   ```
4. 安装 hdfs3 库
   ```shell
   $ conda activate learn_staff
   $ pip3 install hdfs3
   $ pip3 install pyarrow
   ```
5. 连接 hdfs
   ```python3
   from hdfs3 import HDFileSystem

   hdfs = HDFileSystem(host="10.9.0.54", port=8020)
   s = hdfs.ls("/", detail=True)
   for i in s:
       i.pop("encryption_info")
       i.pop("last_access")
       i.pop("replication")
       i.pop("block_size")
       i.pop("size")
       i.pop("last_mod")
       print(i)


   # 输出
   {'kind': 'directory', 'name': '//app-logs', 'owner': 'yarn', 'group': 'hadoop', 'permissions': 1023}
   {'kind': 'directory', 'name': '//apps', 'owner': 'hdfs', 'group': 'hdfs', 'permissions': 493}
   {'kind': 'directory', 'name': '//ats', 'owner': 'yarn', 'group': 'hadoop', 'permissions': 493}
   {'kind': 'directory', 'name': '//atsv2', 'owner': 'hdfs', 'group': 'hdfs', 'permissions': 493}
   {'kind': 'directory', 'name': '//hdp', 'owner': 'hdfs', 'group': 'hdfs', 'permissions': 493}
   {'kind': 'directory', 'name': '//livy2-recovery', 'owner': 'livy', 'group': 'hdfs', 'permissions': 448}
   {'kind': 'directory', 'name': '//mapred', 'owner': 'mapred', 'group': 'hdfs', 'permissions': 493}
   {'kind': 'directory', 'name': '//mr-history', 'owner': 'mapred', 'group': 'hadoop', 'permissions': 511}
   {'kind': 'directory', 'name': '//ranger', 'owner': 'hdfs', 'group': 'hdfs', 'permissions': 493}
   {'kind': 'directory', 'name': '//spark2-history', 'owner': 'spark', 'group': 'hadoop', 'permissions': 511}
   {'kind': 'directory', 'name': '//tmp', 'owner': 'hdfs', 'group': 'hdfs', 'permissions': 511}
   {'kind': 'directory', 'name': '//user', 'owner': 'hdfs', 'group': 'hdfs', 'permissions': 493}
   {'kind': 'directory', 'name': '//warehouse', 'owner': 'hdfs', 'group': 'hdfs', 'permissions': 493}
   ```
6. 高价值参考链接  
   [用ApacheArrow加速PySpark](https://www.codercto.com/a/68911.html)   
   [pyarrow的效率提升（一）](https://zhuanlan.zhihu.com/p/117254592)  
