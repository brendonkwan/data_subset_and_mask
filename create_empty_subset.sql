#!/usr/bin/env bash

mysql --execute='DROP DATABASE IF EXISTS subset'

mysqladmin create subset

mysqldump employees --no-data | mysql subset
