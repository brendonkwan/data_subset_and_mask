#!/usr/bin/env python3

import argparse
import getpass
import mysql.connector

def main():
    username = input('Enter database username: ')
    password = getpass.getpass('Enter database password: ')
    conn = mysql.connector.connect(user=username, password=password)

if __name__ == '__main__':
    main()
