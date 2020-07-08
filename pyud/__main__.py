# -*- coding: utf-8 -*-
"""
pyud.__main__
Copyright (c) 2020 William Lee

This file is part of pyud.

pyud is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyud is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pyud.  If not, see <https://www.gnu.org/licenses/>.
"""

import argparse

import pyud


def define(parser, args):
    pass


def add_define_args(subparser):
    parser = subparser.add_parser('define', help="Define a term")
    parser.set_defaults(func=define)

    parser.add_argument('term')


def parse_args():
    parser = argparse.ArgumentParser(
        prog='pyud',
        description="Command-line interface for the Urban Dictionary API",
    )
    parser.add_argument(
        '--version',
        action='version',
        version="pyud {}".format(pyud.__version__)
    )

    subparser = parser.add_subparsers(metavar='subcommand')
    add_define_args(subparser)

    args = parser.parse_args()
    return parser, args


parser, args = parse_args()
if hasattr(args, 'func'):
    args.func(parser, args)
else:
    parser.print_help()
