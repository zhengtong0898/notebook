-- https://www.nowcoder.com/practice/218ae58dfdcd4af195fff264e062138f
SELECT `SQL1_employees`.`emp_no`,
       `SQL1_employees`.`birth_date`,
       `SQL1_employees`.`first_name`,
       `SQL1_employees`.`last_name`,
       `SQL1_employees`.`gender`,
       `SQL1_employees`.`hire_date`
FROM `SQL1_employees`
ORDER BY `SQL1_employees`.`hire_date`
DESC LIMIT 1;
