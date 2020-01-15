#!/usr/bin/python
import tokenization
from inspect import currentframe, getframeinfo

def get_location():
    cf = currentframe()
    return cf.f_back.f_lineno,getframeinfo(cf).filename

def run_test():

    tokens = tokenization.tokenize("(defun fn (a) (+ a 42))")
    if tokens != ['(', 'defun', 'fn', '(', 'a', ')', '(', '+', 'a', 42, ')', ')']:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    tokens = tokenization.tokenize("abc \"this is a literal\" def")
    if tokens != ["abc", "this is a literal","def"]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    tokens = tokenization.tokenize("  abc 1 53.5 cc(g b)a   'def"  )
    if tokens != ["abc", 1,53.5,"cc","(","g","b",")","a","'","def"]:
        print tokens
        print "Error on line ",get_location()[0],"in", get_location()[1]

if __name__ == "__main__":
  run_test()
