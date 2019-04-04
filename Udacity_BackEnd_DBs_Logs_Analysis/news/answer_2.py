#!/usr/bin/env python2.7
#
# 2. Who are the most popular article authors of all time? That is, when you
# sum up all of the articles each author has written, which authors get the
# most page views? Present this as a sorted list with the most popular author
# at the top.
# Example:
# - Ursula La Multa -- 2304 views
# - Rudolf von Treppenwitz -- 1985 views
# - Markoff Chaney -- 1723 views
# - Anonymous Contributor -- 1023 views
#

import psycopg2

DBNAME = 'news'

try:
    # Connect to the database
    db = psycopg2.connect(database=DBNAME)
    # Open a cursor
    cur = db.cursor()
    # Execute sql statement
    cur.execute('SELECT * from Question_2')
    # Fetch all data
    rows = cur.fetchall()
    print('\nQuestion #2: Who are the most popular '
          'article authors of all time?\n')
    # Loop through all rows
    for row in rows:
        print('{0} -- {1} views'.format(row[0], row[1]))
    print('\n')
    # Close connection to the database
    db.close()
except Exception as e:
    print('Unable to connect!\n{0}').format(e)
