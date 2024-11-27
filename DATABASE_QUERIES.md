### **Retrieve top 10 most expensive products:**
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
 employee_id |    sum
------------:|----------:
 8 | 7487.8804
 7 | 6665.4404
 9 | 3326.2598
 1 |  8836.639
 5 | 3918.7104
 2 |  8696.408
 4 | 11346.138
 6 | 3780.4695
 3 | 10884.737


### **City-wise average, maximum, and minimum age of employees in London:**
  city  |         avg         | max | min
:------:|:-------------------:|:---:|:---:
 London | 63.0000000000000000 | 69 |  58


### **City-wise average age of employees above 60:** <br>
UPDATED QUERY:
```sql
    SSELECT city, AVG(EXTRACT(year FROM AGE(CURRENT_TIMESTAMP, birth_date))) AS avg_age
    FROM employees
    GROUP BY city
    HAVING AVG(EXTRACT(year FROM AGE(CURRENT_TIMESTAMP, birth_date))) > 60;
```
   city   |       avg_age
----------|---------------------
 Redmond  | 87.0000000000000000
 London   | 63.0000000000000000
 Tacoma   | 72.0000000000000000
 Kirkland | 61.0000000000000000
 Seattle  | 70.5000000000000000


### **Retrieve top 3 oldest employees:**
 first_name | last_name | age
------------|-----------|----
 Margaret   | Peacock   |  87
 Nancy      | Davolio   |  75
 Andrew     | Fuller    |  72