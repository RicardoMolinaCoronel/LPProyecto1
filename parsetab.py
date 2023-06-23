
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSAND AND APOSTROPHE ASYNC AWAIT BOOL BOOLEAN CATCH CLOSE COLON COMMA COMMENT DIVISION DOLLAR DOT DOUBLE DOUBLEQUAL DOUBQUOTMARK DYNAMIC ELSE EQUAL EXIT EXMARK FILE FLOAT FOR GREATERTHAN IDENTIFIER IF IMPORT IN INT INTEGER IS ITERABLE LCURLYBRACKET LESSTHAN LIST LPAREN LSQUAREBRACKET MAIN MAP METHOD MINUS NOTEQUAL OPENWRITE OR PLUS PRINT RCURLYBRACKET READLINESYNC REQUIRED RETURN RPAREN RSQUAREBRACKET SEMICOLON SET STR STRING TIMES TRY VAR VOID WHILE WRITEclass : map ifElseStatement function_lambdamap : map_identifier IDENTIFIER EQUAL LCURLYBRACKET map_content RCURLYBRACKET SEMICOLONmap_identifier : MAP\n                     | MAP map_type_specified\n  map_type_specified : LESSTHAN datatype COMMA datatype GREATERTHANdatatype : INT\n               | STRING\n               | BOOL\n               | DOUBLE\n               | DYNAMIC\n               | VAR\n               | VOID\n               | map_identifier\n  returnType : INT\n                 | STRING\n                 | BOOL\n                 | DOUBLE\n                 | DYNAMIC\n                 | VOID\n                 | map_identifier\n  empty :map_content : map_pairs\n                  | empty\n  map_pair : map_key COLON map_valuemap_pairs : map_pair\n                | map_pair COMMA map_pairs\n  map_key : value\n  map_value : value\n  ifElseStatement : ifStatement\n                      | ifStatement elifStatement_repeat\n  elifStatement_repeat : elifStatement\n                           | elifStatement elifStatement_repeat\n  ifStatement : IF LPAREN conditions RPAREN LCURLYBRACKET RCURLYBRACKET\n  elifStatement : ELSE ifStatement\n  elifStatement : ELSE LCURLYBRACKET RCURLYBRACKET\n  value : INTEGER\n              | FLOAT\n              | STR\n              | BOOLEAN\n              | IDENTIFIER\n  deniable_values : IDENTIFIER\n                      | BOOLEAN\n  negation_values : deniable_values\n                     | EXMARK deniable_values\n  condition_values : negation_values\n                      | INTEGER\n                      | FLOAT\n                      | STR\n  condition_operator : DOUBLEQUAL\n                         | LESSTHAN\n                         | GREATERTHAN\n  number : FLOAT\n             | INTEGER\n  condition : IDENTIFIER condition_operator condition_values\n                | EXMARK IDENTIFIER condition_operator condition_values\n                | BOOLEAN condition_operator BOOLEAN\n                | number condition_operator number\n                | STR condition_operator STR\n  conditions : condition\n                 | condition condition_connector conditions\n  condition_connector : AND\n                          | OR\n  function_lambda : returnType IDENTIFIER LPAREN function_arguments_repeat optFunction_argumentsExpression RPAREN EQUAL GREATERTHAN expression SEMICOLON\n   function_argument : datatype IDENTIFIER\n                         | empty\n  function_arguments_repeat : function_argument\n                                | function_argument COMMA function_arguments_repeat\n   optFunction_argumentsExpression : LCURLYBRACKET optFunction_arguments RCURLYBRACKET\n                                       | empty\n  optFunction_argument : REQUIRED datatype IDENTIFIER\n  optFunction_arguments : optFunction_argument\n                            | optFunction_argument COMMA optFunction_arguments\n  expression : IDENTIFIER PLUS IDENTIFIER\n  '
    
