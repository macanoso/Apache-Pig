/*
Pregunta
===========================================================================

Para el archivo `data.tsv` compute la cantidad de registros por letra de la 
columna 2 y clave de al columna 3; esto es, por ejemplo, la cantidad de 
registros en tienen la letra `b` en la columna 2 y la clave `jjj` en la 
columna 3 es:

  ((b,jjj), 216)

Escriba el resultado a la carpeta `output` del directorio actual. Para la 
evaluación, pig sera eejcutado ejecutado en modo local:

$ pig -x local -f pregunta.pig

        >>> Escriba su respuesta a partir de este punto <<<
*/
data = LOAD 'data.tsv' AS (
        word:chararray, 
        bag_info:BAG{A:tuple(B:chararray)}, 
        map_info:map[]
    );
read_data = FOREACH data GENERATE flatten(bag_info) as word, flatten(map_info) as word_long;
joined = FOREACH read_data GENERATE(word,word_long) as tuple_data; 
group_by = GROUP joined BY tuple_data;
counter = FOREACH group_by GENERATE group, COUNT(joined);
STORE counter INTO 'output' USING PigStorage(',');
