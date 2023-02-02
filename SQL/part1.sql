SELECT c.city, SUM(amount)/COUNT(c.city) as breakfast_basket,F.efood_basket, count(c.city)/COUNT(DISTINCT user_id) as breakfast_freq, 
F.efood_freq,D.breakfastuser3perc, E.efooduser3perc, count(c.city) as breakfast_orders

FROM  `efood2023-376511.main_assessment.orders` C

JOIN

(select a.city, A.city_freq/B.city_freq as breakfastuser3perc
from (select city,count(city) as city_freq from(

    SELECT city,user_id
FROM `efood2023-376511.main_assessment.orders`
WHERE cuisine = 'Breakfast' 
GROUP BY user_id, city
HAVING COUNT(user_id) > 3
    ) 

    group by city
    order by city_freq desc) A
    
    JOIN 

    (
select city,count(city) as city_freq from(

    SELECT city,user_id
FROM `efood2023-376511.main_assessment.orders`
WHERE cuisine = 'Breakfast' 
GROUP BY user_id, city
--HAVING COUNT(user_id) > 3
    ) 

    group by city
    order by city_freq desc
    ) B

    on A.city = B.city) D

    on C.city=D.city

JOIN 

(select a.city, A.city_freq/B.city_freq as efooduser3perc
from (select city,count(city) as city_freq from(

    SELECT city,user_id
FROM `efood2023-376511.main_assessment.orders`
--WHERE cuisine = 'Breakfast' 
GROUP BY user_id, city
HAVING COUNT(user_id) > 3
    ) 

    group by city
    order by city_freq desc) A
    
    JOIN 

    (
select city,count(city) as city_freq from(

    SELECT city,user_id
FROM `efood2023-376511.main_assessment.orders`
--WHERE cuisine = 'Breakfast' 
GROUP BY user_id, city
--HAVING COUNT(user_id) > 3
    ) 

    group by city
    order by city_freq desc
    ) B

    on A.city = B.city) E

    on c.city=e.city

JOIN

(
    SELECT city, SUM(amount)/COUNT(city) as efood_basket, count(city)/COUNT(DISTINCT user_id) as efood_freq, 

FROM `efood2023-376511.main_assessment.orders`
--WHERE cuisine = 'Breakfast'
group by city

) F

on c.city=f.city

WHERE cuisine = 'Breakfast'
group by c.city, D.breakfastuser3perc, E.efooduser3perc,F.efood_basket,F.efood_freq
order by breakfast_orders desc
limit 5

