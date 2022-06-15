/*
Pregunta
===========================================================================

Para responder la pregunta use el archivo `data.csv`.

Escriba el codigo en Pig para manipulación de fechas que genere la siguiente
salida.

   1971-07-08,08,8,jue,jueves
   1974-05-23,23,23,jue,jueves
   1973-04-22,22,22,dom,domingo
   1975-01-29,29,29,mie,miercoles
   1974-07-03,03,3,mie,miercoles
   1974-10-18,18,18,vie,viernes
   1970-10-05,05,5,lun,lunes
   1969-02-24,24,24,lun,lunes
   1974-10-17,17,17,jue,jueves
   1975-02-28,28,28,vie,viernes
   1969-12-07,07,7,dom,domingo
   1973-12-24,24,24,lun,lunes
   1970-08-27,27,27,jue,jueves
   1972-12-12,12,12,mar,martes
   1970-07-01,01,1,mie,miercoles
   1974-02-11,11,11,lun,lunes
   1973-04-01,01,1,dom,domingo
   1973-04-29,29,29,dom,domingo

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

read = FOREACH data GENERATE ToDate(Birth,'yyyy-MM-dd') as date;
data = FOREACH read GENERATE ToString(date, 'yyyy-MM-dd') as completa,                              
                              ToString(date, 'dd') as dia, 
                              ToString(date, 'd') as ndia,
                              LOWER(ToString(date, 'EEEE')) as day,
                              LOWER(ToString(date, 'E')) as d;

data = FOREACH data GENERATE completa, dia, ndia, REPLACE(d,'thu','jue') AS d, REPLACE(day,'thursday','jueves') AS day;
data = FOREACH data GENERATE completa, dia, ndia, REPLACE(d,'sun','dom') AS d, REPLACE(day,'sunday','domingo') AS day;
data = FOREACH data GENERATE completa, dia, ndia, REPLACE(d,'fri','vie') AS d, REPLACE(day,'friday','viernes') AS day;
data = FOREACH data GENERATE completa, dia, ndia, REPLACE(d,'mon','lun') AS d, REPLACE(day,'monday','lunes') AS day;
data = FOREACH data GENERATE completa, dia, ndia, REPLACE(d,'tue','mar') AS d, REPLACE(day,'tuesday','martes') AS day;
data = FOREACH data GENERATE completa, dia, ndia, REPLACE(d,'wed','mie') AS d, REPLACE(day,'wednesday','miercoles') AS day;
STORE data INTO 'output' USING PigStorage(',');