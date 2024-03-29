
import ply.lex as lex
import reservadas
import variables_analizador

import tkinter as tk
palabras=['while',
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
   'bool',
   'dynamic',
   'Map',
   'required',
   'final',
   'Stack',
   'of',
   'do',
   'true',
   'false',
   'dynamic',
   'null',
   'keys',
   'values',
          'abstract','case','const','default','export','factory','continue','deferred' ,'extension','assert',
          'break','class','enum','external','Function','get','implements','library','add'
   ]
reserved = reservadas.crear(
    palabras
  )


tokens = ('INTEGER','FLOAT','IDENTIFIER','BOOLEAN','PLUS', 'MINUS', 'TIMES', 'DIVISION', 'LPAREN', 'RPAREN',
          'COMMENT','COMMENTMULTI','DOT','COMMA','GREATERTHAN','LESSTHAN','NOTEQUAL',
          'DOUBQUOTMARK','STR','EQUAL','DOUBLEQUAL',"LCURLYBRACKET","RCURLYBRACKET",
          'LSQUAREBRACKET','RSQUAREBRACKET','SEMICOLON','AMPERSAND', 'COLON', 'EXMARK',
          'AND', 'OR', 'APOSTROPHE','METHOD', 'DOLLAR', 'PIPELINE','REST') + tuple(reserved.values())

'''
Contribucion Ricardo: tokens(COMMENT hasta AMPERSAND), reservadas(while hasta return) - algoritmo1
Contribucion Jared: tokens(COLON - APOSTROPHE), reservada(exit - await) - algoritmo2
Contribucion Freddy: tokens (DOLLAR), reservada (Iterable - Set) - algoritmo3

'''


#Exp Regulares para tokens de símbolos


t_INTEGER = r'\d+'
t_FLOAT=r'[+-]?([0-9]*)[\.][0-9]+'
t_BOOLEAN=r'true|false'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVISION = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT = r'\.'
t_COMMA = r','
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
t_PIPELINE= r'\|'
t_REST= r'%'

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
def t_COMMENTMULTI(t):
  r'\/\*[^\*]*\*\/'
  pass


def t_error(t):
  variables_analizador.error= True
  variables_analizador.cajaValidator.config(fg="#E11E1E")
  variables_analizador.cajaValidator.insert(tk.END, "Lexical error at symbol: "+ t.value.strip()+ "\n")
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
data = '''Map<int,String> personas = {
   1 : 'ere',
    2 :'sd'
};
if(n==5){
  }else if(n==6){
  }else if(n==7){
  }else{
  }
void imprimirMediaNumero(int c1,{required int num1, required int num2}) => num1+num2;
'''

data2 = '''main(){
/*
Algoritmo de pueba
*/
final PI =3.1416;
bool isEmpty = false;
	Map<int,String> personas = {
    		1 : 'Ricardo',
    		2 : 'Molina',
    		4 : 'Coronel'
	};
	Map<String,String> personasVacio ={};
	var claves = personas.keys;
	var valores = personas.values;
	String persona1= "Jorge";
	String persona2= "Jorge"+"Coello";
	
	var x=5;
	int x1=5.5;
	int n=0;
	while(n<5){
		if(n==1){
		x=1;
		continue;
		x= 5.05 + 7 / 5;
  		}else if(n==2){
 		 x=2;
  		}else if(n==3){
   	 	x=3;
  		}else{
  		x=4;
  		}
		x+=1;
		}
	print(x);
	x= 5.0 + 4 / 5;
	x-=n;
}
assert(n<5);
void sumaNumeros(int c1,{required int num1, required int num2}) => num1+num2;
int x1= num1+num2;
'''
#consultarTokens(data2)
