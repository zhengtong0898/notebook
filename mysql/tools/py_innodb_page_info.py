from sys import argv
from mysql.tools.libs.mylib import myargv, get_innodb_page_type


if __name__ == '__main__':
    myargv = myargv(argv)
    if myargv.parse_cmdline() == 0:
        pass
    else:
        print()
        get_innodb_page_type(myargv)
