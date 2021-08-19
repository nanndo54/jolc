
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocop_agrupacionleftop_acceso_arregloleftop_llamadarightop_negacionnotrightcaretleftasteriscobarramoduloleftmasmenosleftmenormenor_igualmayormayor_igualleftigualaciondiferenciacionleftandleftorand asterisco barra bool break caret char coma continue corchete_A corchete_B diferenciacion dospuntos else elseif end float64 for function global id if igual igualacion in int64 local mas mayor mayor_igual menor menor_igual menos modulo mutable not nothing or parentesis_A parentesis_B punto puntoycoma return string struct tipo tipo_bool tipo_char tipo_float64 tipo_int64 tipo_string while\n    INS : INS I puntoycoma\n        | I puntoycoma\n    \n    I   : ASIGNACION\n        | FUNCION\n        | STRUCT\n        | LLAMADA\n        | IF\n        | WHILE\n        | FOR\n        | BREAK\n        | CONTINUE\n        | RETURN\n        | error puntoycoma\n    \n    BLOQUE  : INS end\n            | end\n    \n    TIPO    : tipo_int64\n            | tipo_float64\n            | tipo_bool\n            | tipo_char\n            | tipo_string\n    \n    ASIGNACION  : ID igual ASIGNACION_VALOR\n                | global id igual ASIGNACION_VALOR\n                | global id\n                | local id igual ASIGNACION_VALOR\n                | local id\n    \n    ASIGNACION_VALOR    : E\n                        | E tipo TIPO\n    \n    FUNCION : function id parentesis_A PAR parentesis_B BLOQUE\n            | function id parentesis_A parentesis_B BLOQUE\n    \n    PAR : PAR coma P\n        | P\n    \n    P : id\n    \n    STRUCT  : struct id ATR end\n            | mutable struct id ATR end\n    \n    ATR : ATR A\n        | A\n    \n    A   : id tipo TIPO puntoycoma\n        | id puntoycoma\n    \n    EXP : EXP coma E\n        | E\n    \n    E   : E mas E\n        | E menos E\n        | E asterisco E\n        | E barra E\n        | E caret E\n        | E modulo E\n        | menos E                     %prec op_negacion\n        | E mayor E\n        | E menor E\n        | E mayor_igual E\n        | E menor_igual E\n        | E igualacion E\n        | E diferenciacion E\n        | E or E\n        | E and E\n        | not E\n        | parentesis_A E parentesis_B %prec op_agrupacion\n        | LLAMADA                     %prec op_llamada\n        | ACCESO_ARREGLO              %prec op_acceso_arreglo\n        | ARREGLO\n        | ID\n        | int64\n        | float64\n        | bool\n        | char\n        | string\n        | nothing\n    \n    ARREGLO : corchete_A EXP corchete_B\n            | corchete_A corchete_B\n    \n    LLAMADA : id parentesis_A EXP parentesis_B\n            | id parentesis_A parentesis_B\n    \n    ACCESO_ARREGLO : id corchete_A E corchete_B\n    \n    ID : ID punto id\n        | id\n    \n    IF : if E BLOQUE\n        | if E BLOQUE ELSEIF\n        | if E BLOQUE ELSE\n    \n    ELSEIF  : elseif E BLOQUE\n            | elseif E BLOQUE ELSEIF\n            | elseif E BLOQUE ELSE\n    \n    ELSE : else BLOQUE\n    \n    WHILE : while E BLOQUE\n    \n    FOR : for id in E BLOQUE\n        | for id in RANGO BLOQUE\n    \n    RANGO : E dospuntos E\n    \n    BREAK : break\n    \n    CONTINUE : continue\n    \n    RETURN  : return E\n            | return\n    '
    
