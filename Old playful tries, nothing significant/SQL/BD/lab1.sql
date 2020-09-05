select employee_id, last_name, salary * 12 "ANNUAL SALARY" 
from employees;

-- 3
describe employees;

-- 4 
select * from employees;

-- 5
select employee_id, first_name, last_name, job_id, hire_date
from employees;

-- 6
select distinct job_id
from employees;

-- 7
select last_name || ', ' || job_id as "Angajat si titlu"
from employees;

-- 8
select employee_id || ', ' || first_name || ', ' ||  last_name || ', ' ||  job_id || ', ' ||  hire_date as "Informatii complete"
from employees;

-- 9
select last_name, salary 
from employees
where salary > 2850;

-- 10
select last_name, department_id
from employees
where employee_id = 104;

-- 11
select last_name, salary 
from employees
where salary not between 1500 and 2850;
--where salary < 1500 or salary > 2850;

-- 12
select last_name, job_id, hire_date 
from employees
where hire_date between '20-FEB-1987' and '1-MAY-1989'
order by hire_date;

-- 13
select last_name, department_id 
from employees
where department_id in (10, 30)
order by last_name ASC;

-- 14
select last_name Angajat, salary Salariu
from employees
where department_id in (10, 30) and salary > 3500;

-- 15
select sysdate
from dual;

-- 16 
select last_name, hire_date
from employees
where hire_date like ('%87%');

select last_name, hire_date
from employees
where to_char(hire_date, 'YYYY') = 1987;

-- 17
select last_name, job_id
from employees
where manager_id is null;

-- 18
select last_name, salary, commission_pct * salary 
from employees
where commission_pct > 0
order by salary desc, commission_pct desc;

-- 19
select last_name, salary, commission_pct * salary 
from employees
order by salary desc, commission_pct desc;

-- 20
select last_name from employees
where last_name LIKE ('__a%');

-- 21
select last_name, department_id, manager_id
from employees
where last_name like ('%ll%') and (department_id = 30 or manager_id = 101);

-- 22
select last_name, j.job_title, salary
from employees e, jobs j
where e.job_id = j.JOB_ID 
      and (j.job_title like ('%Clerk%') or j.job_title like ('%Rep%'))
      and salary not in (1000, 2000, 3000);
      
-- 23
select last_name, salary, commission_pct * salary
from employees
where salary > (salary * commission_pct * 5);
