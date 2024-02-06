import inspect
import importlib.util


class ModuleLoader:

    @staticmethod
    def load(path):
        module_name = inspect.getmodulename(path)
        spec = importlib.util.spec_from_file_location(module_name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
