# Data subsetting and masking

An example of data subsetting and data masking. Uses MySQL, Bash and Python
to read a subset of the fictitious employee data from the 'employees' database,
mask the data, and write the masked data to the 'masked_employee_subset'
database.

## Where the data comes from

The fictitious employee data was taken from the GitHub repository named
[datacharmer/test_db](https://github.com/datacharmer/test_db), which was
distributed under the
[Creative Commons Attribution-Share Alike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/).

The employee data consists of about 300,000 employee records with 2.8 million
salary entries.

## Installation:

1. Download the repository.
2. Change directory to the repository.
3. Create the 'employees' database. If the database exists, it will be
   recreated.

    $ mysql < employees.sql

4. Create an empty database named 'masked_subset' with the same structure
   as the 'employees' database.

    $ ./create_empty_masked_subset.sh

5. Test the databases.

    $ mysql --tables < test_employees_md5.sql
    $ mysql --tables < test_masked_subset_empty.sql

## LICENSE
This work is licensed under the 
Creative Commons Attribution-Share Alike 3.0 Unported License. 
To view a copy of this license, visit 
http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to 
Creative Commons, 171 Second Street, Suite 300, San Francisco, 
California, 94105, USA.


