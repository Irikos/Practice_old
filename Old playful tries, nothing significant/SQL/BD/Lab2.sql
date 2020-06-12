-- 1
select first_name || ' ' || last_name || ' castiga ' || salary || concat(' dar doreste ', salary * 3)
from employees;

--2 
select initcap(first_name), upper(last_name), length(concat(first_name, last_name))
from employees
where substr(last_name, 1, 1) = 'J' or 
      substr(last_name, 1, 1) = 'M' or
      substr(upper(last_name), 3, 1) = 'A'
order by length(concat(first_name, last_name)) desc;

select initcap(first_name), upper(last_name), length(concat(first_name, last_name))
from employees
where last_name like ('J%') or 
      last_name like ('M%') or
      upper(last_name) like ('__A%')
order by length(concat(first_name, last_name)) desc;

-- 3
select employee_id, last_name, department_id
from employees
where trim(first_name) like ('%Steven%');

-- 4
select employee_id id, last_name as nume, length(last_name) "Lungime nume", instr(lower(last_name), 'a', 1) "Pozitie litera a"
from employees
where lower(substr(last_name, -1, 1)) = 'e';

-- 5 not correct
select e.last_name
from employees e, dual d
where mod(((sysdate - e.hire_date) / 7), 2) != 0;

-- 6
select employee_id, last_name, salary, trunc(salary * 115/100, 2) as "Salariu nou", round((salary * 115/100) / 100, 2) as "Numar sute"
from employees
where mod(salary, 1000) != 0;

-- 7
select last_name "Nume angajat", hire_date "Data angajarii"
from employees
where commission_pct > 0;

-- 8
select to_char(sysdate + 30, 'month D YYYY HH24 MI SS')
from dual;

-- 9
select to_date('31-dec-2017', 'dd-mon-yyyy') - sysdate
from dual;

-- 12
select last_name, months_between(hire_date, sysdate) as luni
from employees, dual
order by luni;

-- 13
select last_name, hire_date, to_char(hire_date, 'D') as Zi
from employees
order by Zi;

-- 14
select last_name, NVL(to_char(commission_pct), 'Fara comision') as Comision
from employees;

select last_name, decode(commission_pct, null, 'Fara comision', commission_pct) as Comision
from employees;

-- 15
select last_name, salary, commission_pct 
from employees
where salary > 10000;

-- 16
select last_name, job_id, salary, 
case (job_id)
when 'IT_PROG' then salary * 120 / 100
when 'SA_REP' then salary * 125 / 100
when 'SA_MAN' then salary * 135 / 100
else salary
end as "Salariu renegociat"
from employees;

-- 17
select employee_id, last_name, d.department_name
from employees e, departments d
where e.department_id = d.department_id;


select employee_id, last_name, department_name
from employees
inner join departments on employees.department_id = departments.department_id;

-- 18
select job_title
from jobs
inner join employees on jobs.JOB_ID = employees.job_id
where department_id = 30;

-- 19
select last_name, department_name, location_id
from employees
inner join departments on employees.department_id = departments.department_id
where commission_pct > 0;

-- 20
select last_name, department_name
from employees
inner join departments on employees.department_id = departments.department_id
where upper(last_name) like '%A%';

-- 21
select e.last_name, j.job_title, d.department_id, d.department_name, l.city
from (((departments d
inner join employees e on e.department_id = d.department_id)
inner join jobs j on e.job_id = j.job_id)
inner join locations l on d.LOCATION_ID = l.LOCATION_ID)
where l.city like '%Oxford%';

-- 22
select e.employee_id as Ang#, e.last_name as Angajat, e.manager_id as Mgr#, d.last_name as Manager
from employees e
inner join employees d on e.manager_id = d.employee_id; 

-- 23
select e.employee_id as Ang#, e.last_name as Angajat, e.manager_id as Mgr#, d.last_name as Manager
from employees e
left join employees d on e.manager_id = d.employee_id; 

-- 24
select e.last_name, e.department_id, d.last_name
from employees e
right join employees d on d.department_id = e.department_id; 

-- 25
desc jobs;


select e.job_id, j.job_title, d.department_name, sum(e.salary)
from employees e
inner join jobs j on e.job_id = j.job_id
inner join departments d on e.department_id = d.department_id
group by (e.job_id, j.job_title, d.department_name);

select e.job_id, j.job_title, d.department_name, sum(e.salary)
from jobs j
inner join employees e on e.job_id = j.job_id
inner join departments d on e.department_id = d.department_id
group by (e.job_id, j.job_title, d.department_name);

-- 26
select e.last_name, e.hire_date 
from employees e
where e.hire_date > (select hire_date from employees where last_name like '%Gates%');


-- 27
select e.last_name, e.hire_date, d.last_name, d.hire_date
from employees e
inner join employees d on e.hire_date <  d.hire_date and e.manager_id = d.employee_id;
