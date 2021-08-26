from interpreter.symbols import *

INPUT:str
errors:list

def getColumn(t):
  global INPUT
  line_start = INPUT.rfind('\n', 0, t.lexpos) + 1
  return (t.lexpos - line_start) + 1

def parse(input):
  global INPUT
  global errors

  INPUT = input
  errors = []

  ast = parser.parse(input)
  if ast == None: ast = []
  return {'ast':ast, 'symbols':[], 'errors':errors, 'output':[]}

reserved = [
  'Nothing',
  'Int64',
  'Float64',
  'Bool',
  'Char',
  'String',
  'struct',
  'local',
  'global',
  'function',
  'end',
  'if',
  'elseif',
  'else',
  'while',
  'for',
  'break',
  'continue',
  'return',
  'mutable',
  'in'
]

tokens = [
  'id',
  'parentesis_A',
  'parentesis_B',
  'corchete_A',
  'corchete_B',
  'int64',
  'float64',
  'bool',
  'char',
  'string',
  'mas',
  'menos',
  'asterisco',
  'barra',
  'caret',
  'modulo',
  'igual',
  'mayor',
  'menor',
  'mayor_igual',
  'menor_igual',
  'igualacion',
  'diferenciacion',
  'or',
  'and',
  'not',
  'punto',
  'coma',
  'dospuntos',
  'tipo',
  'puntoycoma'
] + reserved

# Lexemas ignorados
t_ignore                       =  ' \t'
t_ignore_comentario            = r'[#].*'
t_ignore_comentario_multilinea = r'[#]=([^=]|[\r\n]|(=+([^#])))*=+[#]'

t_parentesis_A   = r'\('
t_parentesis_B   = r'\)'
t_corchete_A     = r'\['
t_corchete_B     = r'\]'
t_mas            = r'\+'
t_menos          = r'-'
t_asterisco      = r'\*'
t_barra          = r'/'
t_caret          = r'\^'
t_modulo         = r'%'
t_mayor_igual    = r'>='
t_mayor          = r'>'
t_menor_igual    = r'<='
t_menor          = r'<'
t_igualacion     = r'=='
t_diferenciacion = r'!='
t_or             = r'\|\|'
t_and            = r'&&'
t_not            = r'!'
t_punto          = r'\.'
t_coma           = r','
t_igual          = r'='
t_tipo           = r'::'
t_dospuntos      = r':'
t_puntoycoma     = r';'

# def t_nothing(t):
#   r'Nothing'
#   valor, tipo = None, 'nothing'
#   t.value = Expresion(False, False, valor, None, tipo)
#   return t

def t_float64(t):
  r'\d+\.\d+'
  value, type = 0, 'float64'

  try:
    value = float(t.value)
  except ValueError:
    print("Float64 value too big: %d", t.value)

  t.value = Expression(t.lineno, getColumn(t), False, False, value, None, type)
  return t

def t_int64(t):
  r'\d+'
  value, type = 0, 'int64'

  try:
    value = int(t.value)
  except ValueError:
    print("Int64 value too big: %d", t.value)

  t.value = Expression(t.lineno, getColumn(t), False, False, value, None, type)
  return t

def t_bool(t):
  r'(true)|(false)'
  value, type = t.value=='true', 'bool'
  t.value = Expression(t.lineno, getColumn(t), False, False, value, None, type)
  return t

def t_char(t):
  r"'[^'\n]'"
  value, type = t.value[1], 'char'
  t.value = Expression(t.lineno, getColumn(t), False, False, value, None, type)
  return t

def t_string(t):
  r'"[^"\n]*"'
  value, type = t.value[1:-1], 'string'
  t.value = Expression(t.lineno, getColumn(t), False, False, value, None, type)
  return t

