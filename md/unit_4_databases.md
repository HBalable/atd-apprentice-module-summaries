---
title: "Unit 4: DATABASES"
date: "March 2018"
author: "Hasan Balable"
geometry: margin=2.54cm
---

# DATABASES

### Structured Data
Structured data is data that is organised in a context with tags. A database is a collection of structured data. 

### Unstructured Data
Unstructured data is data with no context. This can be in the form of texts, images or any other forms of information.

Ensuring Quality of Data.
-------------

### Validation
Validation is very important when inputting data into a database. It is the act of ensuring that data of the correct type and format is entered so that it can be sorted and understood, fitting in the correct context. For example, a list of dates of birth could be stored in a variety of ways but having one consistent format makes it much easier to order and query.

|Validated |Not Validated|
|:--------:|:-----------:|
|```25.09.1998```|```25/009/98```    |
|```01.02.1965```|```2/1/65```       |
|```30.01.1989```|```06.1.89```      |
|```05.05.2005```|```5, 5,05```       |



### Verification
Verification is another important practice that is used during data entry. It is to ensure that the correct data is being entered. Obviously, this could be slightly more difficult to check as the client that is being used to enter the data often isn’t clever enough to know whether the data is correct, so verification is mostly used to correct human error. One method that is used is double entry: asking the user to enter the data twice.

A relational database consists of a series of tables of structured data. These tables are referenced using keys. The primary key is a unique id of a record in the current table, and the secondary key is that of a referenced table.

Relational Databases
-----------------
Relational databases use multiple tables, and rows (also known as records) in a table refer to primary keys (unique-per-row values; normally a integer or hash) from other tables, enabling for complexity and efficiency that might not be possible in a traditional 2 dimensional database.

Different tables are usually created for different "object types". For example, in the context of VFX, there might be a table for shots, a table for assets and a table for asset versions. The assets table might include a number of different items that are being worked on for a specific shot. These assets would have a reference to the shot that they belong to's primary key from the shot table.

#### Querying a Database

At DNEG I have written a number of tools which use queries read information from our database and our shotgun database. The tools I have used to interact with both of these are APIs, which add a layer of abstraction and make querying much more user friendly, and also much less dangerous. Deleting and editing data is much more protected than it would be interacting directly with the MySQL and PostgreSQL servers.


This shotgun query returns a list of dictionaries containing the ```name``` attribute of all projects in the shotgun database whose ```sg_status``` attribute is "active".

```
from shotgun.common import conn
filters = [["sg_status","is","Active"]]
active_shows = conn.shn.find("Project", filters, fields = ["name", "sg_status"])
[
    {
        'sg_status': 'Active',
        'type': 'Project',
        'id': 4,
        'name': 'DNEG_SHOW1'
    },
    {
        'sg_status': 'Active',
        'type': 'Project',
        'id': 67,
        'name': 'DNEG_SHOW2'
    },
    {
        'sg_status': 'Active',
        'type': 'Project',
        'id': 80,
        'name': 'DNEG_SHOW3'
    },
    # etc...
]
```
