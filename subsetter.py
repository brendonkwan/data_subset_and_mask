#!/usr/bin/env python3

# Copies the details of the given number of employees from the 'employees'
# database to the 'subset' database.
# 
# Author: Brendon Kwan

import argparse
import getpass
import os
import mysql.connector

class Subsetter:
    def __init__(self, conn, verbose):
        self.conn = conn
        self.verbose = verbose

    def create_emp_no_list(self, emp_subset_size):
        emp_no_list = []
        cursor = self.conn.cursor()
        query = ("SELECT emp_no "
            "FROM employees.employees "
            "ORDER BY emp_no "
            "LIMIT {}").format(emp_subset_size)
        cursor.execute(query)
        for (emp_no,) in cursor.fetchall():
            emp_no_list.append(emp_no)
        cursor.close()
        return emp_no_list

    def copy_emp_records(self, table, emp_no):
        """Copies from the given table of the 'employees' database to the
        corresponding table of the 'subset' database all records that
        concern the given employee. No changes are made if the destination table
        already has a record with the given employee number.
        """
        cursor = self.conn.cursor()
        query = ("INSERT IGNORE INTO subset.{} "
            "SELECT * "
            "FROM employees.{} "
            "WHERE emp_no = {}").format(table, table, emp_no)
        if self.verbose:
            print("About to execute: {}".format(query))
        cursor.execute(query)
        self.conn.commit()
        cursor.close()

    def copy_dept_records(self, table, dept_no):
        """Copies from the given table of the 'employees' database to the
        corresponding table of the 'subset' database all records that
        concern the given department. No changes are made if the destination
        table already has a record with the given department number.
        """
        cursor = self.conn.cursor()
        query = ("INSERT IGNORE INTO subset.{} "
            "SELECT * "
            "FROM employees.{} "
            "WHERE dept_no = '{}'").format(table, table, dept_no)
        if self.verbose:
            print("About to execute: {}".format(query))
        cursor.execute(query)
        cursor.close()

    def find_related_dept_no_list(self, emp_no_list):
        dept_no_list = []
        emp_no_string = ', '.join(map(str, emp_no_list))
        cursor = self.conn.cursor()

        # Find the departments that the given employees manage or are part of.
        query = ("(SELECT dept_no "
            "FROM employees.dept_manager "
            "WHERE emp_no IN ({})) "
            "UNION "
            "(SELECT dept_no "
            "FROM employees.dept_emp "
            "WHERE emp_no IN ({}))").format(emp_no_string, emp_no_string)
        cursor.execute(query)
        for (dept_no,) in cursor.fetchall():
            dept_no_list.append(dept_no)
        cursor.close()
        return dept_no_list
        
    def copy_subset(self, emp_subset_size):
        """Copies the given number of employees from the "employees"
        database to the "subset" database. Returns a list containing the
        "emp_no" value of every employee that was copied.
        """
        emp_no_list = self.create_emp_no_list(emp_subset_size)
        for emp_no in emp_no_list:
            self.copy_emp_records('employees', emp_no)
            self.copy_emp_records('salaries', emp_no)
            self.copy_emp_records('titles', emp_no)
        dept_no_list = self.find_related_dept_no_list(emp_no_list)
        for dept_no in dept_no_list:
            self.copy_dept_records('departments', dept_no)
        for emp_no in emp_no_list:
            self.copy_dept_records('dept_emp', emp_no)
            self.copy_dept_records('dept_manager', emp_no)
        self.conn.commit()
        return emp_no_list


def main():
    parser = argparse.ArgumentParser(
            description='Create a subset of the "employees" database')
    parser.add_argument('emp_subset_size', type=int,
            help='Number of employees to include in the subset')
    parser.add_argument('-v', '--verbose', action='store_true',
            help='Verbose mode')
    args = parser.parse_args()

    conn = mysql.connector.connect(
            option_files=os.path.expanduser('~/.my.cnf'))

    subsetter = Subsetter(conn, args.verbose)

    emp_no_list = subsetter.copy_subset(args.emp_subset_size)
    
    print('Copied these employees from the "employees" database ' +
            'to the "subset" database:')
    for emp_no in emp_no_list:
        print('emp_no {}'.format(emp_no))


if __name__ == '__main__':
    main()
