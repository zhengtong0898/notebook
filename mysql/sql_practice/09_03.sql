-- 查询公司管理者的employee_id, last_name, job_id, department_id信息

-- 内连接(intersection): 
-- rhs是所有管理者信息.  
-- 由于是跟employee_id的manager_id做过滤, 因此 rhs 是存在冗余的情况.
-- 因此需要做去重, 这里可以使用 DISTINCT 也可以使用GROUP BY.
SELECT  DISTINCT    rhs.employee_id, rhs.last_name, rhs.job_id, rhs.department_id
FROM                employees AS lhs INNER JOIN employees AS rhs
ON                  lhs.manager_id = rhs.employee_id;


-- 子查询(IN):
-- IN 操作遍历所有子查询中的所有行, 运行效率是 O(n^2)
SELECT employee_id, last_name, job_id, department_id
FROM employees 
WHERE employee_id IN (
                        SELECT DISTINCT manager_id
                        FROM            employees
                     );
                         

-- 子查询(EXIST):
-- EXISTS 操作遍历子查询命中即停止, 运行效率最差是 O(n^2), 最优效率是O(n), 均摊效率是O(n^2/2)
SELECT employee_id, last_name, job_id, department_id 
FROM employees AS lhs 
WHERE EXISTS (
                SELECT  *
                FROM    employees AS rhs
                WHERE   lhs.employee_id = rhs.manager_id
            );
