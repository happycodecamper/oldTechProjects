#!/usr/bin/env python2.7
#
# 1. What are the most popular three articles of all time? Which articles have
# been accessed the most? Present this information as a sorted list with the
# most popular article at the top
# Example:
# -"Princess Shellfish Marries Prince Handsome" -- 1201 views
# -"Baltimore Ravens Defeat Rhode Island Shoggoths" -- 915 views
# -"Political Scandal Ends In Political Scandal" -- 553 views
#

import psycopg2

DBNAME = 'news'

try:
    # Connect to the database
    db = psycopg2.connect(database=DBNAME)
    # Open a cursor
    cur = db.cursor()
    # Execute sql statement
    cur.execute('SELECT * from Question_1')
    # Fetch all data
    rows = cur.fetchall()
    print('\nQuestion #1: What are the most popular three articles of all '
          'time?\n')
    # Loop through all rows
    for title, views in rows:
        print('"{0}" -- {1} Views'.format(title, views))
    print('\n')
    # Close connection to the database
    db.close()
except Exception as e:
    print('Unable to connect!\n{0}').format(e)
