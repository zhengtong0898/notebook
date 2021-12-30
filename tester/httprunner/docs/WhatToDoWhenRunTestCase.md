### httprunner框架的用例执行阶段在做什么?

```python3
import time
from typing import List

try:
    import allure

    USE_ALLURE = True
except ModuleNotFoundError:
    USE_ALLURE = False

from httprunner.client import HttpSession
from httprunner.loader import load_project_meta
from httprunner.parser import parse_variables_mapping
from httprunner.utils import merge_variables
from httprunner.models import VariablesMapping, StepData, TestCase



class HttpRunner(object):

    
    def test_start(self, param: Dict = None) -> "HttpRunner":
        
        ...
        
        try:
            testcase = TestCase(config=self.__config, teststeps=self.__teststeps)           # 入口从这里开始
            return self.run_testcase(testcase=testcase)
        finally:
            logger.remove(log_handler)
            logger.info(f"generate testcase log: {self.__log_path}")

    
    def run_testcase(self, testcase: TestCase) -> "HttpRunner":
        """run specified testcase

        Examples:
            >>> testcase_obj = TestCase(config=TConfig(...), teststeps=[TStep(...)])
            >>> HttpRunner().with_project_meta(project_meta).run_testcase(testcase_obj)

        """
        self.__config = testcase.config                                     # 在 test_start 中执行过, 冗余的代码
        self.__teststeps = testcase.teststeps                               # 在 test_start 中执行过, 冗余的代码

        # prepare
        self.__project_meta = self.__project_meta or load_project_meta(     # 在 test_start 中执行过, 冗余的代码
            self.__config.path
        )
        self.__parse_config(self.__config)                                  # 
        self.__start_at = time.time()
        self.__step_datas: List[StepData] = []
        self.__session = self.__session or HttpSession()
        # save extracted variables of teststeps
        extracted_variables: VariablesMapping = {}

        # run teststeps
        for step in self.__teststeps:
            # override variables
            # step variables > extracted variables from previous steps
            step.variables = merge_variables(step.variables, extracted_variables)
            # step variables > testcase config variables
            step.variables = merge_variables(step.variables, self.__config.variables)

            # parse variables
            step.variables = parse_variables_mapping(
                step.variables, self.__project_meta.functions
            )

            # run step
            if USE_ALLURE:
                with allure.step(f"step: {step.name}"):
                    extract_mapping = self.__run_step(step)
            else:
                extract_mapping = self.__run_step(step)

            # save extracted variables to session variables
            extracted_variables.update(extract_mapping)

        self.__session_variables.update(extracted_variables)
        self.__duration = time.time() - self.__start_at
        return self
```