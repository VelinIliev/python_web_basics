CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    category_id INT REFERENCES categories(id)
);

INSERT INTO employees (first_name, last_name)
VALUES
        ('Ivan', 'Petrov'),
        ('Велин', 'Илиев');

SELECT first_name FROM employees
WHERE first_name LIKE 'I%';

UPDATE employees
SET first_name = 'Velin', last_name = 'Iliev'
WHERE id = 2;

ALTER TABLE employees
ADD COLUMN salary DECIMAL NOT NULL DEFAULT 0;

INSERT INTO categories (name)
VALUES ('Beverages'), ('Food');

INSERT INTO products (name, category_id)
VALUES ('Beer', 1), ('Bread', 2);

SELECT
    products.name AS product,
    c.name AS category
FROM products
JOIN categories AS c
    ON products.category_id = c.id;

CREATE TABLE test (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    name VARCHAR(20)
);

INSERT INTO test(name)
VALUES ('rest');

INSERT INTO test(name)
VALUES ('test');

SELECT * FROM test;

ALTER TABLE test
ADD COLUMN date DATE DEFAULT NOW();

SELECT * FROM test LIMIT 1;

INSERT INTO test(name)
VALUES ('gest');

UPDATE employees
SET salary = salary + 100
WHERE salary <= 10000;

SELECT * FROM employees;

UPDATE employees
SET salary = salary + 10000
WHERE first_name = 'Velin';

SELECT * FROM employees;

ALTER TABLE employees
ADD COLUMN position VARCHAR(30) DEFAULT NULL;

UPDATE employees
SET position = 'graphic designer'
WHERE first_name = 'Velin';

UPDATE employees
SET position = 'web developer'
WHERE first_name = 'Ivan';

SELECT * FROM employees
ORDER BY salary DESC;

UPDATE employees
SET position = 'senior web developer'
WHERE first_name = 'Ivan';
