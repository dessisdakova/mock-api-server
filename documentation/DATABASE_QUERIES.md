### **Retrieve top 10 most expensive products:**
QUERY:
```sql
    SELECT product_name, unit_price
    FROM products
    ORDER BY unit_price DESC
    LIMIT 10;
```
RESULT:
product_name| unit_price
:-----------|----------:
 Côte de Blaye           |      263.5
 Thüringer Rostbratwurst |     123.79
 Mishi Kobe Niku         |         97
 Sir Rodney's Marmalade  |         81
 Carnarvon Tigers        |       62.5
 Raclette Courdavault    |         55
 Manjimup Dried Apples   |         53
 Tarte au sucre          |       49.3
 Ipoh Coffee             |         46
 Rössle Sauerkraut       |       45.6


### **Sum of freight charges by employee:**
QUERY / UPDATED:
```sql
    SELECT employee_id, SUM(freight) 
    FROM orders 
    GROUP BY employee_id 
    ORDER BY employee_id;
```
RESULT:
 employee_id |    sum
------------:|----------:
 1 | 8836.639
 2 | 8696.408
 3 | 10884.737
 4 | 11346.138
 5 | 3918.7104
 6 | 3780.4695
 7 | 6665.4404
 8 | 7487.8804
 9 | 3326.2598


### **City-wise average, maximum, and minimum age of employees in London:**
QUERY / UPDATED:
```sql
    SELECT city, AVG(EXTRACT(year from AGE(CURRENT_TIMESTAMP, birth_date))), 
    MAX(EXTRACT(year from AGE(CURRENT_TIMESTAMP, birth_date))), 
    MIN(EXTRACT(year from AGE(CURRENT_TIMESTAMP, birth_date))) 
    FROM employees 
    WHERE city = 'London' 
    GROUP BY city;
```
RESULT:
  city  |         avg         | max | min
:------:|:-------------------:|:---:|:---:
 London | 63.0000000000000000 | 69 |  58


### **City-wise average age of employees above 60:** <br>
QUERY / UPDATED:
```sql
    SELECT city, AVG(EXTRACT(year FROM AGE(CURRENT_TIMESTAMP, birth_date))) AS avg_age
    FROM employees
    GROUP BY city
    HAVING AVG(EXTRACT(year FROM AGE(CURRENT_TIMESTAMP, birth_date))) > 60;
```
RESULT:
   city   |       avg_age
----------|---------------------
 Redmond  | 87.0000000000000000
 London   | 63.0000000000000000
 Tacoma   | 72.0000000000000000
 Kirkland | 61.0000000000000000
 Seattle  | 71.0000000000000000


### **Retrieve top 3 oldest employees:**
QUERY:
```sql
    SELECT first_name, last_name, EXTRACT(year from AGE(CURRENT_TIMESTAMP, birth_date)) AS age 
    FROM employees 
    ORDER BY age 
    DESC LIMIT 3;
```
RESULT:
 first_name | last_name | age
------------|-----------|----
 Margaret   | Peacock   |  87
 Nancy      | Davolio   |  76
 Andrew     | Fuller    |  72