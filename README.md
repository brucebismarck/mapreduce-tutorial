# mapreduce-tutorial
Homework and projects from INLS626 Bigdata and NoSQL class

First forlder is 1_homework. I used map reduce to do Hive and Pig things.

Data has about 1,000,000 rows, three useable features
Feature 1 is siteId, Feature 2 is backgroundId, 1 and 2 combined is unique patient. Feature 5 is medication taken by patient
Q2_mapper.py and Q2_reducer.py are used to complete 
select F1, F2 from mytable group by F1, F2
Q3_mapper.py and Q3_reducer.py are used to complete
select F1, F2 from mytable where F5 <> 'somestring' group by F1, F2
Q5_mapper.py and Q5_reducer.py
find the medication with highest number of unique patients
Q6_mapper.py and Q6_mapper.py 
find patients taken both med1 and med2.
