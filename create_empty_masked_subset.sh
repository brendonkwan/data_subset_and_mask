#!/usr/bin/env bash

mysql --execute='DROP DATABASE IF EXISTS masked_subset'

mysqladmin create masked_subset

mysqldump employees --no-data | mysql masked_subset
