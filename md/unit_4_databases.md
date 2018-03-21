---
title: "Unit 4: DATABASES"
date: "March 2018"
author: "Hasan Balable"
geometry: margin=2.54cm
---

### Structured Data
Structured data is data that is organised in a context with tags. A database is an collection of structured data. 

### Unstructured Data
Unstructured data is data with no context. This can be in the form of texts, images or any other forms of information.

Ensuring Quality of Data.
-------------

### Validation
Validation is very important when inputting data into a database. It is the act of ensuring that data of the correct type and format is entered, so that it can be sorted and understood and fit in the correct context. For example, a list of dates of birth could be stored in a variety of ways, but having one consistent format makes it much easier to order and query.

|Validated|Not Validated|
|:-------:|:-----------:|
|<ul><li>25.09.1998</li> <li>01.02.1965</li> <li>30.01.1989</li> <li>05.05.2005</li></ul>|<ul><li>25/09/98</li> <li>2/1/65</li> <li>30.1.89</li> <li>5,5,05</li></ul>|	

<!-- Table data from above (for clarity)
 <ul>
    <li>25/09/98</li>
    <li>2/1/65</li>
    <li>30.1.89</li>
    <li>5,5,05</li>
</ul>
<ul>
    <li>25.09.1998</li>
    <li>01.02.1965</li>
    <li>30.01.1989</li>
    <li>05.05.2005</li>
</ul> 
-->

### Verification
Verification is another important practice that is used during data entry. It is to insure that the correct data is being entered. Obviously this could be slightly more difficult to check, as the client that is being used to enter the data often isn’t clever enough to know whether the data is correct, so verification is mostly used to correct human error. One method that is used is double entry: asking the user to enter the data twice.

A relational database consists of a series of tables of structured data. These tables are referenced using keys. The primary key is a unique id of a record in the current table, and the secondary key is that of a referenced table.

Relational Databases
-------------
advantages of a relational database (using links rather than storing lots of metadata in lots of files)

### Querying the Database
para (sql) finding sorting

# Database systems
para (MySQL, FireBird, PostgreSQL)

Databases in Visual Effects
-------------
para
### Database Management
Database queries not easy
most people only need specific tasks
abstraction
### Shotgun
mainly a production system, also dta
