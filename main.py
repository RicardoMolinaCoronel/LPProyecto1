import tkinter

from lexico import tokens
import ply.yacc as yacc
import tkinter as tk
from variables_analizador import app,error,cajaValidator

# BY RICARDO MOLINA : class_content,ifElseStatement,conditions,Map,declarationExpression,function_lambda,parte forStatement
algoritmoPruebaSintaticoRicardoMolina = '''
Map<int,String> personas = {
    1 : 'ere',
    2 :'sd'
};
if(!n==true){
int x=5;
  }else if(n==6){
  int x=6;
  }else if(n==7){
  int x=7;
  }else{
  int x=8;
  }
void imprimirMediaNumero(int c1,{required int num1, required int num2}) => num1+num2;
int x= num1+num2;
'''

# BY JARED CASTILLO : FOR, STACK, INFERED RETURN FUNCTION STATEMENT
algoritmoPruebaSintaticoJaredCastillo = '''
while(a < b) {
  x++;
 }

final stack = Stack<int>();
final smokeStack = Stack.of(list);

suma(int a, int b) {
  return a + b;
}
'''

algoritmoPruebaSemanticoJaredCastillo = '''
List<int> numeros = [1, 2, 3, 4, 5];

List<dynamic> tupla = [1, "dos", true];

bool a = true;

bool c = a && b;

bool c = a || b;
'''
# Testeos
algoritmoLexico1 = '''
//ALGORITMO RICARDO MOLINA
main() {
  print(insertionSort([8,9, 4, 2, 6,10,12]));
}
List<int> insertionSort(List<int> list) {
  for (int j = 1; j < list.length; j++) {
    int key = list[j];
    int i = j - 1;
  }
  return list;
}
    '''

algoritmo2 = '''//ALGORITMO POR JARED CASTILLO 
// importing dart:io file
import 'dart:async';
import 'dart:io';

void main()  {
  menu();
}


void leerFile() {

  try {
    var file = File('C:/Users/wayar/OneDrive/Escritorio/archivo.txt');
    var contents = file.readAsLinesSync();
    for(var line in contents){
    print(line);
    }

  } catch (e) {
    if (e is FileSystemException && e.message.contains('No such file or directory') || e is PathNotFoundException) {
      print('El archivo no existe o la ruta es incorrecta.');
    }
  }
  menu();
}

void escribirFile() async{

    print("Ingresa el contenido: ");
    String contenido = stdin.readLineSync()!;
    var file = File('C:/Users/wayar/OneDrive/Escritorio/archivo.txt');
    var sink = file.openWrite(mode: FileMode.append);
    sink.write((contenido + " "));
    await sink.close();
    print('¡Archivo escrito exitosamente!');  
    menu();
}


void menu() {

  print("\n************* MENU ******************");
  print("1. Ingresar contenido");
  print("2. Leer archivo\n");
  String scan2 = stdin.readLineSync()!;

  print("Elija una opcion: ");
  int opt = int.parse(scan2);

  if(opt == 1){
    escribirFile();
  }else if(opt == 2){
    leerFile();
  }else{
    print("Opcion incorrecta. Cerrando Sesion...");
    exit(0);
  }
}
'''

algoritmo3 = '''
//ALGORITMO FREDDY TENESACA
int mayorQueX(Iterable<int> collection, int x) {
  return collection.where((item) => item > x).length;
}

main() async {
  final numeros = [1, 2, 3, 4, 8, 52, 47, 8, 10, 18, 19, 4, 19];
  final mySet = Set<int>.from(numeros);
  final puntos = {
    'juan': 1, 
    'pedro': 4,
    'josue': 7,
    'luis': 2
   };
  final x = 5;

  print('Numeros mayor que $x en list: ${mayorQueX(numeros, 5)}');
  print('Numeros mayor que $x en set: ${mayorQueX(mySet, 5)}');
  print('Puntos mayor que $x en map: ${mayorQueX(puntos.values, 5)}');
}
'''


def p_class(p):
    'class : class_content_repeat'


def p_class_content_map(p):
    '''class_content : map
    '''


def p_class_content_ifElse(p):
    '''class_content : ifElseStatement
    '''


def p_class_content_lambdaFunction(p):
    '''class_content : function_lambda
    '''


