import ply.lex as lex

#AvanceLexico ply

#Diccionario de palabras reservadas
reserved = {
            'while':'WHILE',
            'for':'FOR',
            'int':'INT',
            'import': 'IMPORT',
            'print':'PRINT',
            'main':'MAIN',
            'List': 'LIST',
            'return':'RETURN',
            'exit' : 'EXIT',
            'write' : 'WRITE',
            'close' : 'CLOSE',
            'readLineSync' : 'READLINE',
            'openWrite' : 'OPENW',
            'void' : 'VOID',
            'try' : 'TRY',
            'catch' : 'CATCH',
            'var' : 'VAR',
            'File' : 'FILE',
            'if' : 'IF',
            'async' : 'ASYNC',
            'await' : 'AWAIT',
            'String' : 'STRING',
            'double' : 'DOUBLE',
            'Iterable' : 'ITERABLE',
            'Set' : 'SET'



           }


#Sequencia de tokens
tokens = ('NUMERO','MAS', 'MENOS', 'POR', 'ENTRE', 'LPAREN', 'RPAREN',
          'CAMPO','COMMENT','PUNTO','COMA','MAYORQUE','MENORQUE','DIFERENTE',
          'COMADOBLE','CADENA','IGUAL','IGUALDOBLE',"LLLAVE","RLLAVE",
          'LCORCH','RCORCH','PUNTOCOMA','AMPERSAND', 'COLON', 'EXMARK', 'AND', 'OR', 'APOSTROFE','METODO', 'DOLAR') + tuple(reserved.values())

'''
Contribucion Ricardo: tokens(COMMENT hasta AMPERSAND), reservadas(while hasta return)
Contribucion Jared: tokens(COLON - APOSTROFE), reservada(exit - openWrite)
Contribucion Freddy: tokens (DOLAR), reservada (Iterable - Set)

'''


#Exp Regulares para tokens de símbolos


t_NUMERO = r'\d+'
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_ENTRE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PUNTO = r'\.'
t_COMA = r','
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_DIFERENTE = r'<>'
t_COMADOBLE = r'\"'
t_CADENA = r'("[^".]*"|\'[^\'.]*\'|"[^"]*"|\'[^\']*\')'
t_IGUAL = r'='
t_IGUALDOBLE = r'=='
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
t_LCORCH = r'\['
t_RCORCH = r'\]'
t_PUNTOCOMA = r';'
t_AMPERSAND = r'&'
t_COLON = r':'
t_EXMARK = r'!'
t_AND = r'&&'
t_OR = r'\|\|'
t_APOSTROFE = r'\''
t_METODO = r'[a-zA-Z\_]+\(\)$'
t_DOLAR=r'\$'

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
  r'\/\/.*'
  pass

# Ignorar lo que no sea un token en mi LP
t_ignore = ' \t'


#Presentación de errores léxicos
def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)

#Contruir analizador
lexer = lex.lex()

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

#Datos de entrada
lexer.input(algoritmo2)

# Tokenizador
while True:
  tok = lexer.token()
  if not tok:
    break  #Rompe
  print(tok)
