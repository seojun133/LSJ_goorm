show databases;
create database mydb;
use mydb;
drop database mydb;

-- 새로 시작

create database mydb;
use mydb;

CREATE TABLE burgers (
  id INTEGER PRIMARY KEY,
  name VARCHAR(50),
  price INTEGER,
  gram INTEGER,
  kcal INTEGER,
  protein INTEGER
);

DESC burgers;


INSERT INTO burgers (
  id ,
  name ,
  price ,
  gram ,
  kcal ,
  protein 
)  values(10, 'healthy burger', 5000, 470, 20, 25);

INSERT INTO burgers (
  id ,
  name ,
  price ,
  gram ,
  kcal ,
  protein 
) values (2, 'chicken burger', 4500, 320, 30, 10);  

select * from burgers;
    
CREATE TABLE customers (
	name VARCHAR(50),
    age INTEGER,
    favorite_burger VARCHAR(50)
);

DESC customers;

INSERT INTO customers (
	name,
    age,
    favorite_burger
) values('SeoJun', 27, 'healthy burger');
    
select * from customers;
    
CREATE TABLE drinks (
  name VARCHAR(50),
  price INTEGER,
  ml INTEGER
);
    
INSERT INTO drinks (
	name,
    price,
    ml
) values('Cola', 1500, 500);

INSERT INTO drinks (
	name,
    price,
    ml
    ) values('Iced tea', 2000, 600);
    
select * from drinks;

CREATE TABLE sauces (
	name VARCHAR(50),
    spicylevel INTEGER
);

insert into sauces (
	name,
    spicylevel
) values('chili', 3), ('habanero', 5), ('sweet_chili', 2);

select * from sauces;