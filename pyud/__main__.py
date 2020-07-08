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

parser = argparse.ArgumentParser(
    prog='pyud',
    description="Command-line interface for the Urban Dictionary API",
)

parser.add_argument(
    '--version', action='version', version="pyud {}".format(pyud.__version__)
)

parser.parse_args()