_lr_action_items = {'MAP':([0,5,6,10,20,21,35,36,48,49,50,101,103,113,],[4,4,-29,4,-30,-31,-32,-34,4,4,-35,4,-33,4,]),'$end':([1,11,125,],[0,-1,-63,]),'IF':([2,22,106,],[7,7,-2,]),'IDENTIFIER':([3,4,9,12,13,14,15,16,17,18,19,23,26,27,28,29,30,31,32,33,41,47,52,53,54,55,56,57,58,77,88,90,95,96,97,118,119,124,],[8,-3,-4,34,-14,-15,-16,-17,-18,-19,-20,40,-6,-7,-8,-9,-10,-11,-12,-13,59,63,40,-61,-62,81,-49,-50,-51,102,81,81,63,63,-5,121,122,126,]),'COMMA':([4,9,25,26,27,28,29,30,31,32,33,49,63,67,70,71,72,73,76,78,97,101,102,108,109,112,121,],[-3,-4,48,-6,-7,-8,-9,-10,-11,-12,-13,-21,-40,95,-36,-37,-38,-39,101,-65,-5,-21,-64,-24,-28,117,-70,]),'GREATERTHAN':([4,9,26,27,28,29,30,31,32,33,40,42,43,44,45,46,59,74,97,115,],[-3,-4,-6,-7,-8,-9,-10,-11,-12,-13,58,58,58,58,-52,-53,58,97,-5,119,]),'LESSTHAN':([4,40,42,43,44,45,46,59,],[10,57,57,57,57,-52,-53,57,]),'INT':([5,6,10,20,21,35,36,48,49,50,101,103,113,],[13,-29,26,-30,-31,-32,-34,26,26,-35,26,-33,26,]),'STRING':([5,6,10,20,21,35,36,48,49,50,101,103,113,],[14,-29,27,-30,-31,-32,-34,27,27,-35,27,-33,27,]),'BOOL':([5,6,10,20,21,35,36,48,49,50,101,103,113,],[15,-29,28,-30,-31,-32,-34,28,28,-35,28,-33,28,]),'DOUBLE':([5,6,10,20,21,35,36,48,49,50,101,103,113,],[16,-29,29,-30,-31,-32,-34,29,29,-35,29,-33,29,]),'DYNAMIC':([5,6,10,20,21,35,36,48,49,50,101,103,113,],[17,-29,30,-30,-31,-32,-34,30,30,-35,30,-33,30,]),'VOID':([5,6,10,20,21,35,36,48,49,50,101,103,113,],[18,-29,32,-30,-31,-32,-34,32,32,-35,32,-33,32,]),'ELSE':([6,21,36,50,103,],[22,22,-34,-35,-33,]),'LPAREN':([7,34,],[23,49,]),'EQUAL':([8,110,],[24,115,]),'VAR':([10,48,49,101,113,],[31,31,31,31,31,]),'LCURLYBRACKET':([22,24,49,51,75,76,78,101,102,114,],[37,47,-21,79,99,-66,-65,-21,-64,-67,]),'EXMARK':([23,52,53,54,55,56,57,58,90,],[41,41,-61,-62,88,-49,-50,-51,88,]),'BOOLEAN':([23,47,52,53,54,55,56,57,58,60,88,90,95,96,],[42,73,42,-61,-62,89,-49,-50,-51,91,89,89,73,73,]),'STR':([23,47,52,53,54,55,56,57,58,62,90,95,96,],[44,72,44,-61,-62,86,-49,-50,-51,93,86,72,72,]),'FLOAT':([23,47,52,53,54,55,56,57,58,61,90,95,96,],[45,71,45,-61,-62,85,-49,-50,-51,45,85,71,71,]),'INTEGER':([23,47,52,53,54,55,56,57,58,61,90,95,96,],[46,70,46,-61,-62,84,-49,-50,-51,46,84,70,70,]),'RCURLYBRACKET':([37,47,63,64,65,66,67,70,71,72,73,79,107,108,109,111,112,120,121,],[50,-21,-40,94,-22,-23,-25,-36,-37,-38,-39,103,-26,-24,-28,116,-71,-72,-70,]),'RPAREN':([38,39,45,46,49,75,76,78,80,81,82,83,84,85,86,87,89,91,92,93,98,100,101,102,104,105,114,116,],[51,-59,-52,-53,-21,-21,-66,-65,-60,-41,-54,-45,-46,-47,-48,-43,-42,-56,-57,-58,110,-69,-21,-64,-44,-55,-67,-68,]),'AND':([39,45,46,81,82,83,84,85,86,87,89,91,92,93,104,105,],[53,-52,-53,-41,-54,-45,-46,-47,-48,-43,-42,-56,-57,-58,-44,-55,]),'OR':([39,45,46,81,82,83,84,85,86,87,89,91,92,93,104,105,],[54,-52,-53,-41,-54,-45,-46,-47,-48,-43,-42,-56,-57,-58,-44,-55,]),'DOUBLEQUAL':([40,42,43,44,45,46,59,],[56,56,56,56,-52,-53,56,]),'COLON':([63,68,69,70,71,72,73,],[-40,96,-27,-36,-37,-38,-39,]),'SEMICOLON':([94,123,126,],[106,125,-73,]),'REQUIRED':([99,117,],[113,113,]),'PLUS':([122,],[124,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'class':([0,],[1,]),'map':([0,],[2,]),'map_identifier':([0,5,10,48,49,101,113,],[3,19,33,33,33,33,33,]),'ifElseStatement':([2,],[5,]),'ifStatement':([2,22,],[6,36,]),'map_type_specified':([4,],[9,]),'function_lambda':([5,],[11,]),'returnType':([5,],[12,]),'elifStatement_repeat':([6,21,],[20,35,]),'elifStatement':([6,21,],[21,21,]),'datatype':([10,48,49,101,113,],[25,74,77,77,118,]),'conditions':([23,52,],[38,80,]),'condition':([23,52,],[39,39,]),'number':([23,52,61,],[43,43,92,]),'condition_connector':([39,],[52,]),'condition_operator':([40,42,43,44,59,],[55,60,61,62,90,]),'map_content':([47,],[64,]),'map_pairs':([47,95,],[65,107,]),'empty':([47,49,75,101,],[66,78,100,78,]),'map_pair':([47,95,],[67,67,]),'map_key':([47,95,],[68,68,]),'value':([47,95,96,],[69,69,109,]),'function_arguments_repeat':([49,101,],[75,114,]),'function_argument':([49,101,],[76,76,]),'condition_values':([55,90,],[82,105,]),'negation_values':([55,90,],[83,83,]),'deniable_values':([55,88,90,],[87,104,87,]),'optFunction_argumentsExpression':([75,],[98,]),'map_value':([96,],[108,]),'optFunction_arguments':([99,117,],[111,120,]),'optFunction_argument':([99,117,],[112,112,]),'expression':([119,],[123,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> class","S'",1,None,None,None),
  ('class -> map ifElseStatement function_lambda','class',3,'p_class','main.py',114),
  ('map -> map_identifier IDENTIFIER EQUAL LCURLYBRACKET map_content RCURLYBRACKET SEMICOLON','map',7,'p_map','main.py',117),
  ('map_identifier -> MAP','map_identifier',1,'p_map_identifier','main.py',120),
  ('map_identifier -> MAP map_type_specified','map_identifier',2,'p_map_identifier','main.py',121),
  ('map_type_specified -> LESSTHAN datatype COMMA datatype GREATERTHAN','map_type_specified',5,'p_map_type_specified','main.py',125),
  ('datatype -> INT','datatype',1,'p_datatype','main.py',128),
  ('datatype -> STRING','datatype',1,'p_datatype','main.py',129),
  ('datatype -> BOOL','datatype',1,'p_datatype','main.py',130),
  ('datatype -> DOUBLE','datatype',1,'p_datatype','main.py',131),
  ('datatype -> DYNAMIC','datatype',1,'p_datatype','main.py',132),
  ('datatype -> VAR','datatype',1,'p_datatype','main.py',133),
  ('datatype -> VOID','datatype',1,'p_datatype','main.py',134),
  ('datatype -> map_identifier','datatype',1,'p_datatype','main.py',135),
  ('returnType -> INT','returnType',1,'p_returnType','main.py',138),
  ('returnType -> STRING','returnType',1,'p_returnType','main.py',139),
  ('returnType -> BOOL','returnType',1,'p_returnType','main.py',140),
  ('returnType -> DOUBLE','returnType',1,'p_returnType','main.py',141),
  ('returnType -> DYNAMIC','returnType',1,'p_returnType','main.py',142),
  ('returnType -> VOID','returnType',1,'p_returnType','main.py',143),
  ('returnType -> map_identifier','returnType',1,'p_returnType','main.py',144),
  ('empty -> <empty>','empty',0,'p_empty','main.py',148),
  ('map_content -> map_pairs','map_content',1,'p_map_content','main.py',150),
  ('map_content -> empty','map_content',1,'p_map_content','main.py',151),
  ('map_pair -> map_key COLON map_value','map_pair',3,'p_map_pair','main.py',155),
  ('map_pairs -> map_pair','map_pairs',1,'p_map_pairs','main.py',157),
  ('map_pairs -> map_pair COMMA map_pairs','map_pairs',3,'p_map_pairs','main.py',158),
  ('map_key -> value','map_key',1,'p_map_key','main.py',162),
  ('map_value -> value','map_value',1,'p_map_value','main.py',165),
  ('ifElseStatement -> ifStatement','ifElseStatement',1,'p_ifElseStatement','main.py',169),
  ('ifElseStatement -> ifStatement elifStatement_repeat','ifElseStatement',2,'p_ifElseStatement','main.py',170),
  ('elifStatement_repeat -> elifStatement','elifStatement_repeat',1,'p_elifStatement_repeat','main.py',174),
  ('elifStatement_repeat -> elifStatement elifStatement_repeat','elifStatement_repeat',2,'p_elifStatement_repeat','main.py',175),
  ('ifStatement -> IF LPAREN conditions RPAREN LCURLYBRACKET RCURLYBRACKET','ifStatement',6,'p_ifStatement','main.py',178),
  ('elifStatement -> ELSE ifStatement','elifStatement',2,'p_elifStatement','main.py',182),
  ('elifStatement -> ELSE LCURLYBRACKET RCURLYBRACKET','elifStatement',3,'p_elseStatement','main.py',185),
  ('value -> INTEGER','value',1,'p_value','main.py',189),
  ('value -> FLOAT','value',1,'p_value','main.py',190),
  ('value -> STR','value',1,'p_value','main.py',191),
  ('value -> BOOLEAN','value',1,'p_value','main.py',192),
  ('value -> IDENTIFIER','value',1,'p_value','main.py',193),
  ('deniable_values -> IDENTIFIER','deniable_values',1,'p_deniable_values','main.py',197),
  ('deniable_values -> BOOLEAN','deniable_values',1,'p_deniable_values','main.py',198),
  ('negation_values -> deniable_values','negation_values',1,'p_negation_values','main.py',201),
  ('negation_values -> EXMARK deniable_values','negation_values',2,'p_negation_values','main.py',202),
  ('condition_values -> negation_values','condition_values',1,'p_condition_values','main.py',206),
  ('condition_values -> INTEGER','condition_values',1,'p_condition_values','main.py',207),
  ('condition_values -> FLOAT','condition_values',1,'p_condition_values','main.py',208),
  ('condition_values -> STR','condition_values',1,'p_condition_values','main.py',209),
  ('condition_operator -> DOUBLEQUAL','condition_operator',1,'p_condition_operator','main.py',212),
  ('condition_operator -> LESSTHAN','condition_operator',1,'p_condition_operator','main.py',213),
  ('condition_operator -> GREATERTHAN','condition_operator',1,'p_condition_operator','main.py',214),
  ('number -> FLOAT','number',1,'p_number','main.py',217),
  ('number -> INTEGER','number',1,'p_number','main.py',218),
  ('condition -> IDENTIFIER condition_operator condition_values','condition',3,'p_condition','main.py',221),
  ('condition -> EXMARK IDENTIFIER condition_operator condition_values','condition',4,'p_condition','main.py',222),
  ('condition -> BOOLEAN condition_operator BOOLEAN','condition',3,'p_condition','main.py',223),
  ('condition -> number condition_operator number','condition',3,'p_condition','main.py',224),
  ('condition -> STR condition_operator STR','condition',3,'p_condition','main.py',225),
  ('conditions -> condition','conditions',1,'p_conditions','main.py',229),
  ('conditions -> condition condition_connector conditions','conditions',3,'p_conditions','main.py',230),
  ('condition_connector -> AND','condition_connector',1,'p_condition_connector','main.py',234),
  ('condition_connector -> OR','condition_connector',1,'p_condition_connector','main.py',235),
  ('function_lambda -> returnType IDENTIFIER LPAREN function_arguments_repeat optFunction_argumentsExpression RPAREN EQUAL GREATERTHAN expression SEMICOLON','function_lambda',10,'p_function_lambda','main.py',239),
  ('function_argument -> datatype IDENTIFIER','function_argument',2,'p_function_argument','main.py',243),
  ('function_argument -> empty','function_argument',1,'p_function_argument','main.py',244),
  ('function_arguments_repeat -> function_argument','function_arguments_repeat',1,'p_function_arguments_repeat','main.py',248),
  ('function_arguments_repeat -> function_argument COMMA function_arguments_repeat','function_arguments_repeat',3,'p_function_arguments_repeat','main.py',249),
  ('optFunction_argumentsExpression -> LCURLYBRACKET optFunction_arguments RCURLYBRACKET','optFunction_argumentsExpression',3,'p_optFunction_argumentsExpression','main.py',253),
  ('optFunction_argumentsExpression -> empty','optFunction_argumentsExpression',1,'p_optFunction_argumentsExpression','main.py',254),
  ('optFunction_argument -> REQUIRED datatype IDENTIFIER','optFunction_argument',3,'p_optFunction_argument','main.py',257),
  ('optFunction_arguments -> optFunction_argument','optFunction_arguments',1,'p_optFunction_arguments','main.py',261),
  ('optFunction_arguments -> optFunction_argument COMMA optFunction_arguments','optFunction_arguments',3,'p_optFunction_arguments','main.py',262),
  ('expression -> IDENTIFIER PLUS IDENTIFIER','expression',3,'p_expression','main.py',266),
]
