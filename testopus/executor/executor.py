from datetime import datetime
import inspect

from testopus.loader.module_loader import ModuleLoader
from testopus.logger.logger import logger
from testopus.loader.test_case_model import TOTestCase, TOTest
from testopus.executor.test_result import TOTestResultHandler
from testopus.utils.decorators import SkipException, FailureExpectedException


class TestExecutor:

    def run(self, test_suit: [TOTestCase]):
        logger.info(f"Test execution started at {datetime.now()}.")
        handler = TOTestResultHandler()

        for test_case in test_suit:
            for test in test_case.tests:
                module = ModuleLoader.load(test_case.path)

                if test.is_member_of_class():
                    self.__execute_obj_method(module, test, handler)
                else:
                    self.__execute_func(module, test, handler)

        logger.info(f"Test execution ended at {datetime.now()}.")

        return handler.get_report_model()

    @staticmethod
    def __execute_func(obj, test: TOTest, handler: TOTestResultHandler):
        func = getattr(obj, test.name, None)

        try:
            handler.start_test_run()
            func()
        except SkipException:
            handler.add_skip(test.get_description())
            return
        except FailureExpectedException as err:
            handler.add_expected_failure(test.get_description(), err)
            return
        except Exception as err:
            handler.add_error(test.get_description(), err)
            return

        handler.add_success(test.get_description())

    def __execute_obj_method(self, module, test: TOTest, handler):
        for _, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                try:
                    instance = obj()
                except TypeError as type_error:
                    logger.error(
                        f"Failed to instantiate a class object {repr(obj)} {type_error}")
                    continue

                if hasattr(instance, test.name) and callable(getattr(instance, test.name)):
                    self.__execute_func(instance, test, handler)