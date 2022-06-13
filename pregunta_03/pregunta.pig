/*
Pregunta
===========================================================================

Obtenga los cinco (5) valores más pequeños de la 3ra columna.

Escriba el resultado a la carpeta `output` del directorio actual. Para la 
evaluación, pig sera eejcutado ejecutado en modo local:

$ pig -x local -f pregunta.pig

        >>> Escriba su respuesta a partir de este punto <<<
*/
data = LOAD 'data.tsv' AS (Words:chararray, Date:chararray, Numbers:int);
number = FOREACH data GENERATE Numbers as numbers;
order_by = ORDER number BY numbers ASC;
limit_data = LIMIT order_by 5; 
STORE limit_data INTO 'output' USING PigStorage(',');