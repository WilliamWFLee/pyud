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
import shutil
from typing import List

import pyud


def show_results(definitions: List[pyud.Definition]):
    showing = True
    index = 0
    while showing:
        definition = definitions[index]

        cols = shutil.get_terminal_size().columns
        heading_template = "{{:-^{}}}".format(cols)

        page_content = (
            heading_template.format(
                "Page {} of {}".format(index + 1, len(definitions))
            ),
            heading_template.format(
                "Showing definition for {!r}".format(definition.word)
            ),
            heading_template.format('Definition'),
            definition.definition,
            heading_template.format('Example'),
            definition.example,
        )
        page = "\n".join(page_content) + "\n"
        print(page)

        try:
            command = input("Options - (N)ext, (P)revious, (Q)uit: ")
        except EOFError:
            print()
            break
        if command.upper() == "Q":
            break
        elif command.upper() == "N":
            index = (index + 1) % len(definitions)
        elif command.upper() == "P":
            index = (index - 1) % len(definitions)


def define(parser, args):
    ud = pyud.Client()
    definitions = ud.define(args.term)
    show_results(definitions)


def add_define_args(subparser):
    parser = subparser.add_parser('define', help="Define a term")
    parser.set_defaults(func=define)

    parser.add_argument('term')


def parse_args():
    parser = argparse.ArgumentParser(
        prog='pyud',
        description="Command-line interface for the Urban Dictionary API",
    )
    parser.set_defaults(func=None)

    parser.add_argument(
        '--version',
        action='version',
        version="pyud {}".format(pyud.__version__),
    )

    subparser = parser.add_subparsers(metavar='subcommand')
    add_define_args(subparser)

    args = parser.parse_args()
    return parser, args


parser, args = parse_args()
if args.func is not None:
    args.func(parser, args)
else:
    parser.print_help()
