import re
import sys
from httprunner.cli import main


if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.argv.append("run")
    sys.argv.append("--verbose")
    sys.argv.append("workflow-create-user.yml")
    print(sys.argv)
    sys.exit(main())
