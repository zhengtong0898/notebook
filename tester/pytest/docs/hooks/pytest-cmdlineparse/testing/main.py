import pytest
from cmdlineparse.plugin import CmdLineParse


if __name__ == '__main__':
    pytest.main(["-s"], plugins=[CmdLineParse()])
