import tkinter

from lexico import tokens
import ply.yacc as yacc
import tkinter as tk
from variables_analizador import app,error,cajaValidator
from lexico import palabras

# BY RICARDO MOLINA : class_content,ifElseStatement,conditions,Map,declarationExpression,asign,function_lambda,main,parte forStatement,print,GUI
# SEMANTIC RULES: declarationString, declarationInt, operationTypesString,operationTypesInt
algoritmoPruebaRicardoMolina = '''
main(){
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
	var x=5;
	int x1=5.5;
	int n=0;
	while(n<5){
		if(n==1){
		x=1;
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
assert(true);
void imprimirMediaNumero(int c1,{required int num1, required int num2}) => num1+num2;
int x1= num1+num2;

'''

# BY JARED CASTILLO : FOR, STACK, INFERED RETURN FUNCTION STATEMENT
algoritmoPruebaSintaticoJaredCastillo = '''
main(){
int a=0;
int b=20;
bool b1 = true;
bool b2 = false;
bool b3 = false || !true;

while(a < b) {
  a+=1;
 }
List<String> letras = ["a","b","c"];
letras.add("d");
letras.add("e");
letras.add("f");

List<int> numeros = [1, 2, 3, 4, 5];
numeros.add(6);
numeros.add(7);

//Error
//List<int> numeros = [1, 2, 3, 4, 5];
//numeros.add("a");

List<bool> booleanos = [true, false, false, false, true];
booleanos.add(true);

final stack = Stack<int>();
final smokeStack = Stack.of(numeros);

}

//Funciones con tipo de retorno inferido
operacionBools(){
return b1 && b2 || b1 || false;
}


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

algoritmoPruebaSintaticoFreddyTenesaca= '''
// Dartprogram to illustrate 
// Anonymous functions in Dart
void main()
{
  var list = ["Shubham","Nick","Adil","Puthal"];
  print("GeeksforGeeks - Anonymous function in Dart");
  list.forEach((item) {
    print('${list.indexOf(item)} : $item');
  });
}
'''

def p_class(p):
    '''class : class_content_repeat
              | declarationMain class_content_repeat
              | class_content_repeat declarationMain
              | declarationMain
    '''


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

def p_class_content_print(p):
    '''class_content : print
    '''


def p_class_content_repeat(p):
    '''class_content_repeat : class_content
                             | class_content_repeat class_content
    '''

def p_declarationMain(p):
    '''declarationMain : datatypeOpt MAIN LPAREN RPAREN LCURLYBRACKET class_content_repeat RCURLYBRACKET
    '''
def p_datatypeOpt(p):
    '''datatypeOpt : datatype
                    | empty
    '''
def p_class_content_bool(p):
    '''class_content : semanticbool
    '''


def p_class_content_semanticlist(p):
    '''class_content : semanticlist
    '''


def p_class_content_asign(p):
    '''class_content : asign
    '''

def p_class_content_addlistInt(p):
    '''class_content : addlistInt
    '''

def p_class_content_addlistBool(p):
    '''class_content : addlistBool
    '''

def p_class_content_addlistFloat(p):
    '''class_content : addlistFloat
    '''

def p_class_content_addlistStr(p):
    '''class_content : addlistStr
    '''

def p_class_content_assert(p):
    '''class_content : assert
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
    '''datatype : INT
                   | STRING
                   | BOOL
                   | DOUBLE
                   | DYNAMIC
                   | VOID
                   | map_identifier
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

def p_print(p):
    '''print : PRINT LPAREN value RPAREN SEMICOLON
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
                            | IDENTIFIER LPAREN  function_arguments_repeat RPAREN LCURLYBRACKET RETURN conditions SEMICOLON RCURLYBRACKET
    '''


def p_value(p):
    '''value : INTEGER
                | FLOAT
                | STR
                | BOOLEAN
                | IDENTIFIER
                | booleanOp
                | propertiesAccess


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
                        | NULL
    '''


def p_condition_operator(p):
    '''condition_operator : DOUBLEQUAL
                           | LESSTHAN
                           | GREATERTHAN
                           | LESSTHAN EQUAL
                           | GREATERTHAN EQUAL
                           | EXMARK EQUAL
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
                  | negation_values
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
    '''optFunction_argumentsExpression : LCURLYBRACKET optFunction_arguments RCURLYBRACKET
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
    '''expression : value
                    | value operatorExpression expression
                    | value operatorExpression operatorExpression
                    | booloperations
    '''
def p_asign(p):
    '''asign : IDENTIFIER EQUAL expression SEMICOLON
              | IDENTIFIER operatorExpression EQUAL expression SEMICOLON

    '''
def p_assert(p):
    '''assert : ASSERT LPAREN conditions RPAREN SEMICOLON
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
                           | REST
    '''


def p_declarationExpression(p):
    '''declarationExpression : datatype repeatDeclaration SEMICOLON
    '''
def p_repeatDeclaration(p):
    '''repeatDeclaration : IDENTIFIER
                          | IDENTIFIER COMMA repeatDeclaration
    '''


def p_declarationExpression_asignOther(p):
    '''declarationExpression : datatype IDENTIFIER EQUAL expression SEMICOLON
    '''
def p_declarationExpression_asignOtherCasting(p):
    '''declarationExpression : datatype IDENTIFIER EQUAL LPAREN datatype RPAREN IDENTIFIER SEMICOLON
    '''
def p_declarationExpression_asignConstant(p):
    '''declarationExpression : FINAL IDENTIFIER EQUAL expression SEMICOLON
    '''



# SEMANTIC RULES

def p_semanticbool(p):
    ''' semanticbool : BOOL IDENTIFIER EQUAL conditions SEMICOLON
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

listidentifier = ""
listtype = ""
def p_semanticlist(p):
    ''' semanticlist : LIST LESSTHAN DYNAMIC GREATERTHAN IDENTIFIER EQUAL LSQUAREBRACKET insidelist RSQUAREBRACKET SEMICOLON
                    | LIST LESSTHAN  INT GREATERTHAN IDENTIFIER EQUAL LSQUAREBRACKET insidelistint RSQUAREBRACKET SEMICOLON
                    | LIST LESSTHAN  STRING GREATERTHAN IDENTIFIER EQUAL LSQUAREBRACKET insideliststr RSQUAREBRACKET SEMICOLON
                    | LIST LESSTHAN  BOOL GREATERTHAN IDENTIFIER EQUAL LSQUAREBRACKET insidelistbool RSQUAREBRACKET SEMICOLON
                    | LIST LESSTHAN  DOUBLE GREATERTHAN IDENTIFIER EQUAL LSQUAREBRACKET insidelistdouble RSQUAREBRACKET SEMICOLON
    '''
    global listidentifier
    global listtype
    listidentifier = p[5]
    listtype = p[3]


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


def p_addlistInt(p):
    ''' addlistInt : IDENTIFIER DOT ADD LPAREN INTEGER RPAREN SEMICOLON
    '''
    global listidentifier
    global listtype
    if p[1] == listidentifier and isinstance(int(p[5]), int) and listtype == "int":
        print("oooook")
    else:
        globals()['error'] = True
        cajaValidator.config(fg=rojo)
        cajaValidator.insert(tk.END, "Error: Se esperaba un número entero.")


def p_addlistStr(p):
    ''' addlistStr : IDENTIFIER DOT ADD LPAREN STR RPAREN SEMICOLON
    '''
    global listidentifier
    global listtype
    if p[1] == listidentifier and isinstance(p[5], str) and listtype == "String":
        print("oooook")
    else:
        globals()['error'] = True
        cajaValidator.config(fg=rojo)
        cajaValidator.insert(tk.END, "Error: Se esperaba un string.")


def p_addlistBool(p):
    ''' addlistBool : IDENTIFIER DOT ADD LPAREN booleanOp RPAREN SEMICOLON
    '''
    global listidentifier
    global listtype
    if p[1] == listidentifier and isinstance(bool(p[5]), bool) and listtype == "bool":
        print("oooook")
    else:
        globals()['error'] = True
        cajaValidator.config(fg=rojo)
        cajaValidator.insert(tk.END, "Error: Se esperaba un booleano.")


def p_addlistFloat(p):
    ''' addlistFloat : IDENTIFIER DOT ADD LPAREN FLOAT RPAREN SEMICOLON
    '''
    global listidentifier
    global listtype
    if p[1] == listidentifier and isinstance(float(p[5]), float) and listtype == "double":
        print("oooook")
    else:
        globals()['error'] = True
        cajaValidator.config(fg=rojo)
        cajaValidator.insert(tk.END, "Error: Se esperaba un flotante.")


# LIST LESSTHAN  datatype GREATERTHAN IDENTIFIER EQUAL LSQUAREBRACKET insidelist RSQUAREBRACKET SEMICOLON

# returnType : INT| STRING| BOOL| DOUBLE| DYNAMIC| VOID| map_identifier



#SEMANTIC RULES RICARDO MOLINA
def p_declarationExpression_asignString(p):
    '''declarationExpression : STRING IDENTIFIER EQUAL expressionString SEMICOLON
                              | STRING IDENTIFIER SEMICOLON
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
                              | INT IDENTIFIER SEMICOLON

    '''
def p_expressionInteger(p):
     '''expressionInteger : number
                          | number operatorExpression expressionInteger
     '''
def p_expressionIntegerIdentifier(p):
    '''expressionInteger : IDENTIFIER
                         | IDENTIFIER operatorExpression expressionInteger
    '''

def p_properties(p):
    '''properties : KEYS
                   | VALUES
    '''
def p_propertiesAccess(p):
    '''  propertiesAccess : IDENTIFIER DOT properties
    '''


def p_error(p):
    globals()['error'] = True
    cajaValidator.config(fg=rojo)
    if p:
        cajaValidator.insert(tk.END, "Syntax error at token: " + p.type + "\n")
        print("Syntax error at token:", p.type)
        # sintactico.errok()
    else:
        cajaValidator.insert(tk.END, "Syntax error at EOF" + "\n")
        print("Syntax error at EOF")


# Build the parser
sintactico = yacc.yacc()

def detect_k():
    cajaCodigo.tag_config("start",
                          foreground="black")

    iF=1
    iC=0
    iFC=0
    codigo = cajaCodigo.get(1.0, "end-1c")
    iCC=0;
    palabra="";
    for indice in range(len(codigo)):
        if (codigo[indice] == "\n"):
            iF += 1
            iC = 0
            iFC = 0
            iCC = 0
            palabra=""
        elif codigo[indice] == " " or not codigo[indice].isalpha():

            iC = iCC+1
            iFC = iCC+1
            iCC += 1
            palabra = ""
        else:
            palabra = palabra+codigo[indice]
            iFC+=1
            iCC += 1
        #print(palabra,iF,iC,iFC)
        if indice+1 < len(codigo):
            if codigo[indice+1] == " " or not codigo[indice+1].isalpha():
                if palabra in palabras:
                    pos1=str(iF)+"."+str(iC)
                    pos2=str(iF)+"."+str(iFC)
                    iC=iFC
                    cajaCodigo.tag_add("start", pos1, pos2)
                    # configuring a tag called start
                    cajaCodigo.tag_config("start",
                            foreground="#03589C")
        else:
            if palabra in palabras:
                pos1 = str(iF) + "." + str(iC)
                pos2 = str(iF) + "." + str(iFC)
                iC = iFC
                cajaCodigo.tag_add("start", pos1, pos2)
                # configuring a tag called start
                cajaCodigo.tag_config("start",
                                      foreground="#03589C")


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
    detect_k()

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








