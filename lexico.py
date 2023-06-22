import ply.lex as lex
import reservadas

reserved = reservadas.crear(
  ['while',
   'for',
   'int',
   'import',
   'print',
   'main',
   'List',
   'return',
   'exit',
   'write',
   'close',
   'readLineSync',
   'openWrite',
   'void',
   'try',
   'catch',
   'var',
   'File',
   'if',
   'else',
   'async',
   'await',
   'String',
   'double',
   'Iterable',
   'Set',
   'in',
   'is',
   'true',
   'false',
   'bool',
   'dynamic'
   ])


tokens = ('INTEGER','FLOAT','IDENTIFIER','PLUS', 'MINUS', 'TIMES', 'DIVISION', 'LPAREN', 'RPAREN',
          'COMMENT','DOT','COMA','GREATERTHAN','LESSTHAN','NOTEQUAL',
          'DOUBQUOTMARK','STR','EQUAL','DOUBLEQUAL',"LCURLYBRACKET","RCURLYBRACKET",
          'LSQUAREBRACKET','RSQUAREBRACKET','SEMICOLON','AMPERSAND', 'COLON', 'EXMARK',
          'AND', 'OR', 'APOSTROPHE','METHOD', 'DOLLAR') + tuple(reserved.values())

'''
Contribucion Ricardo: tokens(COMMENT hasta AMPERSAND), reservadas(while hasta return) - algoritmo1
Contribucion Jared: tokens(COLON - APOSTROPHE), reservada(exit - await) - algoritmo2
Contribucion Freddy: tokens (DOLLAR), reservada (Iterable - Set) - algoritmo3

'''


#Exp Regulares para tokens de símbolos


t_INTEGER = r'[+-]?\d+'
t_FLOAT=r'[+-]?([0-9]*)[\.][0-9]+'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVISION = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT = r'\.'
t_COMA = r','
t_GREATERTHAN = r'>'
t_LESSTHAN = r'<'
t_NOTEQUAL = r'<>'
t_DOUBQUOTMARK = r'\"'
t_STR = r'("[^".]*"|\'[^\'.]*\'|"[^"]*"|\'[^\']*\')'
t_EQUAL = r'='
t_DOUBLEQUAL = r'=='
t_LCURLYBRACKET = r'\{'
t_RCURLYBRACKET = r'\}'
t_LSQUAREBRACKET = r'\['
t_RSQUAREBRACKET = r'\]'
t_SEMICOLON = r';'
t_AMPERSAND = r'&'
t_COLON = r':'
t_EXMARK = r'!'
t_AND = r'&&'
t_OR = r'\|\|'
t_APOSTROPHE = r'\''
t_METHOD = r'[a-zA-Z\_]+\(\)$'
t_DOLLAR=r'\$'

t_ignore = " \t"



#Para contabilizar nro de líneas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_IDENTIFIER(t):
  r'[a-zA-Z]\w*'
  t.type = reserved.get(t.value, 'IDENTIFIER')
  return t

#Ignorar un comentario
def t_COMMENT(t):
  r'\/\/.*'
  pass


def t_error(t):
  print("Error léxico", t.value.strip(), " línea:", t.lineno, "columna:",
        t.lexpos)
  t.lexer.skip(1)


lexico = lex.lex()


# Give the lexer some input
def consultarTokens(data):
  # Tokenize
  lexico.input(data)
  while True:
    tok = lexico.token()
    if not tok:
      break  # No more input
    print(tok)


# Test it out
data = '''int 5;
'''
#consultarTokens(data)
