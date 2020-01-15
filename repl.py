import sys
import core
import traceback
import tokenization
import parse

DEBUG = 0
PROMPT = 0

def eval(s):
  tokens = tokenization.tokenize(s)
  if DEBUG :
      print("tokens:",tokens)

  tokens,tree = parse.parse(tokens)
  if DEBUG :
      print("tree:",tree)

  tree = parse.quote(tree)
  if DEBUG :
      print("post quote:",tree)
  return [core.evaluate({},x) for x in tree]

def lambda_handler(event, context): 
    # assume event is a str
    return eval(event)

def prompt(run_count):
    if PROMPT:
        sys.stdout.write("[%i]> " % run_count)


def repl():
    run_count = 0
    lp = 0
    rp = 0
    bufr = ""
    prompt(run_count)
    while True:
        line = sys.stdin.readline()
        # if EOF
        if line == "":
            sys.exit()
        bufr = bufr + line
        lp = lp + line.count('(')
        rp = rp + line.count(')')
        if(lp == rp):
            try:
                results = eval(bufr)
                run_count = run_count + len(results)
                parse.show(results)
                sys.stdout.write("\n")
            except Exception as error:
                print('Caught this error: ' + repr(error))
                print(traceback.format_exc())
                #print(sys.exc_info()[0])
            bufr = ""
            lp = 0
            rp = 0
        prompt(run_count)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for x in range(1,len(sys.argv)):
          if sys.argv[x]  == "debug":
            DEBUG = 1
          else:
              if sys.argv[x] == "prompt":
                  PROMPT = 1
              else:
                  print("Invalid command line option. Exiting")
                  sys.exit()
    repl()
