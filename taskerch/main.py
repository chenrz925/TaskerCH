#! env python
from typing import Any, Text, Dict
from traceback import print_exc
from argparse import ArgumentParser
from toml import load as toml_load
from datetime import datetime


def main(config: Dict[Text, Any]):
    if '_name_' in config:
        config_name_value = config['_name_']
    else:
        raise RuntimeError(
            '''Tag "_name_" MUST be defined in TOML configuration file.'''
        )

    if '_version_' in config:
        config_version_value = config['_version_']
    else:
        raise RuntimeError(
            '''Tag "_version_" MUST be defined in TOML configuration file.'''
        )
    debug = config['_debug_']
    print(config_name_value)
    print('Version', config_version_value)
    print()

    if '_meta_' not in config:
        raise RuntimeError(
            '''Tag "_meta_" MUST be defined in TOML configuration file.'''
        )
    elif not isinstance(config['_meta_'], list) or len(config['_meta_']) == 0:
        raise RuntimeError(
            '''Tag "_meta_" MUST has ONE members at least in configuration file.'''
        )
    else:
        shared = {}
        for meta in config['_meta_']:
            try:
                module_value = meta['module']
                class_value = meta['class']
                name_value = meta['name']
                execute_value = meta['execute'] if 'execute' in meta else True
            except KeyError:
                raise KeyError('module', 'class', 'name')
            if not execute_value:
                continue
            require_value = meta['require'] if 'require' in meta else []
            for key in require_value:
                if key not in shared:
                    raise RuntimeError(f'Task "{name_value}" require "{key}" in shared data, but not found')
            try:
                module = __import__(module_value)
                if not hasattr(module, class_value) and '.' in module_value:
                    paths = module_value.split('.')[1:]
                    for sub_path in paths:
                        module = getattr(module, sub_path)
                clazz = getattr(module, class_value)
                print(f'Launch task "{name_value}":')
            except Exception:
                raise RuntimeError(
                    f'Wrong reference in "{name_value}", check your class or module reference and fix it.')
            if not issubclass(clazz, AbstractTask):
                raise RuntimeError(
                    f'Wrong reference in "{name_value}", make sure your class is an implement of AbstractTask.')
            start_time = datetime.now()
            try:
                print('↓' * 40)
                task_config = config[name_value] if name_value in config else {}
                clazz(task_config, shared)()
            except Exception as e:
                print_exc()
                if debug:
                    raise e
            finally:
                print('↑' * 40)
            end_time = datetime.now()
            duration = end_time - start_time
            print(f'Finished after {duration.total_seconds()} seconds.')
            print()


if __name__ == '__main__':
    parser = ArgumentParser(
        description='Transportation mode detection with auto-encoder.',
    )
    parser.add_argument(
        '--configuration', '-c',
        help='Configuration file to launch.',
        nargs=1,
        required=True,
        type=str
    )
    namespace = parser.parse_args()
    main(toml_load(namespace.configuration))
