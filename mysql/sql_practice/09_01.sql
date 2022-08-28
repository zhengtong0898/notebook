-- 查询员工的 id, salary, 按照 department_name 排序

select `department_id` as `id`, `salary`
from employees as e
order by (
    select department_name
    from departments as d
    where e.department_id = d.department_id
)


-- 结论: 
-- 1. 使用了相关子查询语法.
-- 2. 子查询写在 order by 这一行, 如何理解?
--    根据SQL执行的顺序来推断出它的工作原理,
--    假设SQl是这样的: 
--    select `department_id`, `salary` 
--    from employees 
--    order by `email`;
--    第一步读取表的所有数据, 每次仅读取一条,      (无筛选: 原始数据集)
--    第二步筛选列, 最终一行仅仅显示两个列,       (有筛选: 仅仅提取两列, 列数缩小, 行数没有所缩小)
--    第三步排序, 按email字段排序               (无筛选, 开辟一个链表对象进行逐行比较的插入排序)
--    
--    回到上面的SQL:
--    由于使用了相关子查询, 因此每次都只是吐一条数据出来给order by,
--    那么 order 就可以对它进行比较排序了.  
--
--    拓展思考:
--    如果order by 右侧的子查询每次吐出来的数据是多条, 
--    那么还能对原始表做比较排序吗?  
--    答案是不行, 因为排序需要的数据集要和一一对应.
--    select `department_id` as `id`, `salary`
--    from employees as e
--    order by  (
--        SELECT 1 as column_name FROM DUAL UNION ALL
--        SELECT 2 FROM DUAL UNION ALL
--        SELECT 3 FROM DUAL UNION ALL
--        SELECT 4 FROM DUAL
--    );
