/*
Pregunta
===========================================================================

Para el archivo `data.tsv` Calcule la cantidad de registros por clave de la 
columna 3. En otras palabras, cuántos registros hay que tengan la clave 
`aaa`?

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
data_read = FOREACH data GENERATE flatten(map_info) as word; 
group_by = GROUP data_read BY word;
counter = FOREACH group_by GENERATE group, COUNT(data_read);
STORE counter INTO 'output' USING PigStorage(',');
