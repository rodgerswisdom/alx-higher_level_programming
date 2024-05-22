# 0x0D. SQL - Introduction

## Table of Contents
- [Introduction](#introduction)
- [Concepts](#concepts)
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [0. List databases](#0-list-databases)
  - [1. Create a database](#1-create-a-database)
  - [2. Delete a database](#2-delete-a-database)
  - [3. List tables](#3-list-tables)
  - [4. First table](#4-first-table)
  - [5. Full description](#5-full-description)
  - [6. List all in table](#6-list-all-in-table)
  - [7. First add](#7-first-add)
  - [8. Count 89](#8-count-89)
  - [9. Full creation](#9-full-creation)
  - [10. List by best](#10-list-by-best)
  - [11. Select the best](#11-select-the-best)
  - [12. Cheating is bad](#12-cheating-is-bad)
  - [13. Score too low](#13-score-too-low)
  - [14. Average](#14-average)
  - [15. Number by score](#15-number-by-score)
  - [16. Say my name](#16-say-my-name)

## Introduction
This project is part of the SE Foundations curriculum, focusing on the basics of SQL using MySQL. It covers the essential concepts and operations needed to manage databases, create and modify tables, and execute queries.

## Concepts
For this project, we expect you to look at these concepts:
- Databases

## Resources
Read or watch:
- [What is Database & SQL?](#)
- [A Basic MySQL Tutorial](#)
- [Basic SQL statements: DDL and DML](#)
- [Basic queries: SQL and RA](#)
- [SQL technique: functions](#)
- [SQL technique: subqueries](#)
- [What makes the big difference between a backtick and an apostrophe?](#)
- [MySQL Cheat Sheet](#)
- [MySQL 8.0 SQL Statement Syntax](#)
- [Installing MySQL in Ubuntu 20.04](#)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE or DELETE data
- What are subqueries
- How to use MySQL functions

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

### More Info
#### Comments for your SQL file:
```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

#### Install MySQL 8.0 on Ubuntu 20.04 LTS
```sh
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

#### Connect to your MySQL server:
```sh
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
mysql> quit
Bye
```

#### Use “container-on-demand” to run MySQL
In the container, credentials are `root/root`
```sh
$ service mysql start
 * Starting MySQL database server mysqld
$ cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema
sys
```

## Tasks
### 0. List databases
- **File:** `0-list_databases.sql`
- **Description:** Write a script that lists all databases of your MySQL server.
```sql
-- List all databases
SHOW DATABASES;
```

### 1. Create a database
- **File:** `1-create_database_if_missing.sql`
- **Description:** Write a script that creates the database `hbtn_0c_0` in your MySQL server. If the database already exists, the script should not fail.
```sql
-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
```

### 2. Delete a database
- **File:** `2-remove_database.sql`
- **Description:** Write a script that deletes the database `hbtn_0c_0` in your MySQL server. If the database doesn’t exist, the script should not fail.
```sql
-- Drop database if exists
DROP DATABASE IF EXISTS hbtn_0c_0;
```

### 3. List tables
- **File:** `3-list_tables.sql`
- **Description:** Write a script that lists all the tables of a database in your MySQL server. The database name will be passed as an argument.
```sql
-- List all tables in given database
SHOW TABLES;
```

### 4. First table
- **File:** `4-first_table.sql`
- **Description:** Write a script that creates a table called `first_table` in the current database in your MySQL server.
```sql
-- Create table first_table
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
```

### 5. Full description
- **File:** `5-full_table.sql`
- **Description:** Write a script that prints the full description of the table `first_table` from the database `hbtn_0c_0`.
```sql
-- Full description of first_table
SHOW CREATE TABLE first_table;
```

### 6. List all in table
- **File:** `6-list_values.sql`
- **Description:** Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0`.
```sql
-- List all rows from first_table
SELECT * FROM first_table;
```

### 7. First add
- **File:** `7-insert_value.sql`
- **Description:** Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`).
```sql
-- Insert new row into first_table
INSERT INTO first_table (id, name) VALUES (89, 'Best School');
```

### 8. Count 89
- **File:** `8-count_89.sql`
- **Description:** Write a script that displays the number of records with `id = 89` in the table `first_table`.
```sql
-- Count rows with id = 89
SELECT COUNT(*) FROM first_table WHERE id = 89;
```

### 9. Full creation
- **File:** `9-full_creation.sql`
- **Description:** Write a script that creates a table `second_table` in the database `hbtn_0c_0` and add multiple rows.
```sql
-- Create table second_table and insert rows
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
```

### 10. List by best
- **File:** `10-top_score.sql`
- **Description:** Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0`, ordered by score (top first).
```sql
-- List all records from second_table ordered by score descending
SELECT score, name FROM second_table ORDER BY score DESC;
```

### 11. Select the best
- **File:** `11-best_score.sql`
- **Description:** Write a script that lists all records with a score >= 10 in the table `second_table`.
```sql
-- List records with score >= 10 from second_table
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
```

### 12. Cheating is bad
- **File:** `12-no_cheating.sql`
- **Description:** Write a script that updates the score of Bob to 10 in the table `second_table`.
```sql
-- Update score of Bob to 10
UPDATE second_table SET score = 10 WHERE

 name = 'Bob';
```

### 13. Score too low
- **File:** `13-change_class.sql`
- **Description:** Write a script that removes all records with a score <= 5 in the table `second_table`.
```sql
-- Delete records with score <= 5 from second_table
DELETE FROM second_table WHERE score <= 5;
```

### 14. Average
- **File:** `14-average.sql`
- **Description:** Write a script that computes the average score of all records in the table `second_table`.
```sql
-- Compute average score from second_table
SELECT AVG(score) FROM second_table;
```

### 15. Number by score
- **File:** `15-groups.sql`
- **Description:** Write a script that lists the number of records with the same score in the table `second_table`.
```sql
-- List number of records with the same score from second_table
SELECT score, COUNT(*) FROM second_table GROUP BY score;
```

### 16. Say my name
- **File:** `16-no_link.sql`
- **Description:** Write a script that lists all records of the table `second_table` and uses the `name` field.
```sql
-- List all records from second_table using name field
SELECT name FROM second_table;
```
