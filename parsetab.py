
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSAND AND APOSTROPHE ASYNC AWAIT BOOL BOOLEAN CATCH CLOSE COLON COMMA COMMENT DIVISION DO DOLLAR DOT DOUBLE DOUBLEQUAL DOUBQUOTMARK DYNAMIC ELSE EQUAL EXIT EXMARK FILE FINAL FLOAT FOR GREATERTHAN IDENTIFIER IF IMPORT IN INT INTEGER IS ITERABLE LCURLYBRACKET LESSTHAN LIST LPAREN LSQUAREBRACKET MAIN MAP METHOD MINUS NOTEQUAL OF OPENWRITE OR PLUS PRINT RCURLYBRACKET READLINESYNC REQUIRED RETURN RPAREN RSQUAREBRACKET SEMICOLON SET STACK STR STRING TIMES TRY VAR VOID WHILE WRITEclass : class_content_repeatclass_content : map\n  class_content : ifElseStatement\n  class_content : function_lambda\n  class_content : declarationExpression\n  class_content : forStatement\n    class_content : while\n  class_content : stack\n  class_content : inferedReturnFunction\n  class_content : expression SEMICOLON\n  class_content_repeat : class_content\n                           | class_content_repeat class_content\n  map : map_identifier IDENTIFIER EQUAL LCURLYBRACKET map_content RCURLYBRACKET SEMICOLONmap_identifier : MAP\n                     | MAP map_type_specified\n  map_type_specified : LESSTHAN datatype COMMA datatype GREATERTHANdatatype : returnType\n               | VAR\n  returnType : INT\n                 | STRING\n                 | BOOL\n                 | DOUBLE\n                 | DYNAMIC\n                 | VOID\n                 | map_identifier\n  empty :map_content : map_pairs\n                  | empty\n  map_pair : map_key COLON map_valuemap_pairs : map_pair\n                | map_pair COMMA map_pairs\n  map_key : value\n  map_value : value\n  ifElseStatement : ifStatement\n                      | ifStatement elifStatement_repeat\n  elifStatement_repeat : elifStatement\n                           | elifStatement elifStatement_repeat\n  ifStatement : IF LPAREN conditions RPAREN LCURLYBRACKET class_content_repeat RCURLYBRACKET\n  elifStatement : ELSE ifStatement\n  elifStatement : ELSE LCURLYBRACKET class_content_repeat RCURLYBRACKET\n  forStatement : FOR LPAREN declarationExpression SEMICOLON condition SEMICOLON expression RPAREN LCURLYBRACKET RCURLYBRACKET\n  taskStatement : IDENTIFIER operatorExpression operatorExpression\n  stack : FINAL IDENTIFIER EQUAL STACK LESSTHAN datatype GREATERTHAN LPAREN opt_value RPAREN SEMICOLON\n  while : WHILE LPAREN conditions RPAREN LCURLYBRACKET class_content_repeat RCURLYBRACKET\n  stack : FINAL IDENTIFIER EQUAL STACK LESSTHAN datatype GREATERTHAN LPAREN RPAREN SEMICOLON\n          | FINAL IDENTIFIER EQUAL STACK DOT OF LPAREN IDENTIFIER RPAREN SEMICOLON\n  inferedReturnFunction : IDENTIFIER LPAREN  function_arguments_repeat RPAREN LCURLYBRACKET RETURN expression SEMICOLON RCURLYBRACKET\n  value : INTEGER\n              | FLOAT\n              | STR\n              | BOOLEAN\n              | IDENTIFIER\n  opt_value : value\n                | empty\n  deniable_values : IDENTIFIER\n                      | BOOLEAN\n  negation_values : deniable_values\n                     | EXMARK deniable_values\n  condition_values : negation_values\n                      | INTEGER\n                      | FLOAT\n                      | STR\n  condition_operator : DOUBLEQUAL\n                         | LESSTHAN\n                         | GREATERTHAN\n                         | LESSTHAN EQUAL\n                         | GREATERTHAN EQUAL\n  number : FLOAT\n             | INTEGER\n  condition : IDENTIFIER condition_operator condition_values\n                | EXMARK IDENTIFIER condition_operator condition_values\n                | BOOLEAN condition_operator BOOLEAN\n                | number condition_operator number\n                | STR condition_operator STR\n  conditions : condition\n                 | condition condition_connector conditions\n  condition_connector : AND\n                          | OR\n  function_lambda : datatype IDENTIFIER LPAREN function_arguments_repeat optFunction_argumentsExpression RPAREN EQUAL GREATERTHAN expression SEMICOLON\n   function_argument : datatype IDENTIFIER\n                        | empty\n\n  function_arguments_repeat : function_argument\n                                | function_argument COMMA function_arguments_repeat\n   optFunction_argumentsExpression : LCURLYBRACKET optFunction_arguments RCURLYBRACKET\n                                       | empty\n\n  optFunction_argument : REQUIRED datatype IDENTIFIER\n\n  optFunction_arguments : optFunction_argument\n                            | optFunction_argument COMMA optFunction_arguments\n  expression : operableTypes operatorExpression operableTypes\n                  | value\n                  | operableTypes operatorExpression\n  operableTypes : IDENTIFIER\n                    | number\n\n  operatorExpression : PLUS\n                         | MINUS\n                         | TIMES\n                         | DIVISION\n                         | PLUS PLUS\n  declarationExpression : datatype IDENTIFIER SEMICOLON\n  declarationExpression : datatype IDENTIFIER EQUAL expression SEMICOLON\n  '
    
