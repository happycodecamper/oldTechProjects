# Logs Analysis Project

Create a reporting tool that prints out reports (in plain text) based on the data in a database to discover what kind of articles the site's readers like.

## Getting Started

The program will run from the command line. It won't take any input from the user. Instead, it will connect to that database, using SQL queries to analyze the log data, and printing out the answers to some questions.

### Prerequisites and Installing

#### Software and data

Install: 
* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/)
* [Python](https://www.python.org/)
* [PostgreSQL](https://www.postgresql.org/) 
* [psycopg2](https://pypi.python.org/pypi/psycopg2)


A folder called *news* was create to save the files of the project.

Change directory with the cd command to the directory where Vagrant is, then run :
```
vagrant up
```

To log into the VM in that same directory, run:
```
vagrant ssh
```

In this shell:
```
cd /vagrant
```
and run:
```
ls
```
Unzip the file newsdata.zip and run the following command: 
```
psql -d news -f newsdata.sql
```

The reporting tool is a Python program using the **psycopg2** module to connect to the database.

## Assignment - Question #1

*What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.*

### Test:
Inside the directory **/vagrant**, run console:

```
psql -d news
```

Run the following query named **answer_1.sql**:
```sql
CREATE view Question_1 AS
SELECT articles.title AS "Most Popular Articles", count(*) AS "Views"
FROM log JOIN articles
ON '/article/' || articles.slug = log.path
GROUP BY articles.title
ORDER BY count(*) DESC LIMIT 3;
```
Leave the psql mode by entering **\q** and change directory with command **cd /news** (name of my directory):

Run:
```
python answer_1.py
```

Snapshot:
```
Question #1: What are the most popular three articles of all time?

"Candidate is jerk, alleges rival" -- 338647 Views
"Bears love berries, alleges bear" -- 253801 Views
"Bad things gone, say good people" -- 170098 Views
```

## Assignment - Question #2

*Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.*

### Test:

Inside the directory **/vagrant**, run console:
```
psql -d news
```

Run the following query named **answer_2.sql**:
```sql
CREATE view Question_2 AS
SELECT  authors.name AS "Articles Authors Name", count(*) AS "Views"
FROM log JOIN articles
ON '/article/' || articles.slug = log.path
JOIN authors
ON authors.id = articles.author
GROUP BY authors.name
ORDER BY count(*) DESC;
```
Leave the psql mode by entering **\q** and change directory with command **cd /news** (name of my directory):

Run:
```
python answer_2.py
```

Snapshot:
```
Question #2: Who are the most popular article authors of all time?

Ursula La Multa -- 507594 views
Rudolf von Treppenwitz -- 423457 views
Anonymous Contributor -- 170098 views
Markoff Chaney -- 84557 views
```

## Assignment - Question #3

*On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)*

### Test:

Inside the directory **/vagrant**, run console:

```
psql -d news
```

Run the following query named **answer_3.sql**:
```sql 
CREATE view Question_3 AS
SELECT to_char(A.time, 'FMMonth DD, YYYY') AS "DATE",
round((A.count/(CAST(A.count AS DECIMAL) + CAST(B.count AS DECIMAL))*100), 1) AS "Errors"
FROM
(SELECT A.time::DATE, count(*)
FROM log AS A
WHERE A.status != '200 OK' 
GROUP BY A.time::DATE
ORDER BY count(*) DESC) AS A
join
(SELECT B.time::DATE, count(*)
FROM log AS B
WHERE B.status = '200 OK' 
GROUP BY B.time::DATE
ORDER BY count(*) DESC) AS B
ON A.time = B.time
WHERE round((A.count/(CAST(A.count AS DECIMAL) + CAST(B.count AS DECIMAL))*100), 1) > 1
ORDER BY A.count DESC;
```
Leave the psql mode by entering **\q** and change directory with command **cd /news** (name of my directory):

Run:
```
python answer_3.py
```

Snapshot:
```
Question #3: On which days did more than 1% of requests lead to errors?

JUL17, 2016 -- 2.3% Errors
```

## Author

* **Maria Brito** - [View my page on GitHub](https://happycodecamper.github.io/)

