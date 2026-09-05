--1. Retrieve all successful bookings:
-- SELECT bj.customer_id,bj.booking_id ,bj.date,bj.ride_distance,bj.booking_value ,bj.Booking_Status  FROM bookings_july AS bj WHERE Booking_Status ='Success'

--2. Find the average ride distance for each vehicle type:
--SELECT bj.vehicle_type ,Round(avg(bj.ride_distance),2)FROM bookings_july bj  GROUP BY bj.vehicle_type 

--3. Get the total number of cancelled rides by customers:
--SELECT count(booking_status) AS Total_Canceled FROM bookings_july bj WHERE bj.booking_status = 'Canceled by Customer'

--4. List the top 5 customers who booked the highest number of rides:
--SELECT customer_id,count(booking_status) AS Total_Successful_rides FROM bookings_july bj WHERE bj.booking_status LIKE '%Success%' GROUP BY bj.customer_id 
--ORDER BY total_successful_rides DESC LIMIT 5

--5. Get the number of rides cancelled by drivers due to personal and car-related issues:
--SELECT count(booking_status),max(bj.canceled_rides_by_driver) FROM  bookings_july bj  WHERE booking_status LIKE '%by Driver%' AND bj.canceled_rides_by_driver LIKE '%Personal & Car related issue%'

--6. Find the maximum and minimum driver ratings for Prime Sedan bookings:
--SELECT max(
--CASE 
--	WHEN driver_ratings ='null' THEN  NULL	
--	ELSE bj.driver_ratings 
--END
--) AS  max_driver_rating ,
--min(bj.driver_ratings) AS min_driver_rating 
--FROM bookings_july bj WHERE bj.vehicle_type = 'Prime Sedan' 

--7. Retrieve all rides where payment was made using UPI:
--SELECT bj.booking_id , bj.payment_method FROM bookings_july bj WHERE bj.payment_method = 'UPI'

--8. Find the average customer rating per vehicle type:
--SELECT vehicle_type ,Round(AVG(
--	CASE 
--		WHEN customer_rating ='null' THEN NULL
--		ELSE bj.customer_rating :: numeric
--	END
--),2) AS Avg_Customer_Rating 
--FROM bookings_july bj GROUP BY bj.vehicle_type 
--ORDER BY avg_customer_rating DESC	

--9. Calculate the total booking value of rides completed successfully:
--SELECT sum(bj.booking_value) AS total_value_successful_rides FROM bookings_july bj WHERE bj.booking_status LIKE '%Success%'

--10. List all incomplete rides along with the reason:
--SELECT * FROM bookings_july bj WHERE bj.booking_status NOT LIKE '%Success%'


--UPDATE bookings_july 
--SET customer_rating = NULL
--WHERE customer_rating = 0::TEXT ;










