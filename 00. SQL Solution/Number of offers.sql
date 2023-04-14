SELECT 
    case
        when Job_Offers is Null then 0 else Job_Offers
        end as Job_Offers
from Students as s 
left join 
    (SELECT Id, DATE, Salary, count(*) as Job_Offers from Jobs
    where month(date) = 11 group by Id) as j
on s.Id=j.Id