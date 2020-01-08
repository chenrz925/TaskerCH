from typing import Text, Type


def import_class(module_name: Text, class_name: Text, base_class: type = None) -> Type:
    module = __import__(module_name)
    if not hasattr(module_name, class_name) and '.' in module_name:
        paths = module_name.split('.')[1:]
        for sub_path in paths:
            module = getattr(module, sub_path)
    clazz = getattr(module, class_name)
    if base_class is not None:
        if not issubclass(clazz, base_class):
            raise RuntimeError()
    return clazz