_lr_action_items = {'FOR':([0,2,3,4,5,6,7,8,9,10,11,15,37,38,41,42,62,63,64,67,89,121,125,127,147,157,163,164,174,177,185,193,194,196,197,198,],[17,17,-11,-2,-3,-4,-5,-6,-7,-8,-9,-34,-12,-10,-35,-36,-37,-39,17,-99,17,-40,-100,17,17,17,17,-13,-44,-38,-47,-79,-41,-45,-46,-43,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,15,37,38,41,42,62,63,64,67,89,121,125,127,147,157,163,164,174,177,185,193,194,196,197,198,],[18,18,-11,-2,-3,-4,-5,-6,-7,-8,-9,-34,-12,-10,-35,-36,-37,-39,18,-99,18,-40,-100,18,18,18,18,-13,-44,-38,-47,-79,-41,-45,-46,-43,]),'FINAL':([0,2,3,4,5,6,7,8,9,10,11,15,37,38,41,42,62,63,64,67,89,121,125,127,147,157,163,164,174,177,185,193,194,196,197,198,],[19,19,-11,-2,-3,-4,-5,-6,-7,-8,-9,-34,-12,-10,-35,-36,-37,-39,19,-99,19,-40,-100,19,19,19,19,-13,-44,-38,-47,-79,-41,-45,-46,-43,]),'IDENTIFIER':([0,2,3,4,5,6,7,8,9,10,11,13,15,16,19,22,24,25,31,32,33,34,35,36,37,38,41,42,46,48,49,50,51,52,53,55,59,61,62,63,64,66,67,69,73,82,85,89,93,96,97,98,99,100,101,102,121,125,127,136,138,139,140,147,149,150,151,156,157,162,163,164,172,174,176,177,179,183,185,193,194,196,197,198,],[14,14,-11,-2,-3,-4,-5,-6,-7,-8,-9,39,-34,44,47,-14,-17,-18,-19,-20,-21,-22,-23,-24,-12,-10,-35,-36,72,81,-94,-95,-96,-97,-15,72,88,-25,-37,-39,14,91,-99,94,103,-98,110,14,72,72,-77,-78,129,-63,-64,-65,-40,-100,14,129,-66,-67,129,14,110,110,91,91,14,-16,14,-13,181,-44,184,-38,91,110,-47,-79,-41,-45,-46,-43,]),'MAP':([0,2,3,4,5,6,7,8,9,10,11,15,37,38,40,41,42,45,54,62,63,64,65,67,87,89,108,121,125,127,144,147,155,157,163,164,174,177,185,193,194,196,197,198,],[22,22,-11,-2,-3,-4,-5,-6,-7,-8,-9,-34,-12,-10,22,-35,-36,22,22,-37,-39,22,22,-99,22,22,22,-40,-100,22,22,22,22,22,22,-13,-44,-38,-47,-79,-41,-45,-46,-43,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,15,37,38,41,42,43,62,63,64,67,89,121,125,127,147,157,163,164,174,177,185,193,194,196,197,198,],[23,23,-11,-2,-3,-4,-5,-6,-7,-8,-9,-34,-12,-10,-35,-36,23,-37,-39,23,-99,23,-40,-100,23,23,23,23,-13,-44,-38,-47,-79,-41,-45,-46,-43,]),'VAR':([0,2,3,4,5,6,7,8,9,10,11,15,37,38,40,41,42,45,54,62,63,64,65,67,87,89,108,121,125,127,144,147,155,157,163,164,174,177,185,193,194,196,197,198,],[25,25,-11,-2,-3,-4,-5,-6,-7,-8,-9,-34,-12,-10,25,-35,-36,25,25,-37,-39,25,25,-99,25,25,25,-40,-100,25,25,25,25,25,25,-13,-44,-38,-47,-79,-41,-45,-46,-43,]),'INTEGER':([0,2,3,4,5,6,7,8,9,10,11,15,37,38,41,42,46,48,49,50,51,52,55,62,63,64,66,67,82,85,89,93,96,97,98,99,100,101,102,105,121,125,127,138,139,140,147,149,150,151,156,157,163,164,174,177,179,183,185,193,194,196,197,198,],[27,27,-11,-2,-3,-4,-5,-6,-7,-8,-9,-34,-12,-10,-35,-36,78,78,-94,-95,-96,-97,78,-37,-39,27,27,-99,-98,117,27,78,78,-77,-78,132,-63,-64,-65,78,-40,-100,27,-66,-67,132,27,117,117,27,27,27,27,-13,-44,-38,27,117,-47,-79,-41,-45,-46,-43,]),'FLOAT':([0,2,3,4,5,6,7,8,9,10,11,15,37,38,41,42,46,48,49,50,51,52,55,62,63,64,66,67,82,85,89,93,96,97,98,99,100,101,102,105,121,125,127,138,139,140,147,149,150,151,156,157,163,164,174,177,179,183,185,193,194,196,197,198,],[28,28,-11,-2,-3,-4,-5,-6,-7,-8,-9,-34,-12,-10,-35,-36,77,77,-94,-95,-96,-97,77,-37,-39,28,28,-99,-98,118,28,77,77,-77,-78,133,-63,-64,-65,77,-40,-100,28,-66,-67,133,28,118,118,28,28,28,28,-13,-44,-38,28,118,-47,-79,-41,-45,-46,-43,]),'STR':([0,2,3,4,5,6,7,8,9,10,11,15,37,38,41,42,46,55,62,63,64,66,67,85,89,93,96,97,98,99,100,101,102,106,121,125,127,138,139,140,147,149,150,151,156,157,163,164,174,177,179,183,185,193,194,196,197,198,],[29,29,-11,-2,-3,-4,-5,-6,-7,-8,-9,-34,-12,-10,-35,-36,76,76,-37,-39,29,29,-99,29,29,76,76,-77,-78,134,-63,-64,-65,143,-40,-100,29,-66,-67,134,29,29,29,29,29,29,29,-13,-44,-38,29,29,-47,-79,-41,-45,-46,-43,]),'BOOLEAN':([0,2,3,4,5,6,7,8,9,10,11,15,37,38,41,42,46,55,62,63,64,66,67,85,89,93,96,97,98,99,100,101,102,104,121,125,127,136,138,139,140,147,149,150,151,156,157,163,164,174,177,179,183,185,193,194,196,197,198,],[30,30,-11,-2,-3,-4,-5,-6,-7,-8,-9,-34,-12,-10,-35,-36,74,74,-37,-39,30,30,-99,30,30,74,74,-77,-78,137,-63,-64,-65,141,-40,-100,30,137,-66,-67,137,30,30,30,30,30,30,30,-13,-44,-38,30,30,-47,-79,-41,-45,-46,-43,]),'INT':([0,2,3,4,5,6,7,8,9,10,11,15,37,38,40,41,42,45,54,62,63,64,65,67,87,89,108,121,125,127,144,147,155,157,163,164,174,177,185,193,194,196,197,198,],[31,31,-11,-2,-3,-4,-5,-6,-7,-8,-9,-34,-12,-10,31,-35,-36,31,31,-37,-39,31,31,-99,31,31,31,-40,-100,31,31,31,31,31,31,-13,-44,-38,-47,-79,-41,-45,-46,-43,]),'STRING':([0,2,3,4,5,6,7,8,9,10,11,15,37,38,40,41,42,45,54,62,63,64,65,67,87,89,108,121,125,127,144,147,155,157,163,164,174,177,185,193,194,196,197,198,],[32,32,-11,-2,-3,-4,-5,-6,-7,-8,-9,-34,-12,-10,32,-35,-36,32,32,-37,-39,32,32,-99,32,32,32,-40,-100,32,32,32,32,32,32,-13,-44,-38,-47,-79,-41,-45,-46,-43,]),'BOOL':([0,2,3,4,5,6,7,8,9,10,11,15,37,38,40,41,42,45,54,62,63,64,65,67,87,89,108,121,125,127,144,147,155,157,163,164,174,177,185,193,194,196,197,198,],[33,33,-11,-2,-3,-4,-5,-6,-7,-8,-9,-34,-12,-10,33,-35,-36,33,33,-37,-39,33,33,-99,33,33,33,-40,-100,33,33,33,33,33,33,-13,-44,-38,-47,-79,-41,-45,-46,-43,]),'DOUBLE':([0,2,3,4,5,6,7,8,9,10,11,15,37,38,40,41,42,45,54,62,63,64,65,67,87,89,108,121,125,127,144,147,155,157,163,164,174,177,185,193,194,196,197,198,],[34,34,-11,-2,-3,-4,-5,-6,-7,-8,-9,-34,-12,-10,34,-35,-36,34,34,-37,-39,34,34,-99,34,34,34,-40,-100,34,34,34,34,34,34,-13,-44,-38,-47,-79,-41,-45,-46,-43,]),'DYNAMIC':([0,2,3,4,5,6,7,8,9,10,11,15,37,38,40,41,42,45,54,62,63,64,65,67,87,89,108,121,125,127,144,147,155,157,163,164,174,177,185,193,194,196,197,198,],[35,35,-11,-2,-3,-4,-5,-6,-7,-8,-9,-34,-12,-10,35,-35,-36,35,35,-37,-39,35,35,-99,35,35,35,-40,-100,35,35,35,35,35,35,-13,-44,-38,-47,-79,-41,-45,-46,-43,]),'VOID':([0,2,3,4,5,6,7,8,9,10,11,15,37,38,40,41,42,45,54,62,63,64,65,67,87,89,108,121,125,127,144,147,155,157,163,164,174,177,185,193,194,196,197,198,],[36,36,-11,-2,-3,-4,-5,-6,-7,-8,-9,-34,-12,-10,36,-35,-36,36,36,-37,-39,36,36,-99,36,36,36,-40,-100,36,36,36,36,36,36,-13,-44,-38,-47,-79,-41,-45,-46,-43,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,15,37,38,41,42,62,63,67,121,125,164,174,177,185,193,194,196,197,198,],[0,-1,-11,-2,-3,-4,-5,-6,-7,-8,-9,-34,-12,-10,-35,-36,-37,-39,-99,-40,-100,-13,-44,-38,-47,-79,-41,-45,-46,-43,]),'RCURLYBRACKET':([3,4,5,6,7,8,9,10,11,15,29,30,37,38,41,42,62,63,67,85,89,110,111,112,113,114,117,118,121,125,153,154,157,163,164,165,166,167,174,177,178,180,181,185,187,193,194,196,197,198,],[-11,-2,-3,-4,-5,-6,-7,-8,-9,-34,-50,-51,-12,-10,-35,-36,-37,-39,-99,-26,121,-52,148,-27,-28,-30,-48,-49,-40,-100,170,-87,174,177,-13,-31,-29,-33,-44,-38,185,-88,-86,-47,194,-79,-41,-45,-46,-43,]),'SEMICOLON':([12,14,21,26,27,28,29,30,44,48,49,50,51,52,67,68,77,78,80,81,82,91,92,94,125,126,129,130,131,132,133,134,135,137,141,142,143,148,158,159,168,186,189,192,195,],[38,-52,-90,-93,-48,-49,-50,-51,67,-91,-94,-95,-96,-97,-99,93,-68,-69,-89,-92,-98,-52,125,67,-100,156,-55,-70,-59,-60,-61,-62,-57,-56,-72,-73,-74,164,-58,-71,178,193,196,197,198,]),'LPAREN':([14,17,18,23,44,161,175,],[40,45,46,55,65,176,183,]),'PLUS':([14,20,26,27,28,49,91,],[-92,49,-93,-69,-68,82,-92,]),'MINUS':([14,20,26,27,28,91,],[-92,50,-93,-69,-68,-92,]),'TIMES':([14,20,26,27,28,91,],[-92,51,-93,-69,-68,-92,]),'DIVISION':([14,20,26,27,28,91,],[-92,52,-93,-69,-68,-92,]),'ELSE':([15,42,63,121,177,],[43,43,-39,-40,-38,]),'RPAREN':([21,26,27,28,29,30,40,48,49,50,51,52,57,58,60,65,70,71,77,78,80,81,82,84,87,88,90,91,110,117,118,120,122,124,128,129,130,131,132,133,134,135,137,141,142,143,158,159,170,173,183,184,188,190,191,],[-90,-93,-48,-49,-50,-51,-26,-91,-94,-95,-96,-97,86,-82,-81,-26,95,-75,-68,-69,-89,-92,-98,109,-26,-80,-26,-52,-52,-48,-49,-83,152,-85,-76,-55,-70,-59,-60,-61,-62,-57,-56,-72,-73,-74,-58,-71,-84,182,189,192,195,-53,-54,]),'COMMA':([22,24,25,29,30,31,32,33,34,35,36,40,53,58,60,61,65,83,87,88,110,114,117,118,154,162,166,167,181,],[-14,-17,-18,-50,-51,-19,-20,-21,-22,-23,-24,-26,-15,87,-81,-25,-26,108,-26,-80,-52,149,-48,-49,171,-16,-29,-33,-86,]),'GREATERTHAN':([22,24,25,31,32,33,34,35,36,53,61,72,74,75,76,77,78,103,146,160,162,169,],[-14,-17,-18,-19,-20,-21,-22,-23,-24,-15,-25,102,102,102,102,-68,-69,102,162,175,-16,179,]),'LESSTHAN':([22,72,74,75,76,77,78,103,107,],[54,101,101,101,101,-68,-69,101,144,]),'COLON':([29,30,110,115,116,117,118,],[-50,-51,-52,150,-32,-48,-49,]),'EQUAL':([39,44,47,94,101,102,152,],[56,66,79,66,138,139,169,]),'LCURLYBRACKET':([43,56,58,60,65,86,87,88,90,95,109,120,182,],[64,85,-82,-81,-26,119,-26,-80,123,127,147,-83,187,]),'EXMARK':([46,55,93,96,97,98,99,100,101,102,138,139,140,],[73,73,73,73,-77,-78,136,-63,-64,-65,-66,-67,136,]),'AND':([71,77,78,129,130,131,132,133,134,135,137,141,142,143,158,159,],[97,-68,-69,-55,-70,-59,-60,-61,-62,-57,-56,-72,-73,-74,-58,-71,]),'OR':([71,77,78,129,130,131,132,133,134,135,137,141,142,143,158,159,],[98,-68,-69,-55,-70,-59,-60,-61,-62,-57,-56,-72,-73,-74,-58,-71,]),'DOUBLEQUAL':([72,74,75,76,77,78,103,],[100,100,100,100,-68,-69,100,]),'STACK':([79,],[107,]),'DOT':([107,],[145,]),'RETURN':([119,],[151,]),'REQUIRED':([123,171,],[155,155,]),'OF':([145,],[161,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'class':([0,],[1,]),'class_content_repeat':([0,64,127,147,],[2,89,157,163,]),'class_content':([0,2,64,89,127,147,157,163,],[3,37,3,37,3,3,37,37,]),'map':([0,2,64,89,127,147,157,163,],[4,4,4,4,4,4,4,4,]),'ifElseStatement':([0,2,64,89,127,147,157,163,],[5,5,5,5,5,5,5,5,]),'function_lambda':([0,2,64,89,127,147,157,163,],[6,6,6,6,6,6,6,6,]),'declarationExpression':([0,2,45,64,89,127,147,157,163,],[7,7,68,7,7,7,7,7,7,]),'forStatement':([0,2,64,89,127,147,157,163,],[8,8,8,8,8,8,8,8,]),'while':([0,2,64,89,127,147,157,163,],[9,9,9,9,9,9,9,9,]),'stack':([0,2,64,89,127,147,157,163,],[10,10,10,10,10,10,10,10,]),'inferedReturnFunction':([0,2,64,89,127,147,157,163,],[11,11,11,11,11,11,11,11,]),'expression':([0,2,64,66,89,127,147,151,156,157,163,179,],[12,12,12,92,12,12,12,168,173,12,12,186,]),'map_identifier':([0,2,40,45,54,64,65,87,89,108,127,144,147,155,157,163,],[13,13,61,61,61,13,61,61,13,61,13,61,13,61,13,13,]),'ifStatement':([0,2,43,64,89,127,147,157,163,],[15,15,63,15,15,15,15,15,15,]),'datatype':([0,2,40,45,54,64,65,87,89,108,127,144,147,155,157,163,],[16,16,59,69,83,16,59,59,16,146,16,160,16,172,16,16,]),'operableTypes':([0,2,48,64,66,89,127,147,151,156,157,163,179,],[20,20,80,20,20,20,20,20,20,20,20,20,20,]),'value':([0,2,64,66,85,89,127,147,149,150,151,156,157,163,179,183,],[21,21,21,21,116,21,21,21,116,167,21,21,21,21,21,190,]),'returnType':([0,2,40,45,54,64,65,87,89,108,127,144,147,155,157,163,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'number':([0,2,46,48,55,64,66,89,93,96,105,127,147,151,156,157,163,179,],[26,26,75,26,75,26,26,26,75,75,142,26,26,26,26,26,26,26,]),'elifStatement_repeat':([15,42,],[41,62,]),'elifStatement':([15,42,],[42,42,]),'operatorExpression':([20,],[48,]),'map_type_specified':([22,],[53,]),'function_arguments_repeat':([40,65,87,],[57,90,120,]),'function_argument':([40,65,87,],[58,58,58,]),'empty':([40,65,85,87,90,183,],[60,60,113,60,124,191,]),'conditions':([46,55,96,],[70,84,128,]),'condition':([46,55,93,96,],[71,71,126,71,]),'condition_connector':([71,],[96,]),'condition_operator':([72,74,75,76,103,],[99,104,105,106,140,]),'map_content':([85,],[111,]),'map_pairs':([85,149,],[112,165,]),'map_pair':([85,149,],[114,114,]),'map_key':([85,149,],[115,115,]),'optFunction_argumentsExpression':([90,],[122,]),'condition_values':([99,140,],[130,159,]),'negation_values':([99,140,],[131,131,]),'deniable_values':([99,136,140,],[135,158,135,]),'optFunction_arguments':([123,171,],[153,180,]),'optFunction_argument':([123,171,],[154,154,]),'map_value':([150,],[166,]),'opt_value':([183,],[188,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> class","S'",1,None,None,None),
  ('class -> class_content_repeat','class',1,'p_class','main.py',155),
  ('class_content -> map','class_content',1,'p_class_content_map','main.py',158),
  ('class_content -> ifElseStatement','class_content',1,'p_class_content_ifElse','main.py',161),
  ('class_content -> function_lambda','class_content',1,'p_class_content_lambdaFunction','main.py',164),
  ('class_content -> declarationExpression','class_content',1,'p_class_content_declarationExpression','main.py',167),
  ('class_content -> forStatement','class_content',1,'p_class_content_for','main.py',170),
  ('class_content -> while','class_content',1,'p_class_content_while','main.py',174),
  ('class_content -> stack','class_content',1,'p_class_content_stack','main.py',178),
  ('class_content -> inferedReturnFunction','class_content',1,'p_class_content_inferedFunction','main.py',182),
  ('class_content -> expression SEMICOLON','class_content',2,'p_class_content_expression','main.py',185),
  ('class_content_repeat -> class_content','class_content_repeat',1,'p_class_content_repeat','main.py',188),
  ('class_content_repeat -> class_content_repeat class_content','class_content_repeat',2,'p_class_content_repeat','main.py',189),
  ('map -> map_identifier IDENTIFIER EQUAL LCURLYBRACKET map_content RCURLYBRACKET SEMICOLON','map',7,'p_map','main.py',192),
  ('map_identifier -> MAP','map_identifier',1,'p_map_identifier','main.py',195),
  ('map_identifier -> MAP map_type_specified','map_identifier',2,'p_map_identifier','main.py',196),
  ('map_type_specified -> LESSTHAN datatype COMMA datatype GREATERTHAN','map_type_specified',5,'p_map_type_specified','main.py',200),
  ('datatype -> returnType','datatype',1,'p_datatype','main.py',203),
  ('datatype -> VAR','datatype',1,'p_datatype','main.py',204),
  ('returnType -> INT','returnType',1,'p_returnType','main.py',207),
  ('returnType -> STRING','returnType',1,'p_returnType','main.py',208),
  ('returnType -> BOOL','returnType',1,'p_returnType','main.py',209),
  ('returnType -> DOUBLE','returnType',1,'p_returnType','main.py',210),
  ('returnType -> DYNAMIC','returnType',1,'p_returnType','main.py',211),
  ('returnType -> VOID','returnType',1,'p_returnType','main.py',212),
  ('returnType -> map_identifier','returnType',1,'p_returnType','main.py',213),
  ('empty -> <empty>','empty',0,'p_empty','main.py',217),
  ('map_content -> map_pairs','map_content',1,'p_map_content','main.py',219),
  ('map_content -> empty','map_content',1,'p_map_content','main.py',220),
  ('map_pair -> map_key COLON map_value','map_pair',3,'p_map_pair','main.py',223),
  ('map_pairs -> map_pair','map_pairs',1,'p_map_pairs','main.py',226),
  ('map_pairs -> map_pair COMMA map_pairs','map_pairs',3,'p_map_pairs','main.py',227),
  ('map_key -> value','map_key',1,'p_map_key','main.py',230),
  ('map_value -> value','map_value',1,'p_map_value','main.py',233),
  ('ifElseStatement -> ifStatement','ifElseStatement',1,'p_ifElseStatement','main.py',237),
  ('ifElseStatement -> ifStatement elifStatement_repeat','ifElseStatement',2,'p_ifElseStatement','main.py',238),
  ('elifStatement_repeat -> elifStatement','elifStatement_repeat',1,'p_elifStatement_repeat','main.py',242),
  ('elifStatement_repeat -> elifStatement elifStatement_repeat','elifStatement_repeat',2,'p_elifStatement_repeat','main.py',243),
  ('ifStatement -> IF LPAREN conditions RPAREN LCURLYBRACKET class_content_repeat RCURLYBRACKET','ifStatement',7,'p_ifStatement','main.py',246),
  ('elifStatement -> ELSE ifStatement','elifStatement',2,'p_elifStatement','main.py',250),
  ('elifStatement -> ELSE LCURLYBRACKET class_content_repeat RCURLYBRACKET','elifStatement',4,'p_elseStatement','main.py',253),
  ('forStatement -> FOR LPAREN declarationExpression SEMICOLON condition SEMICOLON expression RPAREN LCURLYBRACKET RCURLYBRACKET','forStatement',10,'p_forStatement','main.py',257),
  ('taskStatement -> IDENTIFIER operatorExpression operatorExpression','taskStatement',3,'p_taskStatement','main.py',261),
  ('stack -> FINAL IDENTIFIER EQUAL STACK LESSTHAN datatype GREATERTHAN LPAREN opt_value RPAREN SEMICOLON','stack',11,'p_stack','main.py',265),
  ('while -> WHILE LPAREN conditions RPAREN LCURLYBRACKET class_content_repeat RCURLYBRACKET','while',7,'p_whileStatement','main.py',269),
  ('stack -> FINAL IDENTIFIER EQUAL STACK LESSTHAN datatype GREATERTHAN LPAREN RPAREN SEMICOLON','stack',10,'p_stackStatement','main.py',272),
  ('stack -> FINAL IDENTIFIER EQUAL STACK DOT OF LPAREN IDENTIFIER RPAREN SEMICOLON','stack',10,'p_stackStatement','main.py',273),
  ('inferedReturnFunction -> IDENTIFIER LPAREN function_arguments_repeat RPAREN LCURLYBRACKET RETURN expression SEMICOLON RCURLYBRACKET','inferedReturnFunction',9,'p_inferedReturnFunction','main.py',277),
  ('value -> INTEGER','value',1,'p_value','main.py',281),
  ('value -> FLOAT','value',1,'p_value','main.py',282),
  ('value -> STR','value',1,'p_value','main.py',283),
  ('value -> BOOLEAN','value',1,'p_value','main.py',284),
  ('value -> IDENTIFIER','value',1,'p_value','main.py',285),
  ('opt_value -> value','opt_value',1,'p_opt_value','main.py',288),
  ('opt_value -> empty','opt_value',1,'p_opt_value','main.py',289),
  ('deniable_values -> IDENTIFIER','deniable_values',1,'p_deniable_values','main.py',292),
  ('deniable_values -> BOOLEAN','deniable_values',1,'p_deniable_values','main.py',293),
  ('negation_values -> deniable_values','negation_values',1,'p_negation_values','main.py',296),
  ('negation_values -> EXMARK deniable_values','negation_values',2,'p_negation_values','main.py',297),
  ('condition_values -> negation_values','condition_values',1,'p_condition_values','main.py',301),
  ('condition_values -> INTEGER','condition_values',1,'p_condition_values','main.py',302),
  ('condition_values -> FLOAT','condition_values',1,'p_condition_values','main.py',303),
  ('condition_values -> STR','condition_values',1,'p_condition_values','main.py',304),
  ('condition_operator -> DOUBLEQUAL','condition_operator',1,'p_condition_operator','main.py',307),
  ('condition_operator -> LESSTHAN','condition_operator',1,'p_condition_operator','main.py',308),
  ('condition_operator -> GREATERTHAN','condition_operator',1,'p_condition_operator','main.py',309),
  ('condition_operator -> LESSTHAN EQUAL','condition_operator',2,'p_condition_operator','main.py',310),
  ('condition_operator -> GREATERTHAN EQUAL','condition_operator',2,'p_condition_operator','main.py',311),
  ('number -> FLOAT','number',1,'p_number','main.py',314),
  ('number -> INTEGER','number',1,'p_number','main.py',315),
  ('condition -> IDENTIFIER condition_operator condition_values','condition',3,'p_condition','main.py',318),
  ('condition -> EXMARK IDENTIFIER condition_operator condition_values','condition',4,'p_condition','main.py',319),
  ('condition -> BOOLEAN condition_operator BOOLEAN','condition',3,'p_condition','main.py',320),
  ('condition -> number condition_operator number','condition',3,'p_condition','main.py',321),
  ('condition -> STR condition_operator STR','condition',3,'p_condition','main.py',322),
  ('conditions -> condition','conditions',1,'p_conditions','main.py',326),
  ('conditions -> condition condition_connector conditions','conditions',3,'p_conditions','main.py',327),
  ('condition_connector -> AND','condition_connector',1,'p_condition_connector','main.py',331),
  ('condition_connector -> OR','condition_connector',1,'p_condition_connector','main.py',332),
  ('function_lambda -> datatype IDENTIFIER LPAREN function_arguments_repeat optFunction_argumentsExpression RPAREN EQUAL GREATERTHAN expression SEMICOLON','function_lambda',10,'p_function_lambda','main.py',336),
  ('function_argument -> datatype IDENTIFIER','function_argument',2,'p_function_argument','main.py',340),
  ('function_argument -> empty','function_argument',1,'p_function_argument','main.py',341),
  ('function_arguments_repeat -> function_argument','function_arguments_repeat',1,'p_function_arguments_repeat','main.py',346),
  ('function_arguments_repeat -> function_argument COMMA function_arguments_repeat','function_arguments_repeat',3,'p_function_arguments_repeat','main.py',347),
  ('optFunction_argumentsExpression -> LCURLYBRACKET optFunction_arguments RCURLYBRACKET','optFunction_argumentsExpression',3,'p_optFunction_argumentsExpression','main.py',351),
  ('optFunction_argumentsExpression -> empty','optFunction_argumentsExpression',1,'p_optFunction_argumentsExpression','main.py',352),
  ('optFunction_argument -> REQUIRED datatype IDENTIFIER','optFunction_argument',3,'p_optFunction_argument','main.py',356),
  ('optFunction_arguments -> optFunction_argument','optFunction_arguments',1,'p_optFunction_arguments','main.py',361),
  ('optFunction_arguments -> optFunction_argument COMMA optFunction_arguments','optFunction_arguments',3,'p_optFunction_arguments','main.py',362),
  ('expression -> operableTypes operatorExpression operableTypes','expression',3,'p_expression','main.py',366),
  ('expression -> value','expression',1,'p_expression','main.py',367),
  ('expression -> operableTypes operatorExpression','expression',2,'p_expression','main.py',368),
  ('operableTypes -> IDENTIFIER','operableTypes',1,'p_operablTypes','main.py',372),
  ('operableTypes -> number','operableTypes',1,'p_operablTypes','main.py',373),
  ('operatorExpression -> PLUS','operatorExpression',1,'p_operatorExpression','main.py',377),
  ('operatorExpression -> MINUS','operatorExpression',1,'p_operatorExpression','main.py',378),
  ('operatorExpression -> TIMES','operatorExpression',1,'p_operatorExpression','main.py',379),
  ('operatorExpression -> DIVISION','operatorExpression',1,'p_operatorExpression','main.py',380),
  ('operatorExpression -> PLUS PLUS','operatorExpression',2,'p_operatorExpression','main.py',381),
  ('declarationExpression -> datatype IDENTIFIER SEMICOLON','declarationExpression',3,'p_declarationExpression','main.py',385),
  ('declarationExpression -> datatype IDENTIFIER EQUAL expression SEMICOLON','declarationExpression',5,'p_declarationExpression_asign','main.py',389),
]
