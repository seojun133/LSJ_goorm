use mydb;
SET SQL_SAFE_UPDATES = 0;

create table customers (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(1000),
    age INTEGER,
    city VARCHAR(50)
    );
    
create table products(
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50),
    price INTEGER,
    stock INTEGER
);

create table orders (
	id INT AUTO_INCREMENT PRIMARY KEY,
	customer_id INT NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES customers(id),
    product_id INT NOT NULL,
    FOREIGN KEY(product_id) REFERENCES products(id),
    quantity INTEGER,
    order_date date
);

insert into customers (name, email, age, city)
values
('김철수', 'kim@example.com', 28, 'Seoul'),
('이서준', 'lee@eample.com', 27, 'Seoul'),
('최소연', 'choi@example.com', 33, 'Gyeongki'),
('박동수', 'park@example.com', 31, 'Busan'),
('장원영', 'jang@example.com', 22, 'Daegu'),
('오지은', 'oh@example.com', 38, 'Seoul');

select * from customers;
select name, age from customers where age >= 30;
select email from customers where city = 'Seoul';

set foreign_key_checks = 0;
delete from customers where city = 'Busan';
set foreign_key_checks = 0;

update customers
set email = 'kimcs@example.com'
where name = '김철수'; 


insert into products (name, price, stock)
values
('Airpods Pro', 329000, 20),
('IPhone16', 1400000, 7),
('MacBook', 2490000, 0),
('Magic Mouse', 90000, 0),
('Magic Keyboard', 99000, 14);

select * from products;
select * from products where price >= 100000 and stock <= 10;

update products
set stock = 0
where name = 'Magic Mouse';

delete from products where stock = 0;

insert into orders (customer_id, product_id, quantity, order_date)
values
(3, 4, 1, '2025-03-01'),
(7, 5, 3, '2024-12-25'),
(5, 1, 2, '2025-01-03'),
(4, 5, 1, '2022-05-16'),
(1, 6, 1, '2023-05-15');

select * from orders;
select * from orders where order_date like '2025%';

SET SQL_SAFE_UPDATES = 1;