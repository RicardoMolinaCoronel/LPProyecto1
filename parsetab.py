
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSAND AND APOSTROPHE ASYNC AWAIT BOOL BOOLEAN CATCH CLOSE COLON COMMA COMMENT DIVISION DOLLAR DOT DOUBLE DOUBLEQUAL DOUBQUOTMARK DYNAMIC ELSE EQUAL EXIT EXMARK FILE FINAL FLOAT FOR GREATERTHAN IDENTIFIER IF IMPORT IN INT INTEGER IS ITERABLE LCURLYBRACKET LESSTHAN LIST LPAREN LSQUAREBRACKET MAIN MAP METHOD MINUS NOTEQUAL OF OPENWRITE OR PLUS PRINT RCURLYBRACKET READLINESYNC REQUIRED RETURN RPAREN RSQUAREBRACKET SEMICOLON SET STACK STR STRING TIMES TRY VAR VOID WHILE WRITEclass : class_content_repeatclass_content : map\n  class_content : ifElseStatement\n  class_content : function_lambda\n  class_content : declarationExpression\n  class_content : inferedReturnFunction\n  class_content : expression SEMICOLON\n  class_content_repeat : class_content\n                           | class_content_repeat class_content\n  map : map_identifier IDENTIFIER EQUAL LCURLYBRACKET map_content RCURLYBRACKET SEMICOLONmap_identifier : MAP\n                     | MAP map_type_specified\n  map_type_specified : LESSTHAN datatype COMMA datatype GREATERTHANdatatype : returnType\n               | VAR\n  returnType : INT\n                 | STRING\n                 | BOOL\n                 | DOUBLE\n                 | DYNAMIC\n                 | VOID\n                 | map_identifier\n  empty :map_content : map_pairs\n                  | empty\n  map_pair : map_key COLON map_valuemap_pairs : map_pair\n                | map_pair COMMA map_pairs\n  map_key : value\n  map_value : value\n  ifElseStatement : ifStatement\n                      | ifStatement elifStatement_repeat\n  elifStatement_repeat : elifStatement\n                           | elifStatement elifStatement_repeat\n  ifStatement : IF LPAREN conditions RPAREN LCURLYBRACKET class_content_repeat RCURLYBRACKET\n  elifStatement : ELSE ifStatement\n  elifStatement : ELSE LCURLYBRACKET class_content_repeat RCURLYBRACKET\n  forStatement : FOR LPAREN declarationExpression SEMICOLON conditions SEMICOLON taskStatement RPAREN LCURLYBRACKET class_content_repeat RCURLYBRACKET\n  taskStatement : IDENTIFIER PLUS PLUS\n                    | IDENTIFIER MINUS MINUS\n  stack : FINAL IDENTIFIER EQUAL STACK LESSTHAN datatype GREATERTHAN LPAREN opt_value RPAREN SEMICOLON\nstack : FINAL IDENTIFIER EQUAL STACK LESSTHAN datatype GREATERTHAN SEMICOLON\n          | FINAL IDENTIFIER EQUAL STACK DOT OF LPAREN IDENTIFIER RPAREN SEMICOLON\n  inferedReturnFunction : IDENTIFIER LPAREN  function_arguments_repeat RPAREN LCURLYBRACKET RETURN expression SEMICOLON RCURLYBRACKET\n\n  value : INTEGER\n              | FLOAT\n              | STR\n              | BOOLEAN\n              | IDENTIFIER\n  opt_value : value\n                | empty\n  deniable_values : IDENTIFIER\n                      | BOOLEAN\n  negation_values : deniable_values\n                     | EXMARK deniable_values\n  condition_values : negation_values\n                      | INTEGER\n                      | FLOAT\n                      | STR\n  condition_operator : DOUBLEQUAL\n                         | LESSTHAN\n                         | GREATERTHAN\n  number : FLOAT\n             | INTEGER\n  condition : IDENTIFIER condition_operator condition_values\n                | EXMARK IDENTIFIER condition_operator condition_values\n                | BOOLEAN condition_operator BOOLEAN\n                | number condition_operator number\n                | STR condition_operator STR\n  conditions : condition\n                 | condition condition_connector conditions\n  condition_connector : AND\n                          | OR\n  function_lambda : datatype IDENTIFIER LPAREN function_arguments_repeat optFunction_argumentsExpression RPAREN EQUAL GREATERTHAN expression SEMICOLON\n   function_argument : datatype IDENTIFIER\n                        | empty\n\n  function_arguments_repeat : function_argument\n                                | function_argument COMMA function_arguments_repeat\n   optFunction_argumentsExpression : LCURLYBRACKET optFunction_arguments RCURLYBRACKET\n                                       | empty\n\n  optFunction_argument : REQUIRED datatype IDENTIFIER\n\n  optFunction_arguments : optFunction_argument\n                            | optFunction_argument COMMA optFunction_arguments\n  expression : operableTypes operatorExpression operableTypes\n                  | value\n  operableTypes : IDENTIFIER\n                    | number\n\n  operatorExpression : PLUS\n                         | MINUS\n                         | TIMES\n                         | DIVISION\n  declarationExpression : datatype IDENTIFIER SEMICOLON\n  declarationExpression : datatype IDENTIFIER EQUAL expression SEMICOLON\n  '
    