def t_id(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  if t.value in reserved: t.type = t.value
  else: t.value = Expression(t.lineno, getColumn(t), False, False, t.value, None, 'id')
  return t

def t_newline(t):
  r'\n+'
  t.lexer.lineno+=len(t.value)

def t_error(t):
  error = Error(t.lineno, getColumn(t), "Léxico", "No se pudo reconocer el lexema '%s'" % t.value)
  errors.append(error)
  t.lexer.skip(1)

# Analizador léxico
from interpreter.ply.lex import lex
lexer = lex()

# Precedencia de menos a más
precedence = (
  ('left','op_rango'),
  ('left','or'),
  ('left','and'),
  ('left','igualacion','diferenciacion'),
  ('left','menor','menor_igual','mayor','mayor_igual'),
  ('left','mas','menos'),
  ('left','asterisco','barra','modulo'),
  ('right','caret'),
  ('right','op_negacion','not'),
  ('left','op_llamada'),
  ('left','op_acceso_arreglo'),
  ('nonassoc','op_agrupacion')
)

# Producciones
def p_INS(p):
  '''
  INS : INS I puntoycoma
      | INS error puntoycoma
      | I puntoycoma
      | error puntoycoma
  '''
  print(p)
  if len(p)==4:
    p[0] = p[1]
    if type(p[2]) is dict:
      p[0].append(p[2])
  else:
    if type(p[1]) is dict:
      p[0] = [p[1]]
    else:
      p[0] = []

def p_I(p):
  '''
  I : ASIGNACION
    | ASIGNACION_STRUCT
    | ASIGNACION_ARRAY
    | FUNCION
    | STRUCT
    | LLAMADA
    | IF
    | WHILE
    | FOR
    | BREAK
    | CONTINUE
    | RETURN
  '''
  p[0] = p[1]

def p_BLOQUE(p):
  '''
  BLOQUE  : INS end
  '''
  p[0] = p[1]

def p_BLOQUE_ABIERTO(p):
  '''
  BLOQUE_ABIERTO  : INS
  '''
  p[0] = p[1]

def p_TIPO(p):
  '''
  TIPO  : Int64
        | Float64
        | Bool
        | Char
        | String
  '''
  p[0] = p[1]

def p_SCOPE(p):
  '''
  SCOPE  : local
        | global
  '''
  p[0] = p[1]

def p_ASIGNACION(p):
  '''
  ASIGNACION  : id igual ASIGNACION_VALOR
              | SCOPE id igual ASIGNACION_VALOR
              | SCOPE id
  '''
  scope, id, expression, value_type = None, None, None, None

  if len(p)==4:
    id = p[1]
    expression = p[3]['expression']
    value_type = p[3]['type']
  else:
    scope = p[1]
    id = p[2]
    if len(p)==5:
      expression = p[4]['expression']
      value_type = p[4]['type']

  p[0] = Assignment(p.lexer.lineno, getColumn(p.lexer), scope, id, expression, value_type)

def p_ASIGNACION_VALOR(p):
  '''
  ASIGNACION_VALOR  : E
                    | E tipo TIPO
  '''
  expression, type = p[1], None

  if len(p)==4:
    type = p[3]

  p[0] = {'expression':expression, 'type':type}

def p_ASIGNACION_STRUCT(p):
  '''
  ASIGNACION_STRUCT : ID igual E
  '''
  id, expression = p[1], p[3]
  p[0] = Assignment_Struct(p.lexer.lineno, getColumn(p.lexer), id, expression)

def p_ASIGNACION_ARRAY(p):
  '''
  ASIGNACION_ARRAY : id IND igual E
  '''
  id, index, expression = p[1], p[2], p[4]
  p[0] = Assignment_Array(p.lexer.lineno, getColumn(p.lexer), id, index, expression)

def p_IND(p):
  '''
  IND : IND corchete_A E corchete_B
      | corchete_A E corchete_B
  '''
  if len(p)==5:
    p[0] = p[1]
    p[0].append(p[3])
  else: p[0] = [p[2]]

def p_FUNCION(p):
  '''
  FUNCION : function id parentesis_A PAR parentesis_B BLOQUE
          | function id parentesis_A parentesis_B BLOQUE
  '''
  id, parameters, instructions = p[2], [], p[5]

  if len(p)==7:
    parameters = p[4]
    instructions = p[6]

  p[0] = Function(p.lexer.lineno, getColumn(p.lexer), id, parameters, instructions)

def p_PAR(p):
  '''
  PAR : PAR coma P
      | P
  '''
  if len(p)==4:
    p[0] = p[1]
    p[0].append(p[3])
  else: p[0] = [p[1]]

def p_P(p):
  '''
  P : id
  '''
  p[0] = p[1]

def p_STRUCT(p):
  '''
  STRUCT  : struct id ATR end
          | mutable struct id ATR end
  '''
  mutable, id, attributes = False, p[2], p[3]

  if len(p)==6:
    mutable = True
    id = p[3]
    attributes = p[4]

  p[0] = Struct(p.lexer.lineno, getColumn(p.lexer), mutable, id, attributes)

def p_ATR(p):
  '''
  ATR : ATR A
      | A
  '''
  if len(p)==3:
    p[0] = p[1]
    p[0].append(p[2])
  else: p[0] = [p[1]]

def p_A(p):
  '''
  A : id tipo TIPO puntoycoma
    | id puntoycoma
  '''
  id, tipo = p[1], None

  if len(p)==5:
    tipo = p[3]

  p[0] = Attribute(p.lexer.lineno, getColumn(p.lexer), id, tipo)

def p_EXP(p):
  '''
  EXP : EXP coma E
      | E
  '''
  if len(p)==4:
    p[0] = p[1]
    p[0].append(p[3])
  else: p[0] = [p[1]]

def p_E(p):
  '''
  E : E mas E
    | E menos E
    | E asterisco E
    | E barra E
    | E caret E
    | E modulo E
    | menos E                     %prec op_negacion
    | E mayor E
    | E menor E
    | E mayor_igual E
    | E menor_igual E
    | E igualacion E
    | E diferenciacion E
    | E or E
    | E and E
    | not E
    | parentesis_A E parentesis_B %prec op_agrupacion
    | LLAMADA                     %prec op_llamada
    | ACCESO_ARREGLO              %prec op_acceso_arreglo
    | RANGO                       %prec op_rango
    | ARREGLO
    | ID
    | int64
    | float64
    | bool
    | char
    | string
    | Nothing
  '''
  if len(p)==2:
    p[0] = p[1]
    return

  if p[1]=='(':
    p[0] = p[2]
    return

  operable, unary, l, r, type = True, False, None, None, None

  if len(p)==4:
    l = p[1]
    r = p[3]
    type = operations[p[2]]
  else:
    unary = True
    l = p[2]
    type = operations[p[1]]

  p[0] = Expression(p.lexer.lineno, getColumn(p.lexer), operable, unary, l, r, type)

def p_ARREGLO(p):
  '''
  ARREGLO : corchete_A EXP corchete_B
          | corchete_A corchete_B
  '''
  value = []
  if len(p)==4: value = p[2]
  p[0] = Expression(p.lexer.lineno, getColumn(p.lexer), False, False, value, None, 'array')

def p_LLAMADA(p):
  '''
  LLAMADA : id parentesis_A EXP parentesis_B
          | id parentesis_A parentesis_B
  '''
  id, expressions = p[1], []

  if len(p)==5:
    expressions = p[3]

  p[0] = Call(p.lexer.lineno, getColumn(p.lexer), id, expressions)

def p_ACCESO_ARREGLO(p):
  '''
  ACCESO_ARREGLO : id corchete_A E corchete_B
  '''
  id, expression = p[1], p[3]
  p[0] = Access(p.lexer.lineno, getColumn(p.lexer), id, expression)

def p_ID(p):
  '''
  ID  : ID punto id
      | id
  '''
  if len(p)==4:
    p[0] = p[1]
    p[0].append(p[3])
  else: p[0] = [p[1]]

def p_IF(p):
  '''
  IF  : if E BLOQUE
      | if E BLOQUE_ABIERTO ELSE
      | if E BLOQUE_ABIERTO ELSEIF
  '''
  expression, instructions, elseif = p[2], p[3], None

  if len(p)==5:
    elseif = p[4]

  p[0] = If(p.lexer.lineno, getColumn(p.lexer), expression, instructions, elseif)

def p_ELSEIF(p):
  '''
  ELSEIF  : elseif E BLOQUE
          | elseif E BLOQUE_ABIERTO ELSEIF
          | elseif E BLOQUE_ABIERTO ELSE
  '''
  expression, instructions, elseif = p[2], p[3], None

  if len(p)==5:
    elseif = p[4]

  p[0] = If(p.lexer.lineno, getColumn(p.lexer), expression, instructions, elseif)

def p_ELSE(p):
  '''
  ELSE : else BLOQUE
  '''
  instructions = p[2]
  p[0] = Else(p.lexer.lineno, getColumn(p.lexer), instructions)

def p_WHILE(p):
  '''
  WHILE : while E BLOQUE
  '''
  expression, instructions = p[2], p[3]
  p[0] = While(p.lexer.lineno, getColumn(p.lexer), expression, instructions)

def p_FOR(p):
  '''
  FOR : for id in E BLOQUE
  '''
  id, expression, instructions = p[2], p[4], p[5]
  p[0] = For(p.lexer.lineno, getColumn(p.lexer), id, expression, instructions)

def p_RANGO(p):
  '''
  RANGO : E dospuntos E
  '''
  izq, der = p[1], p[3]
  p[0] = Expression(p.lexer.lineno, getColumn(p.lexer), False, False, izq, der, 'rango')

def p_BREAK(p):
  '''
  BREAK : break
  '''
  p[0] = Break(p.lexer.lineno, getColumn(p.lexer))

def p_CONTINUE(p):
  '''
  CONTINUE : continue
  '''
  p[0] = Continue(p.lexer.lineno, getColumn(p.lexer))

def p_RETURN(p):
  '''
  RETURN  : return E
          | return
  '''
  expression = None

  if len(p)==3:
    expression = p[2]

  p[0] = Return(p.lexer.lineno, getColumn(p.lexer), expression)

def p_error(p):
  if p:
    if type(p.value) is dict: msg = "Sintáxis no válida en {}".format(p.type)
    else: msg = "Sintaxis no válida cerca de '{}' ({})" .format(p.value, p.type)
    error = Error(p.lineno, getColumn(p), "Sintáctico", msg)
  else:
    error = Error(0, 0, "Sintáctico", "Ninguna instrucción válida")

  errors.append(error)

from interpreter.ply.yacc import yacc
parser = yacc()
