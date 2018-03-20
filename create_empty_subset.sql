#!/usr/bin/env bash

# Drops and creates the database named 'subset', which has the same
# structure as the 'employees' database but is empty.
#
# Author: Brendon Kwan

mysql --execute='DROP DATABASE IF EXISTS subset'

mysqladmin create subset

mysqldump employees --no-data | mysql subset
