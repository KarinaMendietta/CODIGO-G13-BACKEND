-- funciones
DELIMITER $$
CREATE FUNCTION fn_contar_cursos()
    RETURNS INT UNSIGNED
BEGIN
    DECLARE total INT UNSIGNED;

    select count(*) into total from tbl_curso;

    RETURN total;
END
$$
DELIMITER ;

SELECt fn_contar_cursos();