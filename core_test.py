#!/usr/bin/python
import core
from inspect import currentframe, getframeinfo

def get_location():
    cf = currentframe()
    return cf.f_back.f_lineno,getframeinfo(cf).filename

def run_test():
    if 1 != 1:
        print "Error on line ",get_location()[0],"in", get_location()[1]

if __name__ == "__main__":
  run_test()
