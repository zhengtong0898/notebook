### nargs
读取多个参数并转换为列表格式.  
- nargs=`N`(要求指定数量的参数)  
  Example-1: 必须提供--foo参数, 并填写两个子参数.  
  ```python3
  import argparse
  
  
  parser = argparse.ArgumentParser()
  parser.add_argument('--foo', nargs=2, required=True)
  
  
  # 查看帮助文档: 
  parser.print_helper()
  # usage: argparsepra.py [-h] --foo FOO FOO
  # 
  # optional arguments:
  #   -h, --help     show this help message and exit
  #   --foo FOO FOO
  
  
  # 不提供任何参数: 将会报错 
  parser.parse_args([])
  # usage: argparsepra.py [-h] --foo FOO FOO
  # argparsepra.py: error: the following arguments are required: --foo
  
  
  # 仅提供一个子参数: 也会报错
  parser.parse_args(["--foo", "a"])
  # usage: argparsepra.py [-h] --foo FOO FOO
  # argparsepra.py: error: argument --foo: expected 2 arguments
  
  
  # 提供两个子参数: 没有报错
  args = parser.parse_args(["--foo", "a", "b"])
  print(args.foo)
  # ['a', 'b']
  ```
  
  Example-2: 为子参数增加提示说明
  ```python3
  import argparse 
  
  
  parser = argparse.ArgumentParser()
  parser.add_argument('--foo', nargs=2, metavar=("host", "port"),required=True)
  
  
  # 查看帮助文档: 将默认的 --foo FOO FOO , 替换成了 --foo host port
  parser.print_help()
  # usage: argparsepra.py [-h] --foo host port
  # 
  # optional arguments:
  #   -h, --help       show this help message and exit
  #   --foo host port
  
  
  # 由于增加了提示 host 和 port, 使用者更清楚的知道应该填什么.  
  args = parser.parse_args(["--foo", "192.168.1.100", "3306"])
  print(args.foo)
  # ['192.168.1.100', '3306']
  ```
  
- nargs=`*`(任意数量的子参数, 可为空)  
  ```python3
  import parser
  
  
  parser = argparse.ArgumentParser()
  parser.add_argument('--foo', nargs="*")
  
  
  # 查看帮助文档
  parser.print_help()
  # usage: argparsepra.py [-h] [--foo [FOO [FOO ...]]]
  # 
  # optional arguments:
  #   -h, --help            show this help message and exit
  #   --foo [FOO [FOO ...]]
  
  
  # 提供任意数量的子参数
  args = parser.parse_args(["--foo", "a", "b", "c"])
  print(args.foo)
  # ['a', 'b', 'c']
  ```


- nargs=`+`(任意数量的子参数, 至少提供一个)  

  ```python3
  import parser
  
  
  parser = argparse.ArgumentParser()
  parser.add_argument('foo', nargs='+')
  
  
  # 不提供任何参数: 将会报错
  args = parser.parse_args([])
  # usage: argparsepra.py [-h] foo [foo ...]
  # argparsepra.py: error: the following arguments are required: foo
  
  
  # 提供多个参数: 不会报错
  args = parser.parse_args(["--foo", "a", "b", "c"])
  print(args.foo)
  # ['a', 'b', 'c']
  ```


- nargs=`?`(仅取一个子参数, 可搭配default、const组合使用)

  Example-1: 提供多个子参数: 会报错
  ```python3
  import parser
  
  
  parser = argparse.ArgumentParser()
  parser.add_argument('--foo', nargs="?")
  
  
  # 查看帮助文档
  parser.print_help()
  # usage: argparsepra.py [-h] [--foo [FOO]]
  # 
  # optional arguments:
  #   -h, --help   show this help message and exit
  #   --foo [FOO]
  
  
  # 提供多个子参数: 会报错
  parser.parse_args(["--foo", "a", "b"])
  # usage: argparsepra.py [-h] [--foo [FOO]]
  # argparsepra.py: error: unrecognized arguments: b
  ```
  
  Example-2: 不提供父参数, 采用default值
  ```python3
  import parser
  
  
  parser = argparse.ArgumentParser()
  parser.add_argument('--foo', nargs="?", default="aaa")
  
  
  # 不提供任何参数
  args = parser.parse_args([])
  print(args.foo)
  # 采用default值
  # aaa
  ```
  
  Example-3: 提供父参数, 不提供子参数, 采用const值
  ```python3
  import parser
  
  
  parser = argparse.ArgumentParser()
  parser.add_argument('--foo', nargs="?", const="bbb", default="aaa")
  
  
  # 不提供子参数值
  args = parser.parse_args(["--foo"])
  print(args.foo)
  # 采用const值
  # bbb
  
  
  # 提供子参数值
  args = parser.parse_args(["--foo", "zzz"])
  print(args.foo)
  # 采用提供的子参数的值
  # zzz
  ```