#!/usr/bin/python
import parse
from inspect import currentframe, getframeinfo

def get_location():
    cf = currentframe()
    return cf.f_back.f_lineno,getframeinfo(cf).filename

def run_test():
    tokens,tree = parse.parse(['(', 'defun', 'fn', '(', 'a', ')', '(', '+', 'a', 42, ')', ')'])
    if tokens != [] or tree != [['defun', 'fn', ['a'], ['+', 'a', 42]]]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    tokens,tree = parse.parse([])
    if tokens != [] or tree != []:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    tokens,tree = parse.parse(["a"])
    if tokens != [] or tree != ["a"]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

#   tokens,tree = parse.parse(["a",")","b"])
#   print tree
#   print tokens
#   if tokens != [] or tree != ["a"]:
#       print "Error on line ",get_location()[0],"in", get_location()[1]

#############################################################

    tree = parse.quote(["'","abc"])
    if tokens != [] or tree != [["quote","abc"]]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    tree = parse.quote(["'",["abc"]])
    if tokens != [] or tree != [["quote",["abc"]]]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    tree = parse.quote([])
    if tokens != [] or tree != []:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    tree = parse.quote(["'","'"])
    if tokens != [] or tree != [['quote', "'"]]:
        print "Error on line ",get_location()[0],"in", get_location()[1]



if __name__ == "__main__":
  run_test()