_lr_action_items = {'IDENTIFIER':([0,2,3,4,5,6,7,8,10,12,13,16,18,19,25,26,27,28,29,30,31,32,35,36,39,40,41,42,43,44,46,50,52,53,54,55,57,58,67,71,75,81,82,83,84,85,86,87,103,107,109,118,120,125,126,127,132,133,136,144,145,147,150,152,],[11,11,-8,-2,-3,-4,-5,-6,33,-31,38,-11,-14,-15,-16,-17,-18,-19,-20,-21,-9,-7,-32,-33,60,-88,-89,-90,-91,-12,66,74,-22,-34,-36,11,77,-92,88,92,11,66,-72,-73,111,-60,-61,-62,-37,-93,11,111,111,92,92,77,-13,11,-10,149,-35,77,-44,-74,]),'MAP':([0,2,3,4,5,6,7,8,12,31,32,34,35,36,45,53,54,55,56,58,73,75,79,103,107,109,131,133,136,145,150,152,],[16,16,-8,-2,-3,-4,-5,-6,-31,-9,-7,16,-32,-33,16,-34,-36,16,16,-92,16,16,16,-37,-93,16,16,16,-10,-35,-44,-74,]),'IF':([0,2,3,4,5,6,7,8,12,31,32,35,36,37,53,54,55,58,75,103,107,109,133,136,145,150,152,],[17,17,-8,-2,-3,-4,-5,-6,-31,-9,-7,-32,-33,17,-34,-36,17,-92,17,-37,-93,17,17,-10,-35,-44,-74,]),'VAR':([0,2,3,4,5,6,7,8,12,31,32,34,35,36,45,53,54,55,56,58,73,75,79,103,107,109,131,133,136,145,150,152,],[19,19,-8,-2,-3,-4,-5,-6,-31,-9,-7,19,-32,-33,19,-34,-36,19,19,-92,19,19,19,-37,-93,19,19,19,-10,-35,-44,-74,]),'INTEGER':([0,2,3,4,5,6,7,8,12,31,32,35,36,39,40,41,42,43,46,53,54,55,57,58,71,75,81,82,83,84,85,86,87,90,103,107,109,120,125,126,127,133,136,145,147,150,152,],[21,21,-8,-2,-3,-4,-5,-6,-31,-9,-7,-32,-33,62,-88,-89,-90,-91,62,-34,-36,21,21,-92,99,21,62,-72,-73,114,-60,-61,-62,62,-37,-93,21,114,99,99,21,21,-10,-35,21,-44,-74,]),'FLOAT':([0,2,3,4,5,6,7,8,12,31,32,35,36,39,40,41,42,43,46,53,54,55,57,58,71,75,81,82,83,84,85,86,87,90,103,107,109,120,125,126,127,133,136,145,147,150,152,],[22,22,-8,-2,-3,-4,-5,-6,-31,-9,-7,-32,-33,61,-88,-89,-90,-91,61,-34,-36,22,22,-92,100,22,61,-72,-73,115,-60,-61,-62,61,-37,-93,22,115,100,100,22,22,-10,-35,22,-44,-74,]),'STR':([0,2,3,4,5,6,7,8,12,31,32,35,36,46,53,54,55,57,58,71,75,81,82,83,84,85,86,87,91,103,107,109,120,125,126,127,133,136,145,147,150,152,],[23,23,-8,-2,-3,-4,-5,-6,-31,-9,-7,-32,-33,70,-34,-36,23,23,-92,23,23,70,-72,-73,116,-60,-61,-62,123,-37,-93,23,116,23,23,23,23,-10,-35,23,-44,-74,]),'BOOLEAN':([0,2,3,4,5,6,7,8,12,31,32,35,36,46,53,54,55,57,58,71,75,81,82,83,84,85,86,87,89,103,107,109,118,120,125,126,127,133,136,145,147,150,152,],[24,24,-8,-2,-3,-4,-5,-6,-31,-9,-7,-32,-33,68,-34,-36,24,24,-92,24,24,68,-72,-73,119,-60,-61,-62,121,-37,-93,24,119,119,24,24,24,24,-10,-35,24,-44,-74,]),'INT':([0,2,3,4,5,6,7,8,12,31,32,34,35,36,45,53,54,55,56,58,73,75,79,103,107,109,131,133,136,145,150,152,],[25,25,-8,-2,-3,-4,-5,-6,-31,-9,-7,25,-32,-33,25,-34,-36,25,25,-92,25,25,25,-37,-93,25,25,25,-10,-35,-44,-74,]),'STRING':([0,2,3,4,5,6,7,8,12,31,32,34,35,36,45,53,54,55,56,58,73,75,79,103,107,109,131,133,136,145,150,152,],[26,26,-8,-2,-3,-4,-5,-6,-31,-9,-7,26,-32,-33,26,-34,-36,26,26,-92,26,26,26,-37,-93,26,26,26,-10,-35,-44,-74,]),'BOOL':([0,2,3,4,5,6,7,8,12,31,32,34,35,36,45,53,54,55,56,58,73,75,79,103,107,109,131,133,136,145,150,152,],[27,27,-8,-2,-3,-4,-5,-6,-31,-9,-7,27,-32,-33,27,-34,-36,27,27,-92,27,27,27,-37,-93,27,27,27,-10,-35,-44,-74,]),'DOUBLE':([0,2,3,4,5,6,7,8,12,31,32,34,35,36,45,53,54,55,56,58,73,75,79,103,107,109,131,133,136,145,150,152,],[28,28,-8,-2,-3,-4,-5,-6,-31,-9,-7,28,-32,-33,28,-34,-36,28,28,-92,28,28,28,-37,-93,28,28,28,-10,-35,-44,-74,]),'DYNAMIC':([0,2,3,4,5,6,7,8,12,31,32,34,35,36,45,53,54,55,56,58,73,75,79,103,107,109,131,133,136,145,150,152,],[29,29,-8,-2,-3,-4,-5,-6,-31,-9,-7,29,-32,-33,29,-34,-36,29,29,-92,29,29,29,-37,-93,29,29,29,-10,-35,-44,-74,]),'VOID':([0,2,3,4,5,6,7,8,12,31,32,34,35,36,45,53,54,55,56,58,73,75,79,103,107,109,131,133,136,145,150,152,],[30,30,-8,-2,-3,-4,-5,-6,-31,-9,-7,30,-32,-33,30,-34,-36,30,30,-92,30,30,30,-37,-93,30,30,30,-10,-35,-44,-74,]),'$end':([1,2,3,4,5,6,7,8,12,31,32,35,36,53,54,58,103,107,136,145,150,152,],[0,-1,-8,-2,-3,-4,-5,-6,-31,-9,-7,-32,-33,-34,-36,-92,-37,-93,-10,-35,-44,-74,]),'RCURLYBRACKET':([3,4,5,6,7,8,12,23,24,31,32,35,36,53,54,58,71,75,92,93,94,95,96,99,100,103,107,129,130,133,136,137,138,139,145,146,148,149,150,152,],[-8,-2,-3,-4,-5,-6,-31,-47,-48,-9,-7,-32,-33,-34,-36,-92,-23,103,-49,124,-24,-25,-27,-45,-46,-37,-93,142,-82,145,-10,-28,-26,-30,-35,150,-83,-81,-44,-74,]),'SEMICOLON':([9,11,15,20,21,22,23,24,38,59,60,61,62,77,78,124,140,151,],[32,-49,-85,-87,-45,-46,-47,-48,58,-84,-86,-63,-64,-49,107,136,146,152,]),'LPAREN':([11,17,38,],[34,46,56,]),'PLUS':([11,14,20,21,22,77,],[-86,40,-87,-64,-63,-86,]),'MINUS':([11,14,20,21,22,77,],[-86,41,-87,-64,-63,-86,]),'TIMES':([11,14,20,21,22,77,],[-86,42,-87,-64,-63,-86,]),'DIVISION':([11,14,20,21,22,77,],[-86,43,-87,-64,-63,-86,]),'ELSE':([12,36,54,103,145,],[37,37,-36,-37,-35,]),'COMMA':([16,18,19,23,24,25,26,27,28,29,30,34,44,49,51,52,56,63,73,74,92,96,99,100,130,132,138,139,149,],[-11,-14,-15,-47,-48,-16,-17,-18,-19,-20,-21,-23,-12,73,-76,-22,-23,79,-23,-75,-49,125,-45,-46,143,-13,-26,-30,-81,]),'GREATERTHAN':([16,18,19,25,26,27,28,29,30,44,52,61,62,66,68,69,70,88,108,132,141,],[-11,-14,-15,-16,-17,-18,-19,-20,-21,-12,-22,-63,-64,87,87,87,87,87,132,-13,147,]),'LESSTHAN':([16,61,62,66,68,69,70,88,],[45,-63,-64,86,86,86,86,86,]),'COLON':([23,24,92,97,98,99,100,],[-47,-48,-49,126,-29,-45,-46,]),'EQUAL':([33,38,128,],[47,57,141,]),'RPAREN':([34,48,49,51,56,61,62,64,65,73,74,76,102,104,106,110,111,112,113,114,115,116,117,119,121,122,123,134,135,142,],[-23,72,-77,-76,-23,-63,-64,80,-70,-23,-75,-23,-78,128,-80,-71,-52,-65,-56,-57,-58,-59,-54,-53,-67,-68,-69,-55,-66,-79,]),'LCURLYBRACKET':([37,47,49,51,56,72,73,74,76,80,102,],[55,71,-77,-76,-23,101,-23,-75,105,109,-78,]),'EXMARK':([46,81,82,83,84,85,86,87,120,],[67,67,-72,-73,118,-60,-61,-62,118,]),'DOUBLEQUAL':([61,62,66,68,69,70,88,],[-63,-64,85,85,85,85,85,]),'AND':([61,62,65,111,112,113,114,115,116,117,119,121,122,123,134,135,],[-63,-64,82,-52,-65,-56,-57,-58,-59,-54,-53,-67,-68,-69,-55,-66,]),'OR':([61,62,65,111,112,113,114,115,116,117,119,121,122,123,134,135,],[-63,-64,83,-52,-65,-56,-57,-58,-59,-54,-53,-67,-68,-69,-55,-66,]),'RETURN':([101,],[127,]),'REQUIRED':([105,143,],[131,131,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'class':([0,],[1,]),'class_content_repeat':([0,55,109,],[2,75,133,]),'class_content':([0,2,55,75,109,133,],[3,31,3,31,3,31,]),'map':([0,2,55,75,109,133,],[4,4,4,4,4,4,]),'ifElseStatement':([0,2,55,75,109,133,],[5,5,5,5,5,5,]),'function_lambda':([0,2,55,75,109,133,],[6,6,6,6,6,6,]),'declarationExpression':([0,2,55,75,109,133,],[7,7,7,7,7,7,]),'inferedReturnFunction':([0,2,55,75,109,133,],[8,8,8,8,8,8,]),'expression':([0,2,55,57,75,109,127,133,147,],[9,9,9,78,9,9,140,9,151,]),'map_identifier':([0,2,34,45,55,56,73,75,79,109,131,133,],[10,10,52,52,10,52,52,10,52,10,52,10,]),'ifStatement':([0,2,37,55,75,109,133,],[12,12,54,12,12,12,12,]),'datatype':([0,2,34,45,55,56,73,75,79,109,131,133,],[13,13,50,63,13,50,50,13,108,13,144,13,]),'operableTypes':([0,2,39,55,57,75,109,127,133,147,],[14,14,59,14,14,14,14,14,14,14,]),'value':([0,2,55,57,71,75,109,125,126,127,133,147,],[15,15,15,15,98,15,15,98,139,15,15,15,]),'returnType':([0,2,34,45,55,56,73,75,79,109,131,133,],[18,18,18,18,18,18,18,18,18,18,18,18,]),'number':([0,2,39,46,55,57,75,81,90,109,127,133,147,],[20,20,20,69,20,20,20,69,122,20,20,20,20,]),'elifStatement_repeat':([12,36,],[35,53,]),'elifStatement':([12,36,],[36,36,]),'operatorExpression':([14,],[39,]),'map_type_specified':([16,],[44,]),'function_arguments_repeat':([34,56,73,],[48,76,102,]),'function_argument':([34,56,73,],[49,49,49,]),'empty':([34,56,71,73,76,],[51,51,95,51,106,]),'conditions':([46,81,],[64,110,]),'condition':([46,81,],[65,65,]),'condition_connector':([65,],[81,]),'condition_operator':([66,68,69,70,88,],[84,89,90,91,120,]),'map_content':([71,],[93,]),'map_pairs':([71,125,],[94,137,]),'map_pair':([71,125,],[96,96,]),'map_key':([71,125,],[97,97,]),'optFunction_argumentsExpression':([76,],[104,]),'condition_values':([84,120,],[112,135,]),'negation_values':([84,120,],[113,113,]),'deniable_values':([84,118,120,],[117,134,117,]),'optFunction_arguments':([105,143,],[129,148,]),'optFunction_argument':([105,143,],[130,130,]),'map_value':([126,],[138,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> class","S'",1,None,None,None),
  ('class -> class_content_repeat','class',1,'p_class','main.py',140),
  ('class_content -> map','class_content',1,'p_class_content_map','main.py',143),
  ('class_content -> ifElseStatement','class_content',1,'p_class_content_ifElse','main.py',146),
  ('class_content -> function_lambda','class_content',1,'p_class_content_lambdaFunction','main.py',149),
  ('class_content -> declarationExpression','class_content',1,'p_class_content_declarationExpression','main.py',152),
  ('class_content -> inferedReturnFunction','class_content',1,'p_class_content_inferedFunction','main.py',155),
  ('class_content -> expression SEMICOLON','class_content',2,'p_class_content_expression','main.py',158),
  ('class_content_repeat -> class_content','class_content_repeat',1,'p_class_content_repeat','main.py',161),
  ('class_content_repeat -> class_content_repeat class_content','class_content_repeat',2,'p_class_content_repeat','main.py',162),
  ('map -> map_identifier IDENTIFIER EQUAL LCURLYBRACKET map_content RCURLYBRACKET SEMICOLON','map',7,'p_map','main.py',165),
  ('map_identifier -> MAP','map_identifier',1,'p_map_identifier','main.py',168),
  ('map_identifier -> MAP map_type_specified','map_identifier',2,'p_map_identifier','main.py',169),
  ('map_type_specified -> LESSTHAN datatype COMMA datatype GREATERTHAN','map_type_specified',5,'p_map_type_specified','main.py',173),
  ('datatype -> returnType','datatype',1,'p_datatype','main.py',176),
  ('datatype -> VAR','datatype',1,'p_datatype','main.py',177),
  ('returnType -> INT','returnType',1,'p_returnType','main.py',180),
  ('returnType -> STRING','returnType',1,'p_returnType','main.py',181),
  ('returnType -> BOOL','returnType',1,'p_returnType','main.py',182),
  ('returnType -> DOUBLE','returnType',1,'p_returnType','main.py',183),
  ('returnType -> DYNAMIC','returnType',1,'p_returnType','main.py',184),
  ('returnType -> VOID','returnType',1,'p_returnType','main.py',185),
  ('returnType -> map_identifier','returnType',1,'p_returnType','main.py',186),
  ('empty -> <empty>','empty',0,'p_empty','main.py',190),
  ('map_content -> map_pairs','map_content',1,'p_map_content','main.py',192),
  ('map_content -> empty','map_content',1,'p_map_content','main.py',193),
  ('map_pair -> map_key COLON map_value','map_pair',3,'p_map_pair','main.py',196),
  ('map_pairs -> map_pair','map_pairs',1,'p_map_pairs','main.py',198),
  ('map_pairs -> map_pair COMMA map_pairs','map_pairs',3,'p_map_pairs','main.py',199),
  ('map_key -> value','map_key',1,'p_map_key','main.py',202),
  ('map_value -> value','map_value',1,'p_map_value','main.py',205),
  ('ifElseStatement -> ifStatement','ifElseStatement',1,'p_ifElseStatement','main.py',209),
  ('ifElseStatement -> ifStatement elifStatement_repeat','ifElseStatement',2,'p_ifElseStatement','main.py',210),
  ('elifStatement_repeat -> elifStatement','elifStatement_repeat',1,'p_elifStatement_repeat','main.py',214),
  ('elifStatement_repeat -> elifStatement elifStatement_repeat','elifStatement_repeat',2,'p_elifStatement_repeat','main.py',215),
  ('ifStatement -> IF LPAREN conditions RPAREN LCURLYBRACKET class_content_repeat RCURLYBRACKET','ifStatement',7,'p_ifStatement','main.py',218),
  ('elifStatement -> ELSE ifStatement','elifStatement',2,'p_elifStatement','main.py',222),
  ('elifStatement -> ELSE LCURLYBRACKET class_content_repeat RCURLYBRACKET','elifStatement',4,'p_elseStatement','main.py',225),
  ('forStatement -> FOR LPAREN declarationExpression SEMICOLON conditions SEMICOLON taskStatement RPAREN LCURLYBRACKET class_content_repeat RCURLYBRACKET','forStatement',11,'p_forStatement','main.py',229),
  ('taskStatement -> IDENTIFIER PLUS PLUS','taskStatement',3,'p_taskStatement','main.py',233),
  ('taskStatement -> IDENTIFIER MINUS MINUS','taskStatement',3,'p_taskStatement','main.py',234),
  ('stack -> FINAL IDENTIFIER EQUAL STACK LESSTHAN datatype GREATERTHAN LPAREN opt_value RPAREN SEMICOLON','stack',11,'p_stack','main.py',238),
  ('stack -> FINAL IDENTIFIER EQUAL STACK LESSTHAN datatype GREATERTHAN SEMICOLON','stack',8,'p_stackStatement','main.py',244),
  ('stack -> FINAL IDENTIFIER EQUAL STACK DOT OF LPAREN IDENTIFIER RPAREN SEMICOLON','stack',10,'p_stackStatement','main.py',245),
  ('inferedReturnFunction -> IDENTIFIER LPAREN function_arguments_repeat RPAREN LCURLYBRACKET RETURN expression SEMICOLON RCURLYBRACKET','inferedReturnFunction',9,'p_inferedReturnFunction','main.py',249),
  ('value -> INTEGER','value',1,'p_value','main.py',254),
  ('value -> FLOAT','value',1,'p_value','main.py',255),
  ('value -> STR','value',1,'p_value','main.py',256),
  ('value -> BOOLEAN','value',1,'p_value','main.py',257),
  ('value -> IDENTIFIER','value',1,'p_value','main.py',258),
  ('opt_value -> value','opt_value',1,'p_opt_value','main.py',261),
  ('opt_value -> empty','opt_value',1,'p_opt_value','main.py',262),
  ('deniable_values -> IDENTIFIER','deniable_values',1,'p_deniable_values','main.py',265),
  ('deniable_values -> BOOLEAN','deniable_values',1,'p_deniable_values','main.py',266),
  ('negation_values -> deniable_values','negation_values',1,'p_negation_values','main.py',269),
  ('negation_values -> EXMARK deniable_values','negation_values',2,'p_negation_values','main.py',270),
  ('condition_values -> negation_values','condition_values',1,'p_condition_values','main.py',274),
  ('condition_values -> INTEGER','condition_values',1,'p_condition_values','main.py',275),
  ('condition_values -> FLOAT','condition_values',1,'p_condition_values','main.py',276),
  ('condition_values -> STR','condition_values',1,'p_condition_values','main.py',277),
  ('condition_operator -> DOUBLEQUAL','condition_operator',1,'p_condition_operator','main.py',280),
  ('condition_operator -> LESSTHAN','condition_operator',1,'p_condition_operator','main.py',281),
  ('condition_operator -> GREATERTHAN','condition_operator',1,'p_condition_operator','main.py',282),
  ('number -> FLOAT','number',1,'p_number','main.py',285),
  ('number -> INTEGER','number',1,'p_number','main.py',286),
  ('condition -> IDENTIFIER condition_operator condition_values','condition',3,'p_condition','main.py',289),
  ('condition -> EXMARK IDENTIFIER condition_operator condition_values','condition',4,'p_condition','main.py',290),
  ('condition -> BOOLEAN condition_operator BOOLEAN','condition',3,'p_condition','main.py',291),
  ('condition -> number condition_operator number','condition',3,'p_condition','main.py',292),
  ('condition -> STR condition_operator STR','condition',3,'p_condition','main.py',293),
  ('conditions -> condition','conditions',1,'p_conditions','main.py',297),
  ('conditions -> condition condition_connector conditions','conditions',3,'p_conditions','main.py',298),
  ('condition_connector -> AND','condition_connector',1,'p_condition_connector','main.py',302),
  ('condition_connector -> OR','condition_connector',1,'p_condition_connector','main.py',303),
  ('function_lambda -> datatype IDENTIFIER LPAREN function_arguments_repeat optFunction_argumentsExpression RPAREN EQUAL GREATERTHAN expression SEMICOLON','function_lambda',10,'p_function_lambda','main.py',307),
  ('function_argument -> datatype IDENTIFIER','function_argument',2,'p_function_argument','main.py',311),
  ('function_argument -> empty','function_argument',1,'p_function_argument','main.py',312),
  ('function_arguments_repeat -> function_argument','function_arguments_repeat',1,'p_function_arguments_repeat','main.py',317),
  ('function_arguments_repeat -> function_argument COMMA function_arguments_repeat','function_arguments_repeat',3,'p_function_arguments_repeat','main.py',318),
  ('optFunction_argumentsExpression -> LCURLYBRACKET optFunction_arguments RCURLYBRACKET','optFunction_argumentsExpression',3,'p_optFunction_argumentsExpression','main.py',322),
  ('optFunction_argumentsExpression -> empty','optFunction_argumentsExpression',1,'p_optFunction_argumentsExpression','main.py',323),
  ('optFunction_argument -> REQUIRED datatype IDENTIFIER','optFunction_argument',3,'p_optFunction_argument','main.py',327),
  ('optFunction_arguments -> optFunction_argument','optFunction_arguments',1,'p_optFunction_arguments','main.py',332),
  ('optFunction_arguments -> optFunction_argument COMMA optFunction_arguments','optFunction_arguments',3,'p_optFunction_arguments','main.py',333),
  ('expression -> operableTypes operatorExpression operableTypes','expression',3,'p_expression','main.py',337),
  ('expression -> value','expression',1,'p_expression','main.py',338),
  ('operableTypes -> IDENTIFIER','operableTypes',1,'p_operablTypes','main.py',342),
  ('operableTypes -> number','operableTypes',1,'p_operablTypes','main.py',343),
  ('operatorExpression -> PLUS','operatorExpression',1,'p_operatorExpression','main.py',347),
  ('operatorExpression -> MINUS','operatorExpression',1,'p_operatorExpression','main.py',348),
  ('operatorExpression -> TIMES','operatorExpression',1,'p_operatorExpression','main.py',349),
  ('operatorExpression -> DIVISION','operatorExpression',1,'p_operatorExpression','main.py',350),
  ('declarationExpression -> datatype IDENTIFIER SEMICOLON','declarationExpression',3,'p_declarationExpression','main.py',354),
  ('declarationExpression -> datatype IDENTIFIER EQUAL expression SEMICOLON','declarationExpression',5,'p_declarationExpression_asign','main.py',358),
]
