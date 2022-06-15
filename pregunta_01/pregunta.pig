/* 
Pregunta
===========================================================================

Para el archivo `data.tsv` compute la cantidad de registros por letra.
Almacene los resultados separados por comas. 

Escriba el resultado a la carpeta `output` del directorio actual. Para la 
evaluación, pig sera eejcutado ejecutado en modo local:

$ pig -x local -f pregunta.pig

        >>> Escriba su respuesta a partir de este punto <<<
*/

data = LOAD 'data.tsv' AS (Words:chararray, Date:chararray, Number:int);
new_word = FOREACH data GENERATE Words as word;
group_by = GROUP new_word BY word;
counter = FOREACH group_by GENERATE group, COUNT(new_word);
STORE counter INTO 'output' USING PigStorage(',');
