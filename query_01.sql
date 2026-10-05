-- Query 1 - Salário, departamento e cargo
-- EMPLOYEES com LEFT JOIN em DEPARTMENTS e JOBS

-- HR.DEPARTMENTS
SELECT
    DEPARTMENT_ID,
    DEPARTMENT_NAME,
    MANAGER_ID,
    LOCATION_ID
FROM
    HR.DEPARTMENTS;

-- HR.JOBS
SELECT
    JOB_ID,
    JOB_TITLE,
    MIN_SALARY,
    MAX_SALARY
FROM
    HR.JOBS;

-- HR.EMPLOYEES
SELECT
    EMPLOYEE_ID,
    FIRST_NAME,
    LAST_NAME,
    EMAIL,
    PHONE_NUMBER,
    HIRE_DATE,
    JOB_ID,
    SALARY,
    COMMISSION_PCT,
    MANAGER_ID,
    DEPARTMENT_ID
FROM
    HR.EMPLOYEES;


-- Consulta o primero nome, sobrenome, salario, departamento e cargo em que um funcionario trabalha, 
-- sendo seu salario maior que 0 e consultado o valor correto do cargo na tabela inteira de departments 
SELECT 
    funcionarios.EMPLOYEE_ID, 
    funcionarios.FIRST_NAME, 
    funcionarios.LAST_NAME, 
    funcionarios.SALARY, 
    funcionarios.DEPARTMENT_ID, 
    departamentos.DEPARTMENT_NAME 
FROM HR.EMPLOYEES funcionarios 
LEFT JOIN 
    HR.DEPARTMENTS departamentos ON funcionarios.DEPARTMENT_ID = departamentos.DEPARTMENT_ID 
LEFT JOIN 
    HR.JOBS cargo ON funcionarios.JOB_ID = cargo.JOB_ID 
WHERE 
    funcionarios.SALARY > 0 
ORDER BY 
    funcionarios.FIRST_NAME;