def p_class_content_declarationExpression(p):
    '''class_content : declarationExpression
    '''


def p_class_content_for(p):
    '''class_content : forStatement
    '''


def p_class_content_while(p):
    '''class_content : while
    '''


def p_class_content_stack(p):
    '''class_content : stack
    '''


def p_class_content_inferedFunction(p):
    '''class_content : inferedReturnFunction
    '''


def p_class_content_expression(p):
    '''class_content : expression SEMICOLON
    '''


def p_class_content_repeat(p):
    '''class_content_repeat : class_content
                             | class_content_repeat class_content
    '''


def p_class_content_bool(p):
    '''class_content : semanticbool
    '''


def p_class_content_semanticlist(p):
    '''class_content : semanticlist
    '''


def p_map(p):
    'map : map_identifier IDENTIFIER EQUAL LCURLYBRACKET map_content RCURLYBRACKET SEMICOLON'


def p_map_identifier(p):
    '''map_identifier : MAP
                       | MAP map_type_specified
    '''


def p_map_type_specified(p):
    'map_type_specified : LESSTHAN datatype COMMA datatype GREATERTHAN'


def p_datatype(p):
    '''datatype : returnType
                 | VAR
    '''


def p_returnType(p):
    '''returnType : INT
                   | STRING
                   | BOOL
                   | DOUBLE
                   | DYNAMIC
                   | VOID
                   | map_identifier
    '''


def p_empty(p):
    'empty :'


def p_map_content(p):
    '''map_content : map_pairs
                    | empty
    '''


def p_map_pair(p):
    'map_pair : map_key COLON map_value'


def p_map_pairs(p):
    '''map_pairs : map_pair
                  | map_pair COMMA map_pairs
    '''


def p_map_key(p):
    '''map_key : value
    '''


def p_map_value(p):
    '''map_value : value
    '''


def p_ifElseStatement(p):
    '''ifElseStatement : ifStatement
                        | ifStatement elifStatement_repeat
    '''


def p_elifStatement_repeat(p):
    '''elifStatement_repeat : elifStatement
                             | elifStatement elifStatement_repeat
    '''


def p_ifStatement(p):
    '''ifStatement : IF LPAREN conditions RPAREN LCURLYBRACKET class_content_repeat RCURLYBRACKET
    '''


def p_elifStatement(p):
    '''elifStatement : ELSE ifStatement
    '''


def p_elseStatement(p):
    '''elifStatement : ELSE LCURLYBRACKET class_content_repeat RCURLYBRACKET
    '''


def p_forStatement(p):
    '''forStatement : FOR LPAREN declarationExpression SEMICOLON condition SEMICOLON expression RPAREN LCURLYBRACKET RCURLYBRACKET
    '''


# def p_taskStatement(p):
#  '''taskStatement : IDENTIFIER operatorExpression operatorExpression
#  '''

def p_stack(p):
    '''stack : FINAL IDENTIFIER EQUAL STACK LESSTHAN datatype GREATERTHAN LPAREN opt_value RPAREN SEMICOLON
    '''


def p_whileStatement(p):
    '''while : WHILE LPAREN conditions RPAREN LCURLYBRACKET class_content_repeat RCURLYBRACKET
    '''


def p_stackStatement(p):
    '''stack : FINAL IDENTIFIER EQUAL STACK LESSTHAN datatype GREATERTHAN LPAREN RPAREN SEMICOLON
            | FINAL IDENTIFIER EQUAL STACK DOT OF LPAREN IDENTIFIER RPAREN SEMICOLON
    '''


def p_inferedReturnFunction(p):
    '''inferedReturnFunction : IDENTIFIER LPAREN  function_arguments_repeat RPAREN LCURLYBRACKET RETURN expression SEMICOLON RCURLYBRACKET
    '''


def p_value(p):
    '''value : INTEGER
                | FLOAT
                | STR
                | BOOLEAN
                | IDENTIFIER
                | booleanOp
    '''


def p_opt_value(p):
    '''opt_value : value
                  | empty
    '''


def p_deniable_values(p):
    '''deniable_values : IDENTIFIER
                        | BOOLEAN
                        | booleanOp
    '''


