#!/usr/bin/env python
# coding=utf-8

import os
import sys

m = sys.argv[1]

origin = 'origin'
branch = 'main'
os.system('git add .; git status')
os.system('git commit -m ' + m)
os.system('git push ' + origin + ' ' + branch)

