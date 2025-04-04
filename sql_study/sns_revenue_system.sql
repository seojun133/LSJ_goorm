create database expMission;
use expMission;

create table users (
	id int auto_increment primary key,
    username varchar(50),
    age integer,
    join_date date
);

create table posts (
	id int auto_increment primary key,
    user_id int not null,
    foreign key (user_id) references users(id),
    content text,
    view_count integer,
    ad_revenue decimal(10, 2),
    is_public boolean,
    created_at datetime
);

insert into users (username, age, join_date)
values
('alice', 25, '2024-01-10'),
('bob', 32, '2024-01-15'),
('charlie', 41, '2024-02-01');

insert into posts ( user_id, content,view_count, ad_revenue, is_public, created_at)
values
(1, 'Hello world!', 120, 15.50, TRUE, '2025-03-20 09:00'),
(2, 'Good morning', 300, 42.75, TRUE, '2025-03-20 10:30'),
(3, 'SQL is fun!', 80, 0.00, FALSE, '2025-03-21 14:00'),
(1, '광고 테스트', 50, 5.00, TRUE, '2025-03-22 11:00');

select count(content), sum(view_count), sum(ad_revenue) from posts;

select round(avg(ad_revenue),2) as AVG_AR from posts where ad_revenue > 0;

select user_id, sum(ad_revenue) from posts group by user_id;

select id, ad_revenue from posts 
where ad_revenue = (select max(ad_revenue) from posts);

select id, view_count, ad_revenue, round((ad_revenue/view_count),4) as RV_PER_VIEW
from posts
where ad_revenue > 0 order by ad_revenue / view_count desc limit 1;

select round(avg(view_count) ,2) as AVG_PVC, round(avg(ad_revenue),2) as AVG_PAR
from posts where is_public = TRUE;