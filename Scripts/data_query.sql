SELECT count(*) FROM raw_transactions;
select * from raw_transactions
WHERE unitprice <0 OR unitprice;

Select 
SUM(quantity * unitprice) as Total_Price
from raw_transactions

SELECT count(*) FROM raw_transactions;

--Audit 1: Checking unit prices which are less than and equal to 0
select * from raw_transactions
WHERE unitprice<=0 ;

--Audit 2: Checking cutomer id's which are null
SELECT * FROM raw_transactions
WHERE customerid IS NULL;

--Audit 3: Checking quantites which are less than or equal to 0
select * from raw_transactions
WHERE quantity<=0 ;


--Audit 4: Checking stock codes which are not actually a stock instead it's irrelevant data.
SELECT 
    stockcode, 
    description, 
    COUNT(*) as frequency
FROM raw_transactions
WHERE length(stockcode) < 5 
   OR stockcode SIMILAR TO '[A-Z]+' -- Finds codes that are ONLY letters
GROUP BY stockcode, description
ORDER BY frequency DESC;

-- Creating a Clean View for the Business
CREATE OR REPLACE VIEW certified_sales AS
SELECT * FROM raw_transactions
WHERE customerid IS NOT NULL       -- Audit 2 Fix
  AND unitprice > 0                -- Audit 1 Fix
  AND quantity > 0                 -- Audit 3 Fix
  AND length(stockcode) >= 5       -- Audit 4 Fix
  AND stockcode NOT SIMILAR TO '[A-Z]+'; -- Audit 4 Fix


-- Comparing previous and after numbers.
SELECT 
    'Raw Data' as status, COUNT(*) as row_count FROM raw_transactions
UNION ALL
SELECT 
    'Certified Data' as status, COUNT(*) as row_count FROM certified_sales;