#!/usr/bin/python
import repl
import core
from inspect import currentframe, getframeinfo

def get_location():
    cf = currentframe()
    return cf.f_back.f_lineno,getframeinfo(cf).filename

def eval_test():
    results = repl.eval("1")
    if results != [1]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(+ 77 100")
    if results != [177]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(- 100 77)")
    if results != [23]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

######## CONS CAR CDR ##################
    results = repl.eval("(cons 1 '(2 3 4))")
    if results != [[1,2,3,4]]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(cons 1 '())")
    if results != [[1]]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(cons '(1 2) '(3))")
    if results != [[[1,2],3]]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(cons '(1 2) 3)")
    if results != [[[1,2],3]]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(car '((1) 2 (3)))")
    if results != [[1]]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(car '(1)")
    if results != [1]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(cdr '((1) 2 (3)))")
    if results != [[2,[3]]]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(list 1 2)")
    if results != [[1,2]]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(list 'a 'b)")
    if results != [["a","b"]]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(append '(1 2) '(3 4))")
    if results != [[1,2,3,4]]:
        print "Error on line ",get_location()[0],"in", get_location()[1]


######## DEFUN and LAMBDA TESTS ##################

    results = repl.eval("(defun tom () 42) (tom)")
    if results != ["tom",42]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(defun tom () (lambda (a b) (+ a b))) ((tom) 2 3) (tom)")
    if results != ["tom",5,('function', (["a","b"], ['+', 'a', 'b']))]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(funcall (lambda (x y) (+ x y)) 2 3)")
    if results != [5]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("((lambda () 42))")
    if results != [42]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("((lambda (a b) (+ a b)) 2 3)")
    if results != [5]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(defun tom (a b) (+ a b)) (funcall (function tom) 2 3)")
    if results != ["tom",5]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(defun fibonacci (n) (if (= n 0) 0 (if (= n 1) 1 (+ (fibonacci (- n 1)) (fibonacci (- n 2)))))) (fibonacci 10)")
    if results != ["fibonacci",55]:
        print "Error on line ",get_location()[0],"in", get_location()[1]
   
######## DEFPARAMETER TESTS ##################

    results = repl.eval("(defparameter xyz (+ 3 4)) xyz")
    if results != ["xyz",7]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(defparameter abc (lambda () 42)) abc")
    if results != ["abc",("function",([],42))]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

######## LET TESTS ##################

    results = repl.eval("(let ((a (+ 4 3)) (b (* 2 3))) (+ a b))")
    if results != [13]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

######## IF TESTS ##################

    results = repl.eval("(if 1 2 3)")
    if results != [2]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(if 0 2 3)")
    if results == [3]:
        print "This is weird on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(if '() 2 3)")
    if results != [3]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(if '(1) 2 3)")
    if results != [2]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(if (+ 1 2) (* 56 2) 7)")
    if results != [112]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(if (+ 1 2) (if t (car '(a b c d)) 7) 19)")
    if results != ["a"]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(if nil  (if t (car '(a b c d)) 7) 19)")
    if results != [19]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

######## FLET TESTS ##################

    results = repl.eval("(flet ((f (n) (+ n 10)) (g (n) (- n 3))) (g (f 5)))")
    if results != [12]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(flet ((factorial (n) (if (= n 1) 1 (* n (factorial (- n 1)))))) (factorial 6))")
    if results != [720]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(flet ((fibonacci1 (n) (if (= n 0) 0 (if (= n 1) 1 (+ (fibonacci1 (- n 1)) (fibonacci1 (- n 2))))))) (fibonacci1 18))")
    if results != [2584]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

######## DO TESTS ##################
    results = repl.eval("(do (+ 1 2) (* 77 1) (let ((a 5)) a))")
    if results != [5]:
        print "Error on line ",get_location()[0],"in", get_location()[1]
######## SETF TESTS ##################
    results = repl.eval("(let ((x 5) (y 6) (z 7)) (do (setf x (+ x 1)) (setf x (+ x 2)) x))")
    if results != [8]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

######## OR TESTS ##################
    results = repl.eval("(if (or nil '()) 1 2)")
    if results != [2]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(if (or 1 nil) 1 2)")
    if results != [1]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(if (or nil 1) 1 2)")
    if results != [1]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(if (or 1 1) 1 2)")
    if results != [1]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

######## AND TESTS ##################
    results = repl.eval("(if (and nil '()) 1 2)")
    if results != [2]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(if (and 1 nil) 1 2)")
    if results != [2]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(if (and nil 1) 1 2)")
    if results != [2]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

    results = repl.eval("(if (and 1 1) 1 2)")
    if results != [1]:
        print "Error on line ",get_location()[0],"in", get_location()[1]

if __name__ == "__main__":
  eval_test()

