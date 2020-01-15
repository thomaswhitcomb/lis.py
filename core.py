#!/usr/bin/python
import sys
import time
import copy

TRUE = "t"
FALSE = "nil"

FUNCTION="function"

def reset_state():
  functions={}
  system_dictionary={}

#Map the LISP datum to a truth
def truth(b):
  if type(b) is list:
      if len(b) != 0:
          return 1
      else:
          return 0
  else:
    if b != FALSE:
        return 1
    else:
        return 0

def quit():
    sys.exit()

def or_(env,c1,c2):
    b1 = evaluate(env,c1)
    if b1 != FALSE:
        return TRUE

    b2 = evaluate(env,c2)
    if b2 != FALSE:
        return TRUE
    else:
        return FALSE

def and_(env,c1,c2):
    b1 = evaluate(env,c1)
    if b1 == FALSE:
        return FALSE

    b2 = evaluate(env,c2)
    if b2 != FALSE:
        return TRUE
    else:
        return FALSE

def equal(c1,c2):
    if c1 == c2:
        return TRUE
    else:
        return FALSE

def plus(t1,t2):
    return t1 + t2

def multiply(t1,t2):
    return t1 * t2

def subtract(t1,t2):
    return t1 - t2

def divide(t1,t2):
    return t1 / t2

def defparameter(env,n,s):
    system_dictionary[n] = evaluate(env,s)
    return n

def funcall(env,*args):
    if args[0][0] == FUNCTION:
        formal_args,form = args[0][1]
        i=0
        for arg in args[1:]:
            var = formal_args[i]
            i=i+1
            env[var] = evaluate(env,arg)
        return evaluate(env,form)
    else:
        raise "funcall received non function"

def cdr(l):
    if type(l) is not list:
        raise "Bad cdr"
    return l[1:]

def cons(a,l):
    if type(l) is not list:
        return [a,l]
    return [a]+l

def car(l):
    if type(l) is not list:
        raise "Bad cdr"
    return l[0]

def list_(a1,a2):
    if type(a1) is list or type(a2) is list:
        raise "A list not allowed on list()"
    return [a1,a2]

def append(l1,l2):
    if type(l1) is not list or type(l2) is not list:
        raise "Append requires two lists"
    return l1+l2

primitives = {
            "quit" : lambda e    : quit(),
               "=" : lambda e,*p : equal(*p),
               "+" : lambda e,*p : plus(*p),
               "*" : lambda e,*p : multiply(*p),
               "-" : lambda e,*p : subtract(*p),
               "/" : lambda e,*p : divide(*p),
              "or" : lambda e,*p : or_(e,*p),
             "and" : lambda e,*p : and_(e,*p),
         "funcall" : lambda e,*p : funcall(e,*p),
             "car" : lambda e,*p : car(*p),
             "cdr" : lambda e,*p : cdr(*p),
            "cons" : lambda e,*p : cons(*p),
            "list" : lambda e,*p : list_(*p),
          "append" : lambda e,*p : append(*p),
}


def setf(env,v,s):
    x = evaluate(env,s)
    env[v] = x
    return x

def do(env,*parms):
    for p in parms:
        x = evaluate(env,p)
    return x

def quote(t):
    return t

def defun(name,formal_parameters,form):
    functions[str(name)] = (formal_parameters,form)
    return str(name)

def lambda_(formal_parameters,form):
    return (FUNCTION,(formal_parameters,form))

def function(name):
    return (FUNCTION, functions[str(name)])

def let_(env,var_dcl,body):
    for t in var_dcl:
        env[t[0]] = evaluate(env,t[1])
    return evaluate(env,body)

def if_(env,cond,then_sexp,else_sexp):
    b = evaluate(env,cond)
    if truth(b):
        return evaluate(env,then_sexp)
    else:
        return evaluate(env,else_sexp)

def flet(env,fns,body):
    for f in fns:
        env[f[0]] = lambda_(f[1],f[2])
    return evaluate(env,body)

functions = {
}

# Substitutions not performed
special_forms = {
             "flet" : lambda e,*p : flet(e,*p),
         "function" : lambda e,*p : function(*p),
            "quote" : lambda e,*p : quote(*p),
             "setf" : lambda e,*p : setf(e,*p),
               "do" : lambda e,*p : do(e,*p),
            "defun" : lambda e,*p : defun(*p),
     "defparameter" : lambda e,*p : defparameter(e,*p),
               "if" : lambda e,*p : if_(e,*p),
           "lambda" : lambda e,*p : lambda_(*p),
               "let": lambda e,*p : let_(e,*p),
        }

system_dictionary = {
        "t" : TRUE,
        "nil":FALSE,
        }

def evaluate_s(env_ref,s):
    if len(s) == 0:
        return FALSE

    env_copy = dict(env_ref)

    functor = evaluate(env_copy,s[0])

    #print "functor: ",functor
    # This is the one function that I know affects the scoping of its
    # calling environment
    if functor == "setf":
        ret = special_forms[functor](env_ref,*s[1:] if len(s) > 1 else [])
        return ret

    if str(functor) in special_forms:
        ret = special_forms[functor](env_copy,*s[1:] if len(s) > 1 else [])
        return ret

    if str(functor) in primitives:
        parms=[evaluate(env_copy,datum) for datum in s[1:]]
        ret = primitives[functor](env_copy,*parms)
        return ret

    if str(functor) in functions:
        parms=[evaluate(env_copy,datum) for datum in s[1:]]
        parms = [function(functor)] + parms
        return funcall(env_copy,*parms)

    if type(functor) is tuple and functor[0] == "function":
        parms=[evaluate(env_copy,datum) for datum in s[1:]]
        parms = [functor] + parms
        return funcall(env_copy,*parms)

    raise "Missing function in form: "+str(functor)

def evaluate(env,x):
    if type(x) is list:
        return evaluate_s(env,x)
    else:
        if x in env:
            return copy.deepcopy(env[x])
        else:
          if x in system_dictionary:
            return copy.deepcopy(system_dictionary[x])
          else:
            return copy.deepcopy(x)

