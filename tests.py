#!/usr/bin/env python3
from __future__ import print_function
import os, sys
import pytest
path = '.'
if len(sys.argv) == 2:
	path = sys.argv[1]

files = os.listdir(path)
for name in files:
	full_path = os.path.join(path, name)
	if os.path.isfile(full_path):
		if len(name.split('.')) == 2 and name.split('.')[1] == 'py' and name != "tests.py":
			print("Unittest commences for {}".format(full_path))
			pytest.main(['-x', full_path])
