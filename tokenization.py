#!/usr/bin/python
import sys
import re

re_integer = re.compile("^[0-9]+$")
re_float = re.compile("^[0-9]+\.[0-9]*$")

def tokenize(s):
    tokens = []
    start = 0
    n = s.find("\"",start)
    while n != -1:
        tokens = tokens + tokenize1(s[start:n])
        m = s.find("\"",n+1)
        if m == -1:
            raise "Missing end quote"

        tokens = tokens + [s[n+1:m]]
        start = m+1
        n = s.find("\"",start)

    tokens = tokens + tokenize1(s[start:])

    return tokens

def tokenize1 (s):
  s = s.replace('(',' ( ')
  s = s.replace(')',' ) ')
  s = s.replace("'"," ' ")
  s = s.replace('\n',' ')
  s = s.replace('\r',' ')
  s = s.strip()  #remove all whitespace leading and trailing

  tokens = []
  strings = s.split()
  for s in strings:
      if re_integer.match(s):
          tokens.append(int(s))
      else:
          if re_float.match(s):
              tokens.append(float(s))
          else:
              if s == "(":
                tokens.append(s)
              else:
                  if s == ")":
                      tokens.append(")")
                  else:
                      tokens.append(s)

  return tokens
