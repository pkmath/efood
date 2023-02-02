select city,orders_sum/users_freq as top10perc from(

select c.city,b.users_freq,sum(user_freq) as orders_sum from(


select city, user_id,user_freq, rank from (
select city,user_id, count(user_id) as user_freq, row_number()
over (partition by city
        order by count(user_id) desc) as rank
        from `efood2023-376511.main_assessment.orders`
        
 group by city, user_id
) 
 where rank <=10
) c

JOIN 

(select city, count(user_id) as users_freq
from
        `efood2023-376511.main_assessment.orders`
        group by city
) b

on c.city=b.city

group by c.city, b.users_freq
)
group by city, top10perc
