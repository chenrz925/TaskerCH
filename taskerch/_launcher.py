# -*- coding: utf-8 -*-
# Copyright 2019-2020 Chen Runze. All Rights Reserved.
#
# This Source Code Form is subject to the terms of the
# Apache License Version 2.0. If a copy of the Apache
# License was not distributed with this file, You can
# obtain one at http://www.apache.org/licenses/LICENSE-2.0.

from argparse import ArgumentParser
from sys import argv as sys_argv, stdout as io_stdout
from typing import NoReturn, Text, Callable, List

from ._dependency import Configuration, ConfigurationCreator
from ._dependency import __version__


class Launcher(Callable):
    def _init_argparse(self) -> ArgumentParser:
        parser = ArgumentParser(
            prog='taskerch',
            description='A scalable and extendable experiment task scheduler framework.',
        )
        parser.add_argument(
            'command',
            nargs='?',
            default='help',
            choices=(
                'help',
                'launch',
                'example',
            )
        )
        parser.add_argument(
            '-v', '--version',
            action='version',
            version=f'%(prog)s {__version__}',
        )
        parser.add_argument(
            '-c', '--configuration',
            help='path of configuration file to launch',
            action='store',
            nargs='?',
            default=None,
            type=Text,
            required=False,
        )
        parser.add_argument(
            '-m', '--meta-configuration',
            help='path of meta configuration file to make example configuration',
            action='store',
            nargs='?',
            default=None,
            type=Text,
            required=False,
        )
        parser.add_argument(
            '-o', '--output',
            help='path of output file',
            action='store',
            nargs='?',
            default=None,
            type=Text,
            required=False,
        )
        return parser

    def _init_logging_handler(self, config: Configuration):
        pass

    def _launch_method(self, config: Configuration or List[Configuration]) -> Callable[[], NoReturn]:
        def _func():
            pass

        return _func

    def _example_method(self, meta: Configuration or List[Configuration], output: Text) -> Callable[[], NoReturn]:
        def _func():
            pass

        return _func

    def _help_method(self, parser: ArgumentParser) -> Callable[[], NoReturn]:
        def _func():
            parser.print_help(io_stdout)

        return _func

    def __init__(self, *args: Text):
        parser = self._init_argparse()
        cli_commands = parser.parse_args(args if args else sys_argv[1:])
        if cli_commands.command == 'help':
            self._method = self._help_method(parser)
        elif cli_commands.command == 'launch':
            configuration_path = cli_commands.configuration
            if configuration_path is None:
                parser.print_usage(io_stdout)
                print(
                    f'{parser.prog}: error: configuration not provided (set configuration by \'-c\' or '
                    f'\'--configuration\')'
                )
                exit(1)
            else:
                configuration = ConfigurationCreator(configuration_path).create()
                self._method = self._launch_method(configuration)
        elif cli_commands.command == 'example':
            meta_configuration_path: Text = cli_commands.meta_configuration
            if meta_configuration_path is None:
                parser.print_usage(io_stdout)
                print(
                    f'{parser.prog}: error: meta-configuration not provided (set configuration by \'-m\' or '
                    f'\'--meta-configuration\')'
                )
                exit(1)
            else:
                meta_configuration = ConfigurationCreator(meta_configuration_path).create()
                output = cli_commands.output
                if output is None:
                    if meta_configuration_path.endswith('.toml'):
                        output = meta_configuration_path[:-5] + '.example.toml'
                    else:
                        output = meta_configuration_path + '.example'
                self._method = self._example_method(meta_configuration, output)

    def __call__(self) -> NoReturn:
        self._method()
