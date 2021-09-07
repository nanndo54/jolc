import json

INPUT = '''
println(fib(4));

function fib(num)
  print(num);
  return 1;
end;
'''

lexer = False
parser = False
interpreter = True

def run(INPUT, lexer=False, parser=False, interpreter=False):
  # LEXER
  if lexer:
    from interpreter.analyzer import lexer as lex
    print('=== LEXER ===')
    lex.input(INPUT)
    for tok in lex:
        print(tok)

  # PARSER
  if parser:
    from interpreter.analyzer import parse
    print('=== PARSER ===')
    res = parse(INPUT)
    try:
      print(json.dumps(res, indent=2))
    except:
      print(res)

  # INTERPRETER
  if interpreter:
    from interpreter.main import interpret
    print('=== INTERPRETER ===')
    res = interpret(INPUT)
    try:
      print(json.dumps(res['output'], indent=2))
      print(json.dumps(res['errors'], indent=2))
    except:
      print(res['output'])
      print(res['errors'])

run(INPUT, lexer, parser, interpreter)