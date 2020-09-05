set serveroutput on
DECLARE
  v_data_achizitie DATE := SYSDATE;
  v_data_achizitie2 DATE DEFAULT SYSDATE;
BEGIN
  DBMS_OUTPUT.PUT_LINE(v_data_achizitie);
END;

-- 1
DECLARE 
  v_message varchar2(20) := 'Hello, World!';
  v_learnMessage varchar2(20) := 'Invat PL/SQL';
BEGIN
  dbms_output.put_line(v_message);
  dbms_output.put_line(v_learnMessage);
END;

-- 2
DECLARE
  v_oras locations.city%TYPE;
BEGIN
  select l.city into v_oras 
  from locations l
  inner join departments d on l.location_id = d.location_id
  where d.department_id = 30;
  
  dbms_output.put_line(v_oras);
END;

-- 3
DECLARE
  v_media_sal employees.salary%TYPE;
  v_dept integer;
BEGIN
  select avg(e.salary), e.department_id into v_media_sal, v_dept
  from employees e
  where e.department_id = 50
  group by e.department_id;
  dbms_output.put_line('Media salariului in departamentul ' || v_dept || ' este: ' || v_media_sal);
END;

-- 4
accept myvar char prompt 'Dati numarul departamentului: '
DECLARE
  v_nr_angajati integer := 0;
  v_departament employees.department_id%TYPE;
  v_departament_inspectat employees.department_id%TYPE default '&myvar';
BEGIN

  select count(e.employee_id), e.department_id into v_nr_angajati, v_departament
  from employees e
  where e.department_id = v_departament_inspectat
  group by e.department_id;
  
  case
    when v_nr_angajati > 30 then 
      dbms_output.put_line(' departament mare');
    when v_nr_angajati > 10 and v_nr_angajati < 30 then 
      dbms_output.put_line(' departament mijlociu');
    when v_nr_angajati < 10 then 
      dbms_output.put_line(' departament mic');
  end case;
END;


-- 5
declare
  p_cod_dep employees.department_id%TYPE default 50;
  p_com integer default 0;
  v_lines_affected integer default 0;
begin
  select dbms_random.value(0, 100) into p_com
  from dual;
  
  if v_lines_affected = 0 then
    dbms_output.put_line('Nicio linie actualizata');
  else
    dbms_output.put_line(v_lines_affected);
  end if;
  dbms_output.put_line(p_com);
end;
  
-- 8
accept myFact char prompt 'Dati factorialul: '
declare 
  v_fact integer default 1; 
begin
  for i in 1..'&myFact' loop
    v_fact := v_fact * i;
  end loop;
  dbms_output.put_line(v_fact);
end;
--
--accept myv2 char prompt 'Enter a last name: '
--declare
--v_test varchar(20) := '&myv2';
--begin
--dbms_output.put_line(v_test);
--end;

