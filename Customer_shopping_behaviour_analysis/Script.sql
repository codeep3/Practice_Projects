--Q1. find out total purchase amount spent by each gender?

--SELECT gender,sum(purchase_amount) FROM customer GROUP BY  gender 


--Q2. which customer used discount still spent more than average purchase amount?

--SELECT customer_id,age,purchase_amount FROM customer WHERE discount_applied = 'Yes'
--AND purchase_amount > (select avg(purchase_amount) FROM customer )

--Q3. which are the top 5 products with highest average review rate?

--SELECT item_purchased,round(avg(review_rating::numeric),2) AS average_review_rating 
--FROM customer GROUP  BY	customer.item_purchased ORDER BY  avg(review_rating) DESC  LIMIT 5

--Q4. compare average purchase amount between standard and express shipping.

--SELECT shipping_type,round(avg(purchase_amount::numeric),2)
--FROM customer WHERE shipping_type IN ('Express','Standard') GROUP BY customer.shipping_type

--Q5. Do subscribed customers spend more? compare average spend between total subscribed v/s Non-subscribed customers.

--SELECT subscription_status,count(customer_id) AS total_customers ,round(avg(purchase_amount),2) AS average_amount_spent,
--round(sum(purchase_amount),2) AS total_amount_spend
--FROM customer GROUP BY subscription_status 

--Q6. which 5 products have the highest % of purhcases with discounts applied?

--SELECT sq.item_purchased,total_revenue,round(((purchase_amount/total_revenue)*100),2)AS percentage_of_total_revenue
--FROM (SELECT item_purchased,sum(purchase_amount) AS total_revenue  
--FROM customer 
--WHERE discount_applied = 'Yes'
--GROUP BY item_purchased 
--)AS sq ,customer AS c
--ORDER BY percentage_of_total_revenue DESC LIMIT 5 


--Q7. segment customer into New,Returning and loyal and count each segment

--WITH customer_segment AS(
--SELECT customer_id , 
--CASE  
--	WHEN previous_purchases = 1 THEN 'New'
--	WHEN	previous_purchases BETWEEN 2 AND 10 THEN 'Returning'
--	ELSE 'Loyal'
--	END  AS customer_status
--FROM customer)

--SELECT count(customer_id) AS number_of_customers ,customer_status  FROM customer_segment GROUP BY customer_status


--Q8. revenue contribution of each age group.

--SELECT sum(purchase_amount),age_group FROM customer GROUP BY age_group























