-- 1
select distinct l.city, c.country_name, count(e.employee_id)
from locations l
inner join countries c on l.country_id = c.country_id
inner join departments d on d.location_id = l.location_id
inner join employees e on e.department_id = d.department_id
group by (l.city, c.country_name);

-- 2
select last_name, salary
from employees
where rownum <= 5
order by salary desc;

-- 3
select count(t.last_name) from 
(select e.last_name, count(jh.employee_id) as previousJobs
from employees e
inner join job_history jh on e.employee_id = jh.employee_id
group by e.last_name) t
where t.previousJobs >= 2;

-- 4
select max(t.country_name)
from (select c.country_name, count(employee_id)
      from countries c
      inner join locations l on c.country_id = l.country_id
      inner join departments d on d.location_id = l.location_id
      inner join employees e on e.department_id = d.department_id
      group by c.country_name) t;
      
-- 5
select count(*)
from employees e
where e.manager_id is null;

-- 6
select avg(commission_pct) from employees
where commission_pct is not null;

-- 7
select j.job_title as Job
from jobs j
group by j.job_title;

-- cum fac sa apara pe departamentul 30 si 60?
select j.job_title, sum(e.salary) as total
from employees e
inner join jobs j on j.job_id = e.job_id
group by j.job_title;


