#!/usr/bin/python
import sys
def show(tree):
    i = 0;
    while len(tree) > i:
        x = tree[i]
        if type(x) is list:
            sys.stdout.write("(")
            show(x)
            sys.stdout.write(")")
            if i < len(tree) - 1:
                sys.stdout.write(" ")
        else:
            if x is tuple and x[0] == FUNCTION:
                sys.stdout.write("(function ")
                show(x)
                sys.stdout.write(")")
            else:
                sys.stdout.write(str(x))
            if i < len(tree) - 1:
                sys.stdout.write(" ")

        i = i + 1
    return i

def quote(tree):
    t = []
    while len(tree) > 0:
        x = tree.pop(0)
        if type(x) is list:
            t.append(quote(x))
        else:
          if x == "'":
              t.append(["quote",tree.pop(0)])
          else:
            t.append(x)
    return t

def parse (tokens):
    sexp = []
    while len(tokens) > 0:
        c = tokens.pop(0)
        if c == "(":
            tokens, sexp1 = parse(tokens)
            sexp.append(sexp1)
        else:
            if c == ")":
                return (tokens,sexp)
            else:
                sexp.append(c)
    return (tokens,sexp)
