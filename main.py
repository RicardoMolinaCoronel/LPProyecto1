from lexico import tokens
import ply.yacc as yacc

prueba1='''
Map<int,String> personas = {
   1 : 'ere',
    2 :'sd'
};
if(n==5){
  }else if(n==6){
  }else if(n==7){
  }else{
  }
void imprimirMediaNumero(int c1,{required int num1, required int num2}) => num1+num2;
int x= num1+num2;
'''

prueba2 = '''


for (var i = 0; i < 5; i++) {
  message.write('!');
}

'''
#Testeos
algoritmo1 = '''
//ALGORITMO RICARDO MOLINA
main() {
  print(insertionSort([8,9, 4, 2, 6,10,12]));
}
List<int> insertionSort(List<int> list) {
  for (int j = 1; j < list.length; j++) {
    int key = list[j];
    int i = j - 1;
    while (i >= 0 && list[i] > key) {
      list[i + 1] = list[i];
      i = i - 1;
      list[i + 1] = key;
    }
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

algoritmo3= '''
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
    'class : map ifElseStatement function_lambda declarationExpression'

def p_map(p):
  'map : map_identifier IDENTIFIER EQUAL LCURLYBRACKET map_content RCURLYBRACKET SEMICOLON'

def p_map_identifier(p):
  '''map_identifier : MAP
                     | MAP map_type_specified
  '''

def p_map_type_specified(p):
  'map_type_specified : LESSTHAN datatype COMMA datatype GREATERTHAN'

def p_datatype(p):
  '''datatype : INT
               | STRING
               | BOOL
               | DOUBLE
               | DYNAMIC
               | VAR
               | VOID
               | map_identifier
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
  '''ifStatement : IF LPAREN conditions RPAREN LCURLYBRACKET RCURLYBRACKET
  '''

def p_elifStatement(p):
  '''elifStatement : ELSE ifStatement
  '''
def p_elseStatement(p):
  '''elifStatement : ELSE LCURLYBRACKET RCURLYBRACKET
  '''

def p_forStatement(p):
  ''' for : For LPAREN declarationExpression conditions SEMICOLON task RPAREN LCURLYBRACKET RCURLYBRACKET
  '''

def p_taskStatement(p):
  '''task: value EQUAL
  '''
def p_value(p):
  '''value : INTEGER
              | FLOAT
              | STR
              | BOOLEAN
              | IDENTIFIER
  '''

def p_deniable_values(p):
  '''deniable_values : IDENTIFIER
                      | BOOLEAN
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
  '''

def p_conditions(p):
  '''conditions : condition
                 | condition condition_connector conditions
  '''

def p_condition_connector(p):
  '''condition_connector : AND
                          | OR
  '''

def p_function_lambda(p):
  '''function_lambda : returnType IDENTIFIER LPAREN function_arguments_repeat optFunction_argumentsExpression RPAREN EQUAL GREATERTHAN expression SEMICOLON
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
  '''expression : IDENTIFIER PLUS IDENTIFIER
  '''

def p_declarationExpression(p):
  '''declarationExpression : datatype IDENTIFIER SEMICOLON
  '''

def p_declarationExpression_asign(p):
  '''declarationExpression : datatype IDENTIFIER EQUAL expression SEMICOLON
  '''

def p_error(p):
  if p:
    print("Error de sintaxis en token:", p.type)
    #sintactico.errok()
  else:
    print("Syntax error at EOF")


# Build the parser
sintactico = yacc.yacc()

while True:
  try:
    s = input('dart > ')
  except EOFError:
    break
  if not s: continue
  result = sintactico.parse(prueba1)
  if result != None: print(result)