def p_negation_values(p):
    '''negation_values : deniable_values
                       | EXMARK deniable_values
    '''


def p_condition_values(p):
    '''condition_values : negation_values
                        | INTEGER
                        | FLOAT
                        | STR
    '''


def p_condition_operator(p):
    '''condition_operator : DOUBLEQUAL
                           | LESSTHAN
                           | GREATERTHAN
                           | LESSTHAN EQUAL
                           | GREATERTHAN EQUAL
    '''


def p_number(p):
    '''number : FLOAT
               | INTEGER
    '''


def p_condition(p):
    '''condition : IDENTIFIER condition_operator condition_values
                  | EXMARK IDENTIFIER condition_operator condition_values
                  | BOOLEAN condition_operator BOOLEAN
                  | number condition_operator number
                  | STR condition_operator STR
                  | booleanOp condition_operator booleanOp
    '''


def p_conditions(p):
    '''conditions : condition
                   | condition condition_connector conditions
    '''


def p_condition_connector(p):
    '''condition_connector : AND
                            | OR
                            | AMPERSAND AMPERSAND
                            | PIPELINE PIPELINE
    '''


def p_function_lambda(p):
    '''function_lambda : datatype IDENTIFIER LPAREN function_arguments_repeat optFunction_argumentsExpression RPAREN EQUAL GREATERTHAN expression SEMICOLON
    '''


def p_function_argument(p):
    ''' function_argument : datatype IDENTIFIER
                          | empty
    '''


def p_function_arguments_repeat(p):
    '''function_arguments_repeat : function_argument
                                  | function_argument COMMA function_arguments_repeat
    '''


def p_optFunction_argumentsExpression(p):
    ''' optFunction_argumentsExpression : LCURLYBRACKET optFunction_arguments RCURLYBRACKET
                                         | empty
    '''


def p_optFunction_argument(p):
    '''optFunction_argument : REQUIRED datatype IDENTIFIER

    '''


def p_optFunction_arguments(p):
    '''optFunction_arguments : optFunction_argument
                              | optFunction_argument COMMA optFunction_arguments
    '''


def p_expression(p):
    '''expression : operableTypes operatorExpression operableTypes
                    | value
                    | operableTypes operatorExpression operatorExpression
    '''


def p_operableTypes(p):
    '''operableTypes : IDENTIFIER
                      | number
    '''


def p_operatorExpression(p):
    '''operatorExpression : PLUS
                           | MINUS
                           | TIMES
                           | DIVISION
    '''


def p_declarationExpression(p):
    '''declarationExpression : datatype IDENTIFIER SEMICOLON
    '''


def p_declarationExpression_asignOther(p):
    '''declarationExpression : datatype IDENTIFIER EQUAL expression SEMICOLON
    '''



# SEMANTIC RULES

def p_semanticbool(p):
    ''' semanticbool : BOOL IDENTIFIER EQUAL booleanOp SEMICOLON
             | BOOL IDENTIFIER EQUAL booloperations SEMICOLON
    '''

def p_booleanOp(p):
    '''booleanOp : TRUE
                | FALSE
    '''

def p_booloperation(p):
    ''' booloperation : booleanOp condition_connector booleanOp
                    | IDENTIFIER condition_connector booleanOp
                    | IDENTIFIER condition_connector IDENTIFIER
                    | booleanOp condition_connector IDENTIFIER
    '''


def p_booloperations(p):
    ''' booloperations : booloperation
                      | booloperation condition_connector booloperations
    '''


def p_semanticlist(p):
    ''' semanticlist : LIST LESSTHAN DYNAMIC GREATERTHAN IDENTIFIER EQUAL LSQUAREBRACKET insidelist RSQUAREBRACKET SEMICOLON
                    | LIST LESSTHAN  INT GREATERTHAN IDENTIFIER EQUAL LSQUAREBRACKET insidelistint RSQUAREBRACKET SEMICOLON
                    | LIST LESSTHAN  STRING GREATERTHAN IDENTIFIER EQUAL LSQUAREBRACKET insideliststr RSQUAREBRACKET SEMICOLON
                    | LIST LESSTHAN  BOOL GREATERTHAN IDENTIFIER EQUAL LSQUAREBRACKET insidelistbool RSQUAREBRACKET SEMICOLON
                    | LIST LESSTHAN  DOUBLE GREATERTHAN IDENTIFIER EQUAL LSQUAREBRACKET insidelistdouble RSQUAREBRACKET SEMICOLON
    '''


# LIST LESSTHAN  datatype GREATERTHAN IDENTIFIER EQUAL LSQUAREBRACKET insidelist RSQUAREBRACKET SEMICOLON

# returnType : INT| STRING| BOOL| DOUBLE| DYNAMIC| VOID| map_identifier

def p_insidelist(p):
    ''' insidelist : value
                    | value COMMA insidelist
    '''


def p_insidelistint(p):
    ''' insidelistint : INTEGER
                    | INTEGER COMMA insidelistint
    '''


def p_insideliststr(p):
    ''' insideliststr : STR
                    | STR COMMA insideliststr
    '''


def p_insidelistbool(p):
    ''' insidelistbool : booleanOp
                    | booleanOp COMMA insidelistbool
    '''


def p_insidelistdouble(p):
    ''' insidelistdouble : FLOAT
                    | FLOAT COMMA insidelistdouble
    '''

def p_declarationExpression_asignString(p):
    '''declarationExpression : STRING IDENTIFIER EQUAL expressionString SEMICOLON
    '''
def p_expressionString(p):
     '''expressionString : STR
                          | STR operatorExpressionString expressionString
     '''
def p_operationExpressionString(p):
    '''operatorExpressionString : PLUS
    '''
def p_declarationExpression_asignInteger(p):
    '''declarationExpression : INT IDENTIFIER EQUAL expressionInteger SEMICOLON
    '''
def p_expressionInteger(p):
     '''expressionInteger : number
                          | number operatorExpression expressionInteger
     '''
def p_expressionIntegerIdentifier(p):
    '''expressionInteger : IDENTIFIER
                         | IDENTIFIER operatorExpression expressionInteger
    '''



def p_error(p):
    globals()['error'] = True
    cajaValidator.config(fg=rojo)
    if p:
        cajaValidator.insert(tk.END, "Error de sintaxis en token:" + p.type + "\n")
        print("Error de sintaxis en token:", p.type)
        # sintactico.errok()
    else:
        cajaValidator.insert(tk.END, "Syntax error at EOF" + "\n")
        print("Syntax error at EOF")


# Build the parser
sintactico = yacc.yacc()


def runAnalyzer():
    cajaValidator.config(state=tk.NORMAL)
    cajaValidator.delete(1.0, "end-1c")
    cajaValidator.config(fg=verde)
    codigo = cajaCodigo.get(1.0, "end-1c")
    result = sintactico.parse(codigo)
    if (error != True):
        cajaValidator.insert(1.0, "Todo OK!")
    globals()['error'] = False
    cajaValidator.config(state=tk.DISABLED)


fondo = "#444444"
celeste = "#00A4D3"
gris1 = "#B1B1B1"
verde = "#639D45"
rojo = "#E11E1E"



app.geometry("900x470")
app.configure(background="#444444")
tk.Wm.wm_title(app, "DART ANALYZER")
img = tkinter.PhotoImage(file="img/Dart_logo.png")
app.resizable(False, False)
tk.Label(app, image=img, bg=fondo
         ).place(x=15, y=10, width=45, height=45)
tk.Label(app, text="DART ANALYZER GRUPO 2", font=("Calibri", 23), bg=fondo, fg="white"
         ).place(x=75, y=10, width=350, height=45)
tk.Label(app, text="CODE", font=("Calibri", 12), bg=fondo, fg=gris1
         ).place(x=17, y=70, width=50, height=20)
tk.Label(app, text="VALIDATOR", font=("Calibri", 12), bg=fondo, fg=gris1
         ).place(x=582, y=70, width=100, height=20)
cajaCodigo = tk.Text(app, font=("Calibri", 12), bg="white", fg="black")
cajaCodigo.place(x=15, y=100, width=550, height=300)


tk.Button(app, text="RUN", font=("Calibri", 18), background="#00A4D3", fg="black", relief="flat", command=runAnalyzer
          ).place(x=15, y=410, width=100, height=40)
app.mainloop()




