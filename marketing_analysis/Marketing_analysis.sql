-- #segementing products based on their prices

SELECT *,
CASE
	WHEN p.price < (SELECT percentile_cont(0.25) WITHIN GROUP (ORDER BY price) FROM products) THEN 'Low'
	WHEN (SELECT percentile_cont(0.75) WITHIN GROUP (ORDER BY price) FROM products ) >p.price THEN 'Mid'
	ELSE 'High'
END AS PriceCategory
FROM products AS p;


-- #joining customers and geography tables to get the different data together

SELECT 
	customerid,
	customername,
	age,
	gender,
	city,
	email,
	country
FROM customers c 
JOIN geography g 
ON g.geographyid = c.geographyid;

-- #cleaning reviews

SELECT 
	cr.customerid ,
	cr.reviewdate ,
	replace(cr.reviewtext,'  ',' ') AS Review_Text,
	cr.rating,
	cr.productid ,
	cr.reviewid
FROM customer_reviews cr;

--#cleaning engagement data

SELECT 
	upper(replace(lower(ed.contenttype),'socialmedia','social media')) AS Content_Type,
	ed.engagementdate AS Engagement_Date,
	ed.likes AS Likes,
	left(ed.viewsclickscombined,position('-' IN ed.viewsclickscombined)-1) AS VIEWS,
	Right(ed.viewsclickscombined,LENGTH(ed.viewsclickscombined) - position('-' IN ed.viewsclickscombined)) AS Clicks,
	p.productname AS Product_Name,
	ed.campaignid AS Campaign_Id
FROM engagement_data ed 
LEFT JOIN products as p
ON p.productid = ed.productid;


--# Filtering Duplicates in customer_journey Table

WITH duplicates AS (
	SELECT 
	journeyid ,
	customerid,
	productid,
	visitdate,
	stage,
	ACTION,
	coalesce(duration,avg(duration) OVER(PARTITION BY visitdate)) AS Duration,
	row_number() OVER (PARTITION BY customerid , productid,visitdate,stage,ACTION ORDER BY journeyid) AS Row_num
	FROM customer_journey
)

SELECT 
	journeyid ,
	customerid,
	productid,
	visitdate,
	stage,
	ACTION,
	duration
FROM duplicates
WHERE row_num =1;