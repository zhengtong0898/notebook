### httprunner框架的用例准备阶段在做什么?  

```python3
import os
import uuid
from typing import Dict

from httprunner.models import (
    ProjectMeta,
)

from loguru import logger


try:
    import allure

    USE_ALLURE = True
except ModuleNotFoundError:
    USE_ALLURE = False


class HttpRunner(object):

    __project_meta: ProjectMeta = None
    
    def test_start(self, param: Dict = None) -> "HttpRunner":
        """main entrance, discovered by pytest"""
        self.__init_tests__()                                                     # 已分析过, 忽略
        self.__project_meta = self.__project_meta or load_project_meta(           # 加载 debugtalk.py 中的方法.
            self.__config.path
        )
        self.__case_id = self.__case_id or str(uuid.uuid4())                      # 用例、子用例、参数化用例, 共用一个uuid.
        self.__log_path = self.__log_path or os.path.join(                        # 定义日志路径.
            self.__project_meta.RootDir, "logs", f"{self.__case_id}.run.log"
        )
        log_handler = logger.add(self.__log_path, level="DEBUG")                  # 定义日志级别和日志句柄

        # parse config name
        config_variables = self.__config.variables                                # 这个段落代码的目的是, 解析 config.name
        if param:                                                                 # 当 config.name 中包含变量引用、函数调用  
            config_variables.update(param)                                        # 将变量转换成值, 并执行函数调用, 
        config_variables.update(self.__session_variables)                         # 最终将结果再次拼接成字符串,
        self.__config.name = parse_data(                                          # 重新赋值给 self.__config.name
            self.__config.name, config_variables, self.__project_meta.functions   # TODO: 后面有空重点分析和学习这块代码.  
        )

        if USE_ALLURE:                                                            # TODO: 作用待补充
            # update allure report meta
            allure.dynamic.title(self.__config.name)
            allure.dynamic.description(f"TestCase ID: {self.__case_id}")

        logger.info(
            f"Start to run testcase: {self.__config.name}, TestCase ID: {self.__case_id}"
        )
        
        try:                                                                      # 上面都是准备阶段, 下面是执行测试用例阶段.
            return self.run_testcase(                                             # 这里不是本文重点, 不展开说明.
                TestCase(config=self.__config, teststeps=self.__teststeps)
            )
        finally:
            logger.remove(log_handler)
            logger.info(f"generate testcase log: {self.__log_path}")


```