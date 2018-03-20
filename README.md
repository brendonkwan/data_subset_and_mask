# Data subsetting

Uses MySQL, Bash and Python to create a new database, named `subset`,
that contains a subset of the fictitious employee data from the `employees`
database.

Click [here](https://dev.mysql.com/doc/employee/en/sakila-structure.html)
for an entity-relationship diagram of the `employees` database.

## Where the data comes from

The fictitious data was taken from the GitHub repository named
[`datacharmer/test_db`](https://github.com/datacharmer/test_db), which was
distributed under the
[Creative Commons Attribution-Share Alike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/).

The employee data consists of about 300,000 employee records with 2.8 million
salary entries.

## Prerequisites

1. Install MySQL.
1. Install Python 3.
1. Install the Python package named 'MySQL Connector/Python'.

        $ pip install mysql-connector-python

1. Create a MySQL configuration file at `~/.my.cnf` containing the following
text:

        [client]
        user=<USERNAME>
        password=<PASSWORD>

    Where `<USERNAME>` and `<PASSWORD>` are replaced with your MySQL database
    username and password, respectively.


## Installation:

1. Download the repository.
2. Change directory to the repository.
3. Create and test the `employees` database. If the database exists, it will be
   recreated.

        $ cd test_db
        $ mysql < employees.sql
        $ mysql --table < test_employees_md5.sql

4. Create and test an empty database named `subset` with the same structure
   as the `employees` database.

        $ cd ..
        $ ./create_empty_subset.sh
        $ mysql --table < test_subset_empty.sql

5. Copy the given number of employees, `N`, from the `employees` database
   to the `subset` databse.

        $ ./subsetter.py N

## LICENSE
This work is licensed under the 
Creative Commons Attribution-Share Alike 3.0 Unported License. 
To view a copy of this license, visit 
http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to 
Creative Commons, 171 Second Street, Suite 300, San Francisco, 
California, 94105, USA.


