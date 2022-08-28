-- job_history 表描述
-- 这张表记录一个员工的工作经历, 因此一个员工编号多条数据表示该员工有多份工作经历.  
-- 
-- job_history 表字段
-- mysql> desc job_history;
-- +---------------+-------------+------+-----+---------+-------+
-- | Field         | Type        | Null | Key | Default | Extra |
-- +---------------+-------------+------+-----+---------+-------+
-- | employee_id   | int(6)      | NO   | PRI | NULL    |       |
-- | start_date    | date        | NO   | PRI | NULL    |       |
-- | end_date      | date        | NO   |     | NULL    |       |
-- | job_id        | varchar(10) | NO   | MUL | NULL    |       |
-- | department_id | int(4)      | YES  | MUL | NULL    |       |
-- +---------------+-------------+------+-----+---------+-------+
-- 5 rows in set (0.00 sec)
--
-- 
-- job_history 表数据
-- mysql> SELECT * FROM job_history;
-- +-------------+------------+------------+------------+---------------+
-- | employee_id | start_date | end_date   | job_id     | department_id |
-- +-------------+------------+------------+------------+---------------+
-- |         101 | 1989-09-21 | 1993-10-27 | AC_ACCOUNT |           110 |
-- |         101 | 1993-10-28 | 1997-03-15 | AC_MGR     |           110 |
-- |         102 | 1993-01-13 | 1998-07-24 | IT_PROG    |            60 |
-- |         114 | 1998-03-24 | 1999-12-31 | ST_CLERK   |            50 |
-- |         122 | 1999-01-01 | 1999-12-31 | ST_CLERK   |            50 |
-- |         176 | 1998-03-24 | 1998-12-31 | SA_REP     |            80 |
-- |         176 | 1999-01-01 | 1999-12-31 | SA_MAN     |            80 |
-- |         200 | 1987-09-17 | 1993-06-17 | AD_ASST    |            90 |
-- |         200 | 1994-07-01 | 1998-12-31 | AC_ACCOUNT |            90 |
-- |         201 | 1996-02-17 | 1999-12-19 | MK_REP     |            20 |
-- +-------------+------------+------------+------------+---------------+
-- 10 rows in set (0.00 sec)



-- 题目:  
-- 若 employees 表中 employee_id 与 job_history 表中 employee_id 相同的数目不小于2, 
-- 输出这些相同 id 的员工的 employee_id, last_name 和 job_id.  

SELECT employee_id, last_name, job_id
FROM   employees as em
WHERE  (                                                    -- 相关子查询
            SELECT count(*)                                 
            FROM   job_history as jh
            WHERE  jh.employee_id = em.employee_id          -- 关联外表
       ) >= 2;
