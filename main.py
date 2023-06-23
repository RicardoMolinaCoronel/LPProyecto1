from lexico import tokens
import ply.yacc as yacc

prueba1='''
Map mapa={persona:dasda,
'sdasdas':dasd};
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
    'class : map'

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
               | map_identifier
  '''

def p_map_content(p):
  '''map_content :
                  | map_pairs
  '''

def p_map_pair(p):
  'map_pair : map_key COLON map_value'
def p_map_pairs(p):
  '''map_pairs : map_pair
                | map_pair COMMA map_pairs
  '''

def p_map_key(p):
  '''map_key : INTEGER
              | FLOAT
              | STR
              | TRUE
              | FALSE
              | IDENTIFIER
  '''
def p_map_value(p):
  '''map_value : INTEGER
              | FLOAT
              | STR
              | TRUE
              | FALSE
              | IDENTIFIER
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

