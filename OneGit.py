#!/usr/bin/env python
# coding=utf-8

import os
import argparse

# parser = argparse.ArgumentParser(description='Your commit -m')
# parser.add_argument('e')
# m = str(parser.parse_args())
origin = 'origin'
branch = 'main'
os.system('git add .; git status')
os.system('git commit -m ' + 'test')
os.system('git push ' + origin + ' ' + branch)
