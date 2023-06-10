import ply.lex as lex

#AvanceLexico ply

#Diccionario de palabras reservadas
reserved = {
            'print':'IMPRESION',
            'parse' : 'PARSE',
            'exit' : 'EXIT',
            'write' : 'WRITE',
            'close' : 'CLOSE',
            'readLineSync' : 'READLINE',
            'openWrite' : 'OPENW'
            ''

           }

#Sequencia de tokens
tokens = ('NUMBER','PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
          'CAMPO','COMMENT','PUNTO','COMA','MAYORQUE','MENORQUE','DIFERENTE','COMADOBLE','CADENA','IGUAL', 'COLON',
          'SEMICOLON', 'EXMARK', 'LLLAVE','RLLAVE', 'AND', 'OR') + tuple(reserved.values())

#Exp Regulares para tokens de símbolos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PUNTO=r'\.'
t_NUMBER = r'\d+'
t_COMA = r','
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_DIFERENTE = r'<>'
t_CADENA = r'"[^".]*"'
t_IGUAL = r'=='
t_COLON = r':'
t_SEMICOLON = r';'
t_EXMARK = r'!'
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
t_AND = '&&'
t_OR = '||'



#Para contabilizar nro de líneas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


def t_CAMPO(t):
  r'[a-zA-Z]\w*'
  t.type = reserved.get(t.value, 'CAMPO')
  return t


#Ignorar un comentario
def t_COMMENT(t):
  r'\#.*'
  pass

# Ignorar lo que no sea un token en mi LP
t_ignore = ' \t'


#Presentación de errores léxicos
def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)

#Contruir analizador
lexer = lex.lex()

#Testeando
data = '''
    '''.lower()

#Datos de entrada
lexer.input(data)

# Tokenizador
while True:
  tok = lexer.token()
  if not tok:
    break  #Rompe
  print(tok)