_lr_action_items = {'error':([0,1,28,38,42,43,44,45,46,47,48,49,50,51,52,54,57,60,63,86,88,89,93,98,103,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,131,132,133,141,146,148,156,],[13,13,-2,13,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,13,-1,-73,-71,13,-47,-56,-69,-70,13,13,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,-68,13,13,13,13,-72,-85,]),'global':([0,1,28,38,42,43,44,45,46,47,48,49,50,51,52,54,57,60,63,86,88,89,93,98,103,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,131,132,133,141,146,148,156,],[15,15,-2,15,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,15,-1,-73,-71,15,-47,-56,-69,-70,15,15,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,-68,15,15,15,15,-72,-85,]),'local':([0,1,28,38,42,43,44,45,46,47,48,49,50,51,52,54,57,60,63,86,88,89,93,98,103,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,131,132,133,141,146,148,156,],[17,17,-2,17,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,17,-1,-73,-71,17,-47,-56,-69,-70,17,17,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,-68,17,17,17,17,-72,-85,]),'function':([0,1,28,38,42,43,44,45,46,47,48,49,50,51,52,54,57,60,63,86,88,89,93,98,103,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,131,132,133,141,146,148,156,],[18,18,-2,18,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,18,-1,-73,-71,18,-47,-56,-69,-70,18,18,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,-68,18,18,18,18,-72,-85,]),'struct':([0,1,20,28,38,42,43,44,45,46,47,48,49,50,51,52,54,57,60,63,86,88,89,93,98,103,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,131,132,133,141,146,148,156,],[19,19,37,-2,19,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,19,-1,-73,-71,19,-47,-56,-69,-70,19,19,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,-68,19,19,19,19,-72,-85,]),'mutable':([0,1,28,38,42,43,44,45,46,47,48,49,50,51,52,54,57,60,63,86,88,89,93,98,103,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,131,132,133,141,146,148,156,],[20,20,-2,20,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,20,-1,-73,-71,20,-47,-56,-69,-70,20,20,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,-68,20,20,20,20,-72,-85,]),'id':([0,1,15,17,18,19,21,22,23,26,28,30,31,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,57,60,61,63,65,66,68,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,88,89,91,93,95,98,99,103,106,108,109,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,131,132,133,141,142,146,148,150,154,156,],[16,16,32,34,35,36,52,52,55,52,-2,52,60,52,67,70,16,52,52,52,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,52,16,-1,-73,52,-71,52,101,67,-36,67,52,52,52,52,52,52,52,52,52,52,52,52,52,52,16,-47,-56,52,-69,52,-70,52,16,-38,-35,67,52,16,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,-68,16,16,16,101,16,-72,52,-37,-85,]),'if':([0,1,28,38,42,43,44,45,46,47,48,49,50,51,52,54,57,60,63,86,88,89,93,98,103,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,131,132,133,141,146,148,156,],[21,21,-2,21,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,21,-1,-73,-71,21,-47,-56,-69,-70,21,21,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,-68,21,21,21,21,-72,-85,]),'while':([0,1,28,38,42,43,44,45,46,47,48,49,50,51,52,54,57,60,63,86,88,89,93,98,103,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,131,132,133,141,146,148,156,],[22,22,-2,22,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,22,-1,-73,-71,22,-47,-56,-69,-70,22,22,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,-68,22,22,22,22,-72,-85,]),'for':([0,1,28,38,42,43,44,45,46,47,48,49,50,51,52,54,57,60,63,86,88,89,93,98,103,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,131,132,133,141,146,148,156,],[23,23,-2,23,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,23,-1,-73,-71,23,-47,-56,-69,-70,23,23,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,-68,23,23,23,23,-72,-85,]),'break':([0,1,28,38,42,43,44,45,46,47,48,49,50,51,52,54,57,60,63,86,88,89,93,98,103,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,131,132,133,141,146,148,156,],[24,24,-2,24,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,24,-1,-73,-71,24,-47,-56,-69,-70,24,24,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,-68,24,24,24,24,-72,-85,]),'continue':([0,1,28,38,42,43,44,45,46,47,48,49,50,51,52,54,57,60,63,86,88,89,93,98,103,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,131,132,133,141,146,148,156,],[25,25,-2,25,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,25,-1,-73,-71,25,-47,-56,-69,-70,25,25,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,-68,25,25,25,25,-72,-85,]),'return':([0,1,28,38,42,43,44,45,46,47,48,49,50,51,52,54,57,60,63,86,88,89,93,98,103,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,131,132,133,141,146,148,156,],[26,26,-2,26,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,26,-1,-73,-71,26,-47,-56,-69,-70,26,26,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,-68,26,26,26,26,-72,-85,]),'$end':([1,28,57,],[0,-2,-1,]),'puntoycoma':([2,3,4,5,6,7,8,9,10,11,12,13,24,25,26,27,29,32,34,42,43,44,45,46,47,48,49,50,51,52,56,58,59,60,63,67,71,87,88,89,93,94,97,98,100,107,110,111,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,131,134,135,136,137,138,139,143,144,145,147,148,149,151,152,155,157,158,],[28,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,29,-86,-87,-89,57,-13,-23,-25,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,-88,-21,-26,-73,-71,106,-75,-15,-47,-56,-69,-82,-22,-70,-24,-33,-76,-77,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-14,-57,-68,-27,-16,-17,-18,-19,-20,-29,154,-34,-81,-72,-83,-84,-28,-78,-79,-80,]),'igual':([14,16,32,34,60,],[30,-74,61,65,-73,]),'punto':([14,16,45,52,60,],[31,-74,31,-74,-73,]),'parentesis_A':([16,21,22,26,30,33,35,39,40,41,52,53,61,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,91,95,99,112,150,],[33,41,41,41,41,41,66,41,41,41,33,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'menos':([21,22,26,30,33,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,56,59,60,61,63,64,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,89,90,91,93,95,98,99,112,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,140,146,148,150,156,],[39,39,39,39,39,73,39,39,39,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,39,73,73,73,-73,39,-71,73,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,73,73,73,39,-69,39,-70,39,39,-41,-42,73,73,73,73,-48,-49,-50,-51,-52,-53,-54,-55,-57,73,-68,73,73,73,-72,39,73,]),'not':([21,22,26,30,33,39,40,41,53,61,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,91,95,99,112,150,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'int64':([21,22,26,30,33,39,40,41,53,61,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,91,95,99,112,150,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'float64':([21,22,26,30,33,39,40,41,53,61,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,91,95,99,112,150,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'bool':([21,22,26,30,33,39,40,41,53,61,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,91,95,99,112,150,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'char':([21,22,26,30,33,39,40,41,53,61,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,91,95,99,112,150,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'string':([21,22,26,30,33,39,40,41,53,61,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,91,95,99,112,150,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'nothing':([21,22,26,30,33,39,40,41,53,61,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,91,95,99,112,150,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'corchete_A':([21,22,26,30,33,39,40,41,52,53,61,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,91,95,99,112,150,],[53,53,53,53,53,53,53,53,91,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'end':([28,38,42,43,44,45,46,47,48,49,50,51,52,54,57,60,63,68,69,86,88,89,93,98,103,106,108,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,131,132,133,141,146,148,154,156,],[-2,87,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,87,-1,-73,-71,107,-36,128,-47,-56,-69,-70,87,-38,-35,145,87,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,-68,87,87,87,87,-72,-37,-85,]),'parentesis_B':([33,42,43,44,45,46,47,48,49,50,51,52,60,62,63,64,66,88,89,90,93,98,101,102,104,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,131,140,148,153,],[63,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,-73,98,-71,-40,103,-47,-56,129,-69,-70,-32,141,-31,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,-68,-39,-72,-30,]),'mas':([38,42,43,44,45,46,47,48,49,50,51,52,54,56,59,60,63,64,88,89,90,93,98,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,140,146,148,156,],[72,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,72,72,72,-73,-71,72,72,72,72,-69,-70,-41,-42,72,72,72,72,-48,-49,-50,-51,-52,-53,-54,-55,-57,72,-68,72,72,72,-72,72,]),'asterisco':([38,42,43,44,45,46,47,48,49,50,51,52,54,56,59,60,63,64,88,89,90,93,98,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,140,146,148,156,],[74,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,74,74,74,-73,-71,74,74,74,74,-69,-70,-41,-42,-43,-44,74,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,74,-68,74,74,74,-72,74,]),'barra':([38,42,43,44,45,46,47,48,49,50,51,52,54,56,59,60,63,64,88,89,90,93,98,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,140,146,148,156,],[75,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,75,75,75,-73,-71,75,75,75,75,-69,-70,-41,-42,-43,-44,75,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,75,-68,75,75,75,-72,75,]),'caret':([38,42,43,44,45,46,47,48,49,50,51,52,54,56,59,60,63,64,88,89,90,93,98,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,140,146,148,156,],[76,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,76,76,76,-73,-71,76,76,76,76,-69,-70,-41,-42,-43,-44,76,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,76,-68,76,76,76,-72,76,]),'modulo':([38,42,43,44,45,46,47,48,49,50,51,52,54,56,59,60,63,64,88,89,90,93,98,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,140,146,148,156,],[77,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,77,77,77,-73,-71,77,77,77,77,-69,-70,-41,-42,-43,-44,77,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,77,-68,77,77,77,-72,77,]),'mayor':([38,42,43,44,45,46,47,48,49,50,51,52,54,56,59,60,63,64,88,89,90,93,98,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,140,146,148,156,],[78,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,78,78,78,-73,-71,78,78,78,78,-69,-70,78,78,78,78,78,78,-48,-49,-50,-51,-52,-53,-54,-55,-57,78,-68,78,78,78,-72,78,]),'menor':([38,42,43,44,45,46,47,48,49,50,51,52,54,56,59,60,63,64,88,89,90,93,98,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,140,146,148,156,],[79,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,79,79,79,-73,-71,79,79,79,79,-69,-70,79,79,79,79,79,79,-48,-49,-50,-51,-52,-53,-54,-55,-57,79,-68,79,79,79,-72,79,]),'mayor_igual':([38,42,43,44,45,46,47,48,49,50,51,52,54,56,59,60,63,64,88,89,90,93,98,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,140,146,148,156,],[80,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,80,80,80,-73,-71,80,80,80,80,-69,-70,80,80,80,80,80,80,-48,-49,-50,-51,-52,-53,-54,-55,-57,80,-68,80,80,80,-72,80,]),'menor_igual':([38,42,43,44,45,46,47,48,49,50,51,52,54,56,59,60,63,64,88,89,90,93,98,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,140,146,148,156,],[81,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,81,81,81,-73,-71,81,81,81,81,-69,-70,81,81,81,81,81,81,-48,-49,-50,-51,-52,-53,-54,-55,-57,81,-68,81,81,81,-72,81,]),'igualacion':([38,42,43,44,45,46,47,48,49,50,51,52,54,56,59,60,63,64,88,89,90,93,98,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,140,146,148,156,],[82,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,82,82,82,-73,-71,82,82,82,82,-69,-70,82,82,82,82,82,82,82,82,82,82,-52,-53,-54,-55,-57,82,-68,82,82,82,-72,82,]),'diferenciacion':([38,42,43,44,45,46,47,48,49,50,51,52,54,56,59,60,63,64,88,89,90,93,98,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,140,146,148,156,],[83,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,83,83,83,-73,-71,83,83,83,83,-69,-70,83,83,83,83,83,83,83,83,83,83,-52,-53,-54,-55,-57,83,-68,83,83,83,-72,83,]),'or':([38,42,43,44,45,46,47,48,49,50,51,52,54,56,59,60,63,64,88,89,90,93,98,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,140,146,148,156,],[84,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,84,84,84,-73,-71,84,84,84,84,-69,-70,84,84,84,84,84,84,84,84,84,84,84,84,-54,84,-57,84,-68,84,84,84,-72,84,]),'and':([38,42,43,44,45,46,47,48,49,50,51,52,54,56,59,60,63,64,88,89,90,93,98,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,132,140,146,148,156,],[85,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,85,85,85,-73,-71,85,85,85,85,-69,-70,85,85,85,85,85,85,85,85,85,85,85,85,-54,-55,-57,85,-68,85,85,85,-72,85,]),'tipo':([42,43,44,45,46,47,48,49,50,51,52,59,60,63,67,88,89,93,98,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,131,148,],[-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,96,-73,-71,105,-47,-56,-69,-70,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,-68,-72,]),'coma':([42,43,44,45,46,47,48,49,50,51,52,60,62,63,64,88,89,92,93,98,101,102,104,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,131,140,148,153,],[-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,-73,99,-71,-40,-47,-56,99,-69,-70,-32,142,-31,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,-68,-39,-72,-30,]),'corchete_B':([42,43,44,45,46,47,48,49,50,51,52,53,60,63,64,88,89,92,93,98,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,131,140,148,],[-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,93,-73,-71,-40,-47,-56,131,-69,-70,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,148,-68,-39,-72,]),'dospuntos':([42,43,44,45,46,47,48,49,50,51,52,60,63,88,89,93,98,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,131,132,148,],[-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-74,-73,-71,-47,-56,-69,-70,-41,-42,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-57,-68,150,-72,]),'in':([55,],[95,]),'elseif':([71,87,128,155,],[112,-15,-14,112,]),'else':([71,87,128,155,],[113,-15,-14,113,]),'tipo_int64':([96,105,],[135,135,]),'tipo_float64':([96,105,],[136,136,]),'tipo_bool':([96,105,],[137,137,]),'tipo_char':([96,105,],[138,138,]),'tipo_string':([96,105,],[139,139,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'INS':([0,38,54,103,113,132,133,141,146,],[1,86,86,86,86,86,86,86,86,]),'I':([0,1,38,54,86,103,113,132,133,141,146,],[2,27,2,2,27,2,2,2,2,2,2,]),'ASIGNACION':([0,1,38,54,86,103,113,132,133,141,146,],[3,3,3,3,3,3,3,3,3,3,3,]),'FUNCION':([0,1,38,54,86,103,113,132,133,141,146,],[4,4,4,4,4,4,4,4,4,4,4,]),'STRUCT':([0,1,38,54,86,103,113,132,133,141,146,],[5,5,5,5,5,5,5,5,5,5,5,]),'LLAMADA':([0,1,21,22,26,30,33,38,39,40,41,53,54,61,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,91,95,99,103,112,113,132,133,141,146,150,],[6,6,42,42,42,42,42,6,42,42,42,42,6,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,6,42,42,42,6,42,6,6,6,6,6,42,]),'IF':([0,1,38,54,86,103,113,132,133,141,146,],[7,7,7,7,7,7,7,7,7,7,7,]),'WHILE':([0,1,38,54,86,103,113,132,133,141,146,],[8,8,8,8,8,8,8,8,8,8,8,]),'FOR':([0,1,38,54,86,103,113,132,133,141,146,],[9,9,9,9,9,9,9,9,9,9,9,]),'BREAK':([0,1,38,54,86,103,113,132,133,141,146,],[10,10,10,10,10,10,10,10,10,10,10,]),'CONTINUE':([0,1,38,54,86,103,113,132,133,141,146,],[11,11,11,11,11,11,11,11,11,11,11,]),'RETURN':([0,1,38,54,86,103,113,132,133,141,146,],[12,12,12,12,12,12,12,12,12,12,12,]),'ID':([0,1,21,22,26,30,33,38,39,40,41,53,54,61,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,91,95,99,103,112,113,132,133,141,146,150,],[14,14,45,45,45,45,45,14,45,45,45,45,14,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,14,45,45,45,14,45,14,14,14,14,14,45,]),'E':([21,22,26,30,33,39,40,41,53,61,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,91,95,99,112,150,],[38,54,56,59,64,88,89,90,64,59,59,114,115,116,117,118,119,120,121,122,123,124,125,126,127,130,132,140,146,156,]),'ACCESO_ARREGLO':([21,22,26,30,33,39,40,41,53,61,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,91,95,99,112,150,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'ARREGLO':([21,22,26,30,33,39,40,41,53,61,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,91,95,99,112,150,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'ASIGNACION_VALOR':([30,61,65,],[58,97,100,]),'EXP':([33,53,],[62,92,]),'ATR':([36,70,],[68,109,]),'A':([36,68,70,109,],[69,108,69,108,]),'BLOQUE':([38,54,103,113,132,133,141,146,],[71,94,143,147,149,151,152,155,]),'PAR':([66,],[102,]),'P':([66,142,],[104,153,]),'ELSEIF':([71,155,],[110,157,]),'ELSE':([71,155,],[111,158,]),'RANGO':([95,],[133,]),'TIPO':([96,105,],[134,144,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> INS","S'",1,None,None,None),
  ('INS -> INS I puntoycoma','INS',3,'p_INS','analyzer.py',201),
  ('INS -> I puntoycoma','INS',2,'p_INS','analyzer.py',202),
  ('I -> ASIGNACION','I',1,'p_I','analyzer.py',212),
  ('I -> FUNCION','I',1,'p_I','analyzer.py',213),
  ('I -> STRUCT','I',1,'p_I','analyzer.py',214),
  ('I -> LLAMADA','I',1,'p_I','analyzer.py',215),
  ('I -> IF','I',1,'p_I','analyzer.py',216),
  ('I -> WHILE','I',1,'p_I','analyzer.py',217),
  ('I -> FOR','I',1,'p_I','analyzer.py',218),
  ('I -> BREAK','I',1,'p_I','analyzer.py',219),
  ('I -> CONTINUE','I',1,'p_I','analyzer.py',220),
  ('I -> RETURN','I',1,'p_I','analyzer.py',221),
  ('I -> error puntoycoma','I',2,'p_I','analyzer.py',222),
  ('BLOQUE -> INS end','BLOQUE',2,'p_BLOQUE','analyzer.py',228),
  ('BLOQUE -> end','BLOQUE',1,'p_BLOQUE','analyzer.py',229),
  ('TIPO -> tipo_int64','TIPO',1,'p_TIPO','analyzer.py',235),
  ('TIPO -> tipo_float64','TIPO',1,'p_TIPO','analyzer.py',236),
  ('TIPO -> tipo_bool','TIPO',1,'p_TIPO','analyzer.py',237),
  ('TIPO -> tipo_char','TIPO',1,'p_TIPO','analyzer.py',238),
  ('TIPO -> tipo_string','TIPO',1,'p_TIPO','analyzer.py',239),
  ('ASIGNACION -> ID igual ASIGNACION_VALOR','ASIGNACION',3,'p_ASIGNACION','analyzer.py',245),
  ('ASIGNACION -> global id igual ASIGNACION_VALOR','ASIGNACION',4,'p_ASIGNACION','analyzer.py',246),
  ('ASIGNACION -> global id','ASIGNACION',2,'p_ASIGNACION','analyzer.py',247),
  ('ASIGNACION -> local id igual ASIGNACION_VALOR','ASIGNACION',4,'p_ASIGNACION','analyzer.py',248),
  ('ASIGNACION -> local id','ASIGNACION',2,'p_ASIGNACION','analyzer.py',249),
  ('ASIGNACION_VALOR -> E','ASIGNACION_VALOR',1,'p_ASIGNACION_VALOR','analyzer.py',268),
  ('ASIGNACION_VALOR -> E tipo TIPO','ASIGNACION_VALOR',3,'p_ASIGNACION_VALOR','analyzer.py',269),
  ('FUNCION -> function id parentesis_A PAR parentesis_B BLOQUE','FUNCION',6,'p_FUNCION','analyzer.py',280),
  ('FUNCION -> function id parentesis_A parentesis_B BLOQUE','FUNCION',5,'p_FUNCION','analyzer.py',281),
  ('PAR -> PAR coma P','PAR',3,'p_PAR','analyzer.py',292),
  ('PAR -> P','PAR',1,'p_PAR','analyzer.py',293),
  ('P -> id','P',1,'p_P','analyzer.py',302),
  ('STRUCT -> struct id ATR end','STRUCT',4,'p_STRUCT','analyzer.py',308),
  ('STRUCT -> mutable struct id ATR end','STRUCT',5,'p_STRUCT','analyzer.py',309),
  ('ATR -> ATR A','ATR',2,'p_ATR','analyzer.py',321),
  ('ATR -> A','ATR',1,'p_ATR','analyzer.py',322),
  ('A -> id tipo TIPO puntoycoma','A',4,'p_A','analyzer.py',331),
  ('A -> id puntoycoma','A',2,'p_A','analyzer.py',332),
  ('EXP -> EXP coma E','EXP',3,'p_EXP','analyzer.py',343),
  ('EXP -> E','EXP',1,'p_EXP','analyzer.py',344),
  ('E -> E mas E','E',3,'p_E','analyzer.py',353),
  ('E -> E menos E','E',3,'p_E','analyzer.py',354),
  ('E -> E asterisco E','E',3,'p_E','analyzer.py',355),
  ('E -> E barra E','E',3,'p_E','analyzer.py',356),
  ('E -> E caret E','E',3,'p_E','analyzer.py',357),
  ('E -> E modulo E','E',3,'p_E','analyzer.py',358),
  ('E -> menos E','E',2,'p_E','analyzer.py',359),
  ('E -> E mayor E','E',3,'p_E','analyzer.py',360),
  ('E -> E menor E','E',3,'p_E','analyzer.py',361),
  ('E -> E mayor_igual E','E',3,'p_E','analyzer.py',362),
  ('E -> E menor_igual E','E',3,'p_E','analyzer.py',363),
  ('E -> E igualacion E','E',3,'p_E','analyzer.py',364),
  ('E -> E diferenciacion E','E',3,'p_E','analyzer.py',365),
  ('E -> E or E','E',3,'p_E','analyzer.py',366),
  ('E -> E and E','E',3,'p_E','analyzer.py',367),
  ('E -> not E','E',2,'p_E','analyzer.py',368),
  ('E -> parentesis_A E parentesis_B','E',3,'p_E','analyzer.py',369),
  ('E -> LLAMADA','E',1,'p_E','analyzer.py',370),
  ('E -> ACCESO_ARREGLO','E',1,'p_E','analyzer.py',371),
  ('E -> ARREGLO','E',1,'p_E','analyzer.py',372),
  ('E -> ID','E',1,'p_E','analyzer.py',373),
  ('E -> int64','E',1,'p_E','analyzer.py',374),
  ('E -> float64','E',1,'p_E','analyzer.py',375),
  ('E -> bool','E',1,'p_E','analyzer.py',376),
  ('E -> char','E',1,'p_E','analyzer.py',377),
  ('E -> string','E',1,'p_E','analyzer.py',378),
  ('E -> nothing','E',1,'p_E','analyzer.py',379),
  ('ARREGLO -> corchete_A EXP corchete_B','ARREGLO',3,'p_ARREGLO','analyzer.py',404),
  ('ARREGLO -> corchete_A corchete_B','ARREGLO',2,'p_ARREGLO','analyzer.py',405),
  ('LLAMADA -> id parentesis_A EXP parentesis_B','LLAMADA',4,'p_LLAMADA','analyzer.py',412),
  ('LLAMADA -> id parentesis_A parentesis_B','LLAMADA',3,'p_LLAMADA','analyzer.py',413),
  ('ACCESO_ARREGLO -> id corchete_A E corchete_B','ACCESO_ARREGLO',4,'p_ACCESO_ARREGLO','analyzer.py',424),
  ('ID -> ID punto id','ID',3,'p_ID','analyzer.py',431),
  ('ID -> id','ID',1,'p_ID','analyzer.py',432),
  ('IF -> if E BLOQUE','IF',3,'p_IF','analyzer.py',441),
  ('IF -> if E BLOQUE ELSEIF','IF',4,'p_IF','analyzer.py',442),
  ('IF -> if E BLOQUE ELSE','IF',4,'p_IF','analyzer.py',443),
  ('ELSEIF -> elseif E BLOQUE','ELSEIF',3,'p_ELSEIF','analyzer.py',454),
  ('ELSEIF -> elseif E BLOQUE ELSEIF','ELSEIF',4,'p_ELSEIF','analyzer.py',455),
  ('ELSEIF -> elseif E BLOQUE ELSE','ELSEIF',4,'p_ELSEIF','analyzer.py',456),
  ('ELSE -> else BLOQUE','ELSE',2,'p_ELSE','analyzer.py',467),
  ('WHILE -> while E BLOQUE','WHILE',3,'p_WHILE','analyzer.py',474),
  ('FOR -> for id in E BLOQUE','FOR',5,'p_FOR','analyzer.py',481),
  ('FOR -> for id in RANGO BLOQUE','FOR',5,'p_FOR','analyzer.py',482),
  ('RANGO -> E dospuntos E','RANGO',3,'p_RANGO','analyzer.py',489),
  ('BREAK -> break','BREAK',1,'p_BREAK','analyzer.py',496),
  ('CONTINUE -> continue','CONTINUE',1,'p_CONTINUE','analyzer.py',502),
  ('RETURN -> return E','RETURN',2,'p_RETURN','analyzer.py',508),
  ('RETURN -> return','RETURN',1,'p_RETURN','analyzer.py',509),
]