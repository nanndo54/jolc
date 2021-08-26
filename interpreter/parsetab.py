
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftop_rangoleftorleftandleftigualaciondiferenciacionleftmenormenor_igualmayormayor_igualleftmasmenosleftasteriscobarramodulorightcaretrightop_negacionnotleftop_llamadaleftop_acceso_arreglononassocop_agrupacionBool Char Float64 Int64 Nothing String and asterisco barra bool break caret char coma continue corchete_A corchete_B diferenciacion dospuntos else elseif end float64 for function global id if igual igualacion in int64 local mas mayor mayor_igual menor menor_igual menos modulo mutable not or parentesis_A parentesis_B punto puntoycoma return string struct tipo while\n  INS : INS I puntoycoma\n      | INS error puntoycoma\n      | I puntoycoma\n      | error puntoycoma\n  \n  I : ASIGNACION\n    | ASIGNACION_STRUCT\n    | ASIGNACION_ARRAY\n    | FUNCION\n    | STRUCT\n    | LLAMADA\n    | IF\n    | WHILE\n    | FOR\n    | BREAK\n    | CONTINUE\n    | RETURN\n  \n  BLOQUE  : INS end\n  \n  BLOQUE_ABIERTO  : INS\n  \n  TIPO  : Int64\n        | Float64\n        | Bool\n        | Char\n        | String\n  \n  SCOPE  : local\n        | global\n  \n  ASIGNACION  : id igual ASIGNACION_VALOR\n              | SCOPE id igual ASIGNACION_VALOR\n              | SCOPE id\n  \n  ASIGNACION_VALOR  : E\n                    | E tipo TIPO\n  \n  ASIGNACION_STRUCT : ID igual E\n  \n  ASIGNACION_ARRAY : id IND igual E\n  \n  IND : IND corchete_A E corchete_B\n      | corchete_A E corchete_B\n  \n  FUNCION : function id parentesis_A PAR parentesis_B BLOQUE\n          | function id parentesis_A parentesis_B BLOQUE\n  \n  PAR : PAR coma P\n      | P\n  \n  P : id\n  \n  STRUCT  : struct id ATR end\n          | mutable struct id ATR end\n  \n  ATR : ATR A\n      | A\n  \n  A : id tipo TIPO puntoycoma\n    | id puntoycoma\n  \n  EXP : EXP coma E\n      | E\n  \n  E : E mas E\n    | E menos E\n    | E asterisco E\n    | E barra E\n    | E caret E\n    | E modulo E\n    | menos E                     %prec op_negacion\n    | E mayor E\n    | E menor E\n    | E mayor_igual E\n    | E menor_igual E\n    | E igualacion E\n    | E diferenciacion E\n    | E or E\n    | E and E\n    | not E\n    | parentesis_A E parentesis_B %prec op_agrupacion\n    | LLAMADA                     %prec op_llamada\n    | ACCESO_ARREGLO              %prec op_acceso_arreglo\n    | RANGO                       %prec op_rango\n    | ARREGLO\n    | ID\n    | int64\n    | float64\n    | bool\n    | char\n    | string\n    | Nothing\n  \n  ARREGLO : corchete_A EXP corchete_B\n          | corchete_A corchete_B\n  \n  LLAMADA : id parentesis_A EXP parentesis_B\n          | id parentesis_A parentesis_B\n  \n  ACCESO_ARREGLO : id corchete_A E corchete_B\n  \n  ID  : ID punto id\n      | id\n  \n  IF  : if E BLOQUE\n      | if E BLOQUE_ABIERTO ELSE\n      | if E BLOQUE_ABIERTO ELSEIF\n  \n  ELSEIF  : elseif E BLOQUE\n          | elseif E BLOQUE_ABIERTO ELSEIF\n          | elseif E BLOQUE_ABIERTO ELSE\n  \n  ELSE : else BLOQUE\n  \n  WHILE : while E BLOQUE\n  \n  FOR : for id in E BLOQUE\n  \n  RANGO : E dospuntos E\n  \n  BREAK : break\n  \n  CONTINUE : continue\n  \n  RETURN  : return E\n          | return\n  '
    
_lr_action_items = {'error':([0,1,32,33,44,48,49,50,51,52,53,54,55,56,57,58,59,61,64,65,71,76,99,100,101,105,107,112,118,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,147,148,157,163,164,],[3,31,-3,-4,3,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,3,-1,-2,-79,-81,31,-54,-63,-77,31,-78,3,3,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,-92,-64,-76,3,3,3,-80,]),'id':([0,1,17,19,20,22,23,24,27,28,29,32,33,34,36,37,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,68,69,71,74,76,77,79,80,81,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,105,107,108,112,113,118,121,123,124,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,147,148,157,158,163,164,168,],[16,16,38,41,42,59,59,62,59,-24,-25,-3,-4,59,59,59,59,76,78,81,16,59,59,59,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,59,16,-1,-2,59,59,-79,59,-81,116,78,-43,78,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,16,-54,-63,59,-77,16,59,-78,59,16,-45,-42,78,16,59,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,-92,-64,-76,16,16,116,16,-80,-44,]),'function':([0,1,32,33,44,48,49,50,51,52,53,54,55,56,57,58,59,61,64,65,71,76,99,100,101,105,107,112,118,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,147,148,157,163,164,],[19,19,-3,-4,19,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,19,-1,-2,-79,-81,19,-54,-63,-77,19,-78,19,19,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,-92,-64,-76,19,19,19,-80,]),'struct':([0,1,21,32,33,44,48,49,50,51,52,53,54,55,56,57,58,59,61,64,65,71,76,99,100,101,105,107,112,118,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,147,148,157,163,164,],[20,20,43,-3,-4,20,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,20,-1,-2,-79,-81,20,-54,-63,-77,20,-78,20,20,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,-92,-64,-76,20,20,20,-80,]),'mutable':([0,1,32,33,44,48,49,50,51,52,53,54,55,56,57,58,59,61,64,65,71,76,99,100,101,105,107,112,118,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,147,148,157,163,164,],[21,21,-3,-4,21,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,21,-1,-2,-79,-81,21,-54,-63,-77,21,-78,21,21,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,-92,-64,-76,21,21,21,-80,]),'if':([0,1,32,33,44,48,49,50,51,52,53,54,55,56,57,58,59,61,64,65,71,76,99,100,101,105,107,112,118,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,147,148,157,163,164,],[22,22,-3,-4,22,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,22,-1,-2,-79,-81,22,-54,-63,-77,22,-78,22,22,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,-92,-64,-76,22,22,22,-80,]),'while':([0,1,32,33,44,48,49,50,51,52,53,54,55,56,57,58,59,61,64,65,71,76,99,100,101,105,107,112,118,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,147,148,157,163,164,],[23,23,-3,-4,23,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,23,-1,-2,-79,-81,23,-54,-63,-77,23,-78,23,23,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,-92,-64,-76,23,23,23,-80,]),'for':([0,1,32,33,44,48,49,50,51,52,53,54,55,56,57,58,59,61,64,65,71,76,99,100,101,105,107,112,118,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,147,148,157,163,164,],[24,24,-3,-4,24,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,24,-1,-2,-79,-81,24,-54,-63,-77,24,-78,24,24,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,-92,-64,-76,24,24,24,-80,]),'break':([0,1,32,33,44,48,49,50,51,52,53,54,55,56,57,58,59,61,64,65,71,76,99,100,101,105,107,112,118,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,147,148,157,163,164,],[25,25,-3,-4,25,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,25,-1,-2,-79,-81,25,-54,-63,-77,25,-78,25,25,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,-92,-64,-76,25,25,25,-80,]),'continue':([0,1,32,33,44,48,49,50,51,52,53,54,55,56,57,58,59,61,64,65,71,76,99,100,101,105,107,112,118,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,147,148,157,163,164,],[26,26,-3,-4,26,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,26,-1,-2,-79,-81,26,-54,-63,-77,26,-78,26,26,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,-92,-64,-76,26,26,26,-80,]),'return':([0,1,32,33,44,48,49,50,51,52,53,54,55,56,57,58,59,61,64,65,71,76,99,100,101,105,107,112,118,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,147,148,157,163,164,],[27,27,-3,-4,27,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,27,-1,-2,-79,-81,27,-54,-63,-77,27,-78,27,27,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,-92,-64,-76,27,27,27,-80,]),'local':([0,1,32,33,44,48,49,50,51,52,53,54,55,56,57,58,59,61,64,65,71,76,99,100,101,105,107,112,118,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,147,148,157,163,164,],[28,28,-3,-4,28,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,28,-1,-2,-79,-81,28,-54,-63,-77,28,-78,28,28,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,-92,-64,-76,28,28,28,-80,]),'global':([0,1,32,33,44,48,49,50,51,52,53,54,55,56,57,58,59,61,64,65,71,76,99,100,101,105,107,112,118,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,147,148,157,163,164,],[29,29,-3,-4,29,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,29,-1,-2,-79,-81,29,-54,-63,-77,29,-78,29,29,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,-92,-64,-76,29,29,29,-80,]),'$end':([1,32,33,64,65,],[0,-3,-4,-1,-2,]),'puntoycoma':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,25,26,27,30,31,38,48,49,50,51,52,53,54,55,56,57,58,59,63,66,67,71,75,76,78,82,100,101,105,106,110,112,115,122,125,126,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,147,149,150,151,152,153,154,159,160,161,162,164,165,166,169,171,172,],[32,33,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-93,-94,-96,64,65,-28,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,-95,-26,-29,-79,-31,-81,121,-83,-54,-63,-77,-90,-32,-78,-27,-40,-84,-85,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,-92,-17,-64,-76,-30,-19,-20,-21,-22,-23,-36,168,-41,-89,-80,-91,-35,-86,-87,-88,]),'igual':([16,18,35,38,76,114,155,],[34,39,68,74,-81,-34,-33,]),'parentesis_A':([16,22,23,27,34,36,37,39,41,45,46,47,59,60,68,69,74,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,103,108,113,128,],[36,47,47,47,47,47,47,47,77,47,47,47,36,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'punto':([16,18,52,59,76,],[-82,40,40,-82,-81,]),'corchete_A':([16,22,23,27,34,35,36,37,39,45,46,47,59,60,68,69,74,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,103,108,113,114,128,155,],[37,60,60,60,60,69,60,60,60,60,60,60,103,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,-34,60,-33,]),'menos':([22,23,27,34,36,37,39,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,67,68,69,71,72,73,74,75,76,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,101,102,103,105,108,110,111,112,113,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,147,148,156,163,164,],[45,45,45,45,45,45,45,85,45,45,45,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,45,85,85,85,45,45,-79,85,85,45,85,-81,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-54,-63,85,45,-77,45,85,85,-78,45,45,-48,-49,-50,-51,-52,-53,85,85,85,85,85,85,85,85,85,-64,85,-76,85,85,85,-80,]),'not':([22,23,27,34,36,37,39,45,46,47,60,68,69,74,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,103,108,113,128,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'int64':([22,23,27,34,36,37,39,45,46,47,60,68,69,74,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,103,108,113,128,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'float64':([22,23,27,34,36,37,39,45,46,47,60,68,69,74,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,103,108,113,128,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'bool':([22,23,27,34,36,37,39,45,46,47,60,68,69,74,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,103,108,113,128,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'char':([22,23,27,34,36,37,39,45,46,47,60,68,69,74,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,103,108,113,128,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'string':([22,23,27,34,36,37,39,45,46,47,60,68,69,74,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,103,108,113,128,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'Nothing':([22,23,27,34,36,37,39,45,46,47,60,68,69,74,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,103,108,113,128,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'end':([32,33,64,65,79,80,99,107,121,123,124,168,],[-3,-4,-1,-2,122,-43,144,144,-45,-42,161,-44,]),'else':([32,33,64,65,83,99,170,],[-3,-4,-1,-2,127,-18,127,]),'elseif':([32,33,64,65,83,99,170,],[-3,-4,-1,-2,128,-18,128,]),'parentesis_B':([36,48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,76,77,100,101,102,105,112,116,117,119,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,147,156,164,167,],[71,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,112,-79,-47,-81,118,-54,-63,145,-77,-78,-39,157,-38,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,-92,-64,-76,-46,-80,-37,]),'mas':([44,48,49,50,51,52,53,54,55,56,57,58,59,61,63,67,71,72,73,75,76,100,101,102,105,110,111,112,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,147,148,156,163,164,],[84,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,84,84,84,-79,84,84,84,-81,-54,-63,84,-77,84,84,-78,-48,-49,-50,-51,-52,-53,84,84,84,84,84,84,84,84,84,-64,84,-76,84,84,84,-80,]),'asterisco':([44,48,49,50,51,52,53,54,55,56,57,58,59,61,63,67,71,72,73,75,76,100,101,102,105,110,111,112,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,147,148,156,163,164,],[86,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,86,86,86,-79,86,86,86,-81,-54,-63,86,-77,86,86,-78,86,86,-50,-51,-52,-53,86,86,86,86,86,86,86,86,86,-64,86,-76,86,86,86,-80,]),'barra':([44,48,49,50,51,52,53,54,55,56,57,58,59,61,63,67,71,72,73,75,76,100,101,102,105,110,111,112,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,147,148,156,163,164,],[87,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,87,87,87,-79,87,87,87,-81,-54,-63,87,-77,87,87,-78,87,87,-50,-51,-52,-53,87,87,87,87,87,87,87,87,87,-64,87,-76,87,87,87,-80,]),'caret':([44,48,49,50,51,52,53,54,55,56,57,58,59,61,63,67,71,72,73,75,76,100,101,102,105,110,111,112,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,147,148,156,163,164,],[88,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,88,88,88,-79,88,88,88,-81,-54,-63,88,-77,88,88,-78,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,-64,88,-76,88,88,88,-80,]),'modulo':([44,48,49,50,51,52,53,54,55,56,57,58,59,61,63,67,71,72,73,75,76,100,101,102,105,110,111,112,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,147,148,156,163,164,],[89,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,89,89,89,-79,89,89,89,-81,-54,-63,89,-77,89,89,-78,89,89,-50,-51,-52,-53,89,89,89,89,89,89,89,89,89,-64,89,-76,89,89,89,-80,]),'mayor':([44,48,49,50,51,52,53,54,55,56,57,58,59,61,63,67,71,72,73,75,76,100,101,102,105,110,111,112,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,147,148,156,163,164,],[90,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,90,90,90,-79,90,90,90,-81,-54,-63,90,-77,90,90,-78,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,90,90,90,90,90,-64,90,-76,90,90,90,-80,]),'menor':([44,48,49,50,51,52,53,54,55,56,57,58,59,61,63,67,71,72,73,75,76,100,101,102,105,110,111,112,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,147,148,156,163,164,],[91,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,91,91,91,-79,91,91,91,-81,-54,-63,91,-77,91,91,-78,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,91,91,91,91,91,-64,91,-76,91,91,91,-80,]),'mayor_igual':([44,48,49,50,51,52,53,54,55,56,57,58,59,61,63,67,71,72,73,75,76,100,101,102,105,110,111,112,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,147,148,156,163,164,],[92,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,92,92,92,-79,92,92,92,-81,-54,-63,92,-77,92,92,-78,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,92,92,92,92,92,-64,92,-76,92,92,92,-80,]),'menor_igual':([44,48,49,50,51,52,53,54,55,56,57,58,59,61,63,67,71,72,73,75,76,100,101,102,105,110,111,112,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,147,148,156,163,164,],[93,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,93,93,93,-79,93,93,93,-81,-54,-63,93,-77,93,93,-78,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,93,93,93,93,93,-64,93,-76,93,93,93,-80,]),'igualacion':([44,48,49,50,51,52,53,54,55,56,57,58,59,61,63,67,71,72,73,75,76,100,101,102,105,110,111,112,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,147,148,156,163,164,],[94,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,94,94,94,-79,94,94,94,-81,-54,-63,94,-77,94,94,-78,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,94,94,94,-64,94,-76,94,94,94,-80,]),'diferenciacion':([44,48,49,50,51,52,53,54,55,56,57,58,59,61,63,67,71,72,73,75,76,100,101,102,105,110,111,112,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,147,148,156,163,164,],[95,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,95,95,95,-79,95,95,95,-81,-54,-63,95,-77,95,95,-78,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,95,95,95,-64,95,-76,95,95,95,-80,]),'or':([44,48,49,50,51,52,53,54,55,56,57,58,59,61,63,67,71,72,73,75,76,100,101,102,105,110,111,112,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,147,148,156,163,164,],[96,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,96,96,96,-79,96,96,96,-81,-54,-63,96,-77,96,96,-78,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,96,-64,96,-76,96,96,96,-80,]),'and':([44,48,49,50,51,52,53,54,55,56,57,58,59,61,63,67,71,72,73,75,76,100,101,102,105,110,111,112,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,147,148,156,163,164,],[97,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,97,97,97,-79,97,97,97,-81,-54,-63,97,-77,97,97,-78,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,97,-62,97,-64,97,-76,97,97,97,-80,]),'dospuntos':([44,48,49,50,51,52,53,54,55,56,57,58,59,61,63,67,71,72,73,75,76,100,101,102,105,110,111,112,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,147,148,156,163,164,],[98,-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,98,98,98,-79,98,98,98,-81,-54,-63,98,-77,98,98,-78,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,98,-64,98,-76,98,98,98,-80,]),'tipo':([48,49,50,51,52,53,54,55,56,57,58,59,67,71,76,78,100,101,105,112,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,147,164,],[-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,109,-79,-81,120,-54,-63,-77,-78,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,-92,-64,-76,-80,]),'coma':([48,49,50,51,52,53,54,55,56,57,58,59,70,71,72,76,100,101,104,105,112,116,117,119,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,147,156,164,167,],[-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,113,-79,-47,-81,-54,-63,113,-77,-78,-39,158,-38,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,-92,-64,-76,-46,-80,-37,]),'corchete_B':([48,49,50,51,52,53,54,55,56,57,58,59,60,71,72,73,76,100,101,104,105,111,112,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,145,146,147,156,164,],[-65,-66,-67,-68,-69,-70,-71,-72,-73,-74,-75,-82,105,-79,-47,114,-81,-54,-63,147,-77,155,-78,-48,-49,-50,-51,-52,-53,-55,-56,-57,-58,-59,-60,-61,-62,-92,-64,164,-76,-46,-80,]),'in':([62,],[108,]),'Int64':([109,120,],[150,150,]),'Float64':([109,120,],[151,151,]),'Bool':([109,120,],[152,152,]),'Char':([109,120,],[153,153,]),'String':([109,120,],[154,154,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'INS':([0,44,61,118,127,148,157,163,],[1,99,107,107,107,107,107,99,]),'I':([0,1,44,61,99,107,118,127,148,157,163,],[2,30,2,2,30,30,2,2,2,2,2,]),'ASIGNACION':([0,1,44,61,99,107,118,127,148,157,163,],[4,4,4,4,4,4,4,4,4,4,4,]),'ASIGNACION_STRUCT':([0,1,44,61,99,107,118,127,148,157,163,],[5,5,5,5,5,5,5,5,5,5,5,]),'ASIGNACION_ARRAY':([0,1,44,61,99,107,118,127,148,157,163,],[6,6,6,6,6,6,6,6,6,6,6,]),'FUNCION':([0,1,44,61,99,107,118,127,148,157,163,],[7,7,7,7,7,7,7,7,7,7,7,]),'STRUCT':([0,1,44,61,99,107,118,127,148,157,163,],[8,8,8,8,8,8,8,8,8,8,8,]),'LLAMADA':([0,1,22,23,27,34,36,37,39,44,45,46,47,60,61,68,69,74,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,103,107,108,113,118,127,128,148,157,163,],[9,9,48,48,48,48,48,48,48,9,48,48,48,48,9,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,9,48,9,48,48,9,9,48,9,9,9,]),'IF':([0,1,44,61,99,107,118,127,148,157,163,],[10,10,10,10,10,10,10,10,10,10,10,]),'WHILE':([0,1,44,61,99,107,118,127,148,157,163,],[11,11,11,11,11,11,11,11,11,11,11,]),'FOR':([0,1,44,61,99,107,118,127,148,157,163,],[12,12,12,12,12,12,12,12,12,12,12,]),'BREAK':([0,1,44,61,99,107,118,127,148,157,163,],[13,13,13,13,13,13,13,13,13,13,13,]),'CONTINUE':([0,1,44,61,99,107,118,127,148,157,163,],[14,14,14,14,14,14,14,14,14,14,14,]),'RETURN':([0,1,44,61,99,107,118,127,148,157,163,],[15,15,15,15,15,15,15,15,15,15,15,]),'SCOPE':([0,1,44,61,99,107,118,127,148,157,163,],[17,17,17,17,17,17,17,17,17,17,17,]),'ID':([0,1,22,23,27,34,36,37,39,44,45,46,47,60,61,68,69,74,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,103,107,108,113,118,127,128,148,157,163,],[18,18,52,52,52,52,52,52,52,18,52,52,52,52,18,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,18,52,18,52,52,18,18,52,18,18,18,]),'IND':([16,],[35,]),'E':([22,23,27,34,36,37,39,45,46,47,60,68,69,74,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,103,108,113,128,],[44,61,63,67,72,73,75,100,101,102,72,110,111,67,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,146,148,156,163,]),'ACCESO_ARREGLO':([22,23,27,34,36,37,39,45,46,47,60,68,69,74,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,103,108,113,128,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'RANGO':([22,23,27,34,36,37,39,45,46,47,60,68,69,74,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,103,108,113,128,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'ARREGLO':([22,23,27,34,36,37,39,45,46,47,60,68,69,74,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,103,108,113,128,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'ASIGNACION_VALOR':([34,74,],[66,115,]),'EXP':([36,60,],[70,104,]),'ATR':([42,81,],[79,124,]),'A':([42,79,81,124,],[80,123,80,123,]),'BLOQUE':([44,61,118,127,148,157,163,],[82,106,159,162,165,166,169,]),'BLOQUE_ABIERTO':([44,163,],[83,170,]),'PAR':([77,],[117,]),'P':([77,158,],[119,167,]),'ELSE':([83,170,],[125,172,]),'ELSEIF':([83,170,],[126,171,]),'TIPO':([109,120,],[149,160,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> INS","S'",1,None,None,None),
  ('INS -> INS I puntoycoma','INS',3,'p_INS','analyzer.py',197),
  ('INS -> INS error puntoycoma','INS',3,'p_INS','analyzer.py',198),
  ('INS -> I puntoycoma','INS',2,'p_INS','analyzer.py',199),
  ('INS -> error puntoycoma','INS',2,'p_INS','analyzer.py',200),
  ('I -> ASIGNACION','I',1,'p_I','analyzer.py',215),
  ('I -> ASIGNACION_STRUCT','I',1,'p_I','analyzer.py',216),
  ('I -> ASIGNACION_ARRAY','I',1,'p_I','analyzer.py',217),
  ('I -> FUNCION','I',1,'p_I','analyzer.py',218),
  ('I -> STRUCT','I',1,'p_I','analyzer.py',219),
  ('I -> LLAMADA','I',1,'p_I','analyzer.py',220),
  ('I -> IF','I',1,'p_I','analyzer.py',221),
  ('I -> WHILE','I',1,'p_I','analyzer.py',222),
  ('I -> FOR','I',1,'p_I','analyzer.py',223),
  ('I -> BREAK','I',1,'p_I','analyzer.py',224),
  ('I -> CONTINUE','I',1,'p_I','analyzer.py',225),
  ('I -> RETURN','I',1,'p_I','analyzer.py',226),
  ('BLOQUE -> INS end','BLOQUE',2,'p_BLOQUE','analyzer.py',232),
  ('BLOQUE_ABIERTO -> INS','BLOQUE_ABIERTO',1,'p_BLOQUE_ABIERTO','analyzer.py',239),
  ('TIPO -> Int64','TIPO',1,'p_TIPO','analyzer.py',245),
  ('TIPO -> Float64','TIPO',1,'p_TIPO','analyzer.py',246),
  ('TIPO -> Bool','TIPO',1,'p_TIPO','analyzer.py',247),
  ('TIPO -> Char','TIPO',1,'p_TIPO','analyzer.py',248),
  ('TIPO -> String','TIPO',1,'p_TIPO','analyzer.py',249),
  ('SCOPE -> local','SCOPE',1,'p_SCOPE','analyzer.py',255),
  ('SCOPE -> global','SCOPE',1,'p_SCOPE','analyzer.py',256),
  ('ASIGNACION -> id igual ASIGNACION_VALOR','ASIGNACION',3,'p_ASIGNACION','analyzer.py',262),
  ('ASIGNACION -> SCOPE id igual ASIGNACION_VALOR','ASIGNACION',4,'p_ASIGNACION','analyzer.py',263),
  ('ASIGNACION -> SCOPE id','ASIGNACION',2,'p_ASIGNACION','analyzer.py',264),
  ('ASIGNACION_VALOR -> E','ASIGNACION_VALOR',1,'p_ASIGNACION_VALOR','analyzer.py',283),
  ('ASIGNACION_VALOR -> E tipo TIPO','ASIGNACION_VALOR',3,'p_ASIGNACION_VALOR','analyzer.py',284),
  ('ASIGNACION_STRUCT -> ID igual E','ASIGNACION_STRUCT',3,'p_ASIGNACION_STRUCT','analyzer.py',295),
  ('ASIGNACION_ARRAY -> id IND igual E','ASIGNACION_ARRAY',4,'p_ASIGNACION_ARRAY','analyzer.py',302),
  ('IND -> IND corchete_A E corchete_B','IND',4,'p_IND','analyzer.py',309),
  ('IND -> corchete_A E corchete_B','IND',3,'p_IND','analyzer.py',310),
  ('FUNCION -> function id parentesis_A PAR parentesis_B BLOQUE','FUNCION',6,'p_FUNCION','analyzer.py',319),
  ('FUNCION -> function id parentesis_A parentesis_B BLOQUE','FUNCION',5,'p_FUNCION','analyzer.py',320),
  ('PAR -> PAR coma P','PAR',3,'p_PAR','analyzer.py',332),
  ('PAR -> P','PAR',1,'p_PAR','analyzer.py',333),
  ('P -> id','P',1,'p_P','analyzer.py',342),
  ('STRUCT -> struct id ATR end','STRUCT',4,'p_STRUCT','analyzer.py',348),
  ('STRUCT -> mutable struct id ATR end','STRUCT',5,'p_STRUCT','analyzer.py',349),
  ('ATR -> ATR A','ATR',2,'p_ATR','analyzer.py',362),
  ('ATR -> A','ATR',1,'p_ATR','analyzer.py',363),
  ('A -> id tipo TIPO puntoycoma','A',4,'p_A','analyzer.py',372),
  ('A -> id puntoycoma','A',2,'p_A','analyzer.py',373),
  ('EXP -> EXP coma E','EXP',3,'p_EXP','analyzer.py',384),
  ('EXP -> E','EXP',1,'p_EXP','analyzer.py',385),
  ('E -> E mas E','E',3,'p_E','analyzer.py',394),
  ('E -> E menos E','E',3,'p_E','analyzer.py',395),
  ('E -> E asterisco E','E',3,'p_E','analyzer.py',396),
  ('E -> E barra E','E',3,'p_E','analyzer.py',397),
  ('E -> E caret E','E',3,'p_E','analyzer.py',398),
  ('E -> E modulo E','E',3,'p_E','analyzer.py',399),
  ('E -> menos E','E',2,'p_E','analyzer.py',400),
  ('E -> E mayor E','E',3,'p_E','analyzer.py',401),
  ('E -> E menor E','E',3,'p_E','analyzer.py',402),
  ('E -> E mayor_igual E','E',3,'p_E','analyzer.py',403),
  ('E -> E menor_igual E','E',3,'p_E','analyzer.py',404),
  ('E -> E igualacion E','E',3,'p_E','analyzer.py',405),
  ('E -> E diferenciacion E','E',3,'p_E','analyzer.py',406),
  ('E -> E or E','E',3,'p_E','analyzer.py',407),
  ('E -> E and E','E',3,'p_E','analyzer.py',408),
  ('E -> not E','E',2,'p_E','analyzer.py',409),
  ('E -> parentesis_A E parentesis_B','E',3,'p_E','analyzer.py',410),
  ('E -> LLAMADA','E',1,'p_E','analyzer.py',411),
  ('E -> ACCESO_ARREGLO','E',1,'p_E','analyzer.py',412),
  ('E -> RANGO','E',1,'p_E','analyzer.py',413),
  ('E -> ARREGLO','E',1,'p_E','analyzer.py',414),
  ('E -> ID','E',1,'p_E','analyzer.py',415),
  ('E -> int64','E',1,'p_E','analyzer.py',416),
  ('E -> float64','E',1,'p_E','analyzer.py',417),
  ('E -> bool','E',1,'p_E','analyzer.py',418),
  ('E -> char','E',1,'p_E','analyzer.py',419),
  ('E -> string','E',1,'p_E','analyzer.py',420),
  ('E -> Nothing','E',1,'p_E','analyzer.py',421),
  ('ARREGLO -> corchete_A EXP corchete_B','ARREGLO',3,'p_ARREGLO','analyzer.py',446),
  ('ARREGLO -> corchete_A corchete_B','ARREGLO',2,'p_ARREGLO','analyzer.py',447),
  ('LLAMADA -> id parentesis_A EXP parentesis_B','LLAMADA',4,'p_LLAMADA','analyzer.py',455),
  ('LLAMADA -> id parentesis_A parentesis_B','LLAMADA',3,'p_LLAMADA','analyzer.py',456),
  ('ACCESO_ARREGLO -> id corchete_A E corchete_B','ACCESO_ARREGLO',4,'p_ACCESO_ARREGLO','analyzer.py',467),
  ('ID -> ID punto id','ID',3,'p_ID','analyzer.py',474),
  ('ID -> id','ID',1,'p_ID','analyzer.py',475),
  ('IF -> if E BLOQUE','IF',3,'p_IF','analyzer.py',484),
  ('IF -> if E BLOQUE_ABIERTO ELSE','IF',4,'p_IF','analyzer.py',485),
  ('IF -> if E BLOQUE_ABIERTO ELSEIF','IF',4,'p_IF','analyzer.py',486),
  ('ELSEIF -> elseif E BLOQUE','ELSEIF',3,'p_ELSEIF','analyzer.py',497),
  ('ELSEIF -> elseif E BLOQUE_ABIERTO ELSEIF','ELSEIF',4,'p_ELSEIF','analyzer.py',498),
  ('ELSEIF -> elseif E BLOQUE_ABIERTO ELSE','ELSEIF',4,'p_ELSEIF','analyzer.py',499),
  ('ELSE -> else BLOQUE','ELSE',2,'p_ELSE','analyzer.py',510),
  ('WHILE -> while E BLOQUE','WHILE',3,'p_WHILE','analyzer.py',517),
  ('FOR -> for id in E BLOQUE','FOR',5,'p_FOR','analyzer.py',524),
  ('RANGO -> E dospuntos E','RANGO',3,'p_RANGO','analyzer.py',531),
  ('BREAK -> break','BREAK',1,'p_BREAK','analyzer.py',538),
  ('CONTINUE -> continue','CONTINUE',1,'p_CONTINUE','analyzer.py',544),
  ('RETURN -> return E','RETURN',2,'p_RETURN','analyzer.py',550),
  ('RETURN -> return','RETURN',1,'p_RETURN','analyzer.py',551),
]
