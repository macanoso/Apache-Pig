/*
Pregunta
===========================================================================

Para responder la pregunta use el archivo `data.csv`.

Escriba el código equivalente a la siguiente consulta SQL.

   SELECT  
       firstname,
       SUBSTRING_INDEX(firstname, 'a', 1)
   FROM 
       u;

Escriba el resultado a la carpeta `output` del directorio actual. Para la 
evaluación, pig sera eejcutado ejecutado en modo local:

$ pig -x local -f pregunta.pig

        >>> Escriba su respuesta a partir de este punto <<<
*/
data = LOAD 'data.csv' USING PigStorage(',')
    AS (
            Id:int,
            Name:chararray,
            LastName:chararray,
            Birth:chararray,
            color:chararray,
            value:int
    );

birthday = FOREACH data GENERATE  REGEX_EXTRACT(Birth,'(.*)-(.*)-(.*)', 2);
STORE birthday INTO 'output' USING PigStorage(',');
