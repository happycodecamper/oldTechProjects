#!/usr/bin/env python2.7
#
# 3. On which days did more than 1% of requests lead to errors? The log table
# includes a column status that indicates the HTTP status code that the news
# site sent to the user's browser. (Refer to this lesson for more information
# about the idea of HTTP status codes.)
# Example:
# - July 29, 2016 --> 2.5% errors
#

import psycopg2

DBNAME = 'news'

try:
    # Connect to the database
    db = psycopg2.connect(database=DBNAME)
    # Open a cursor
    cur = db.cursor()
    # Execute sql statement
    cur.execute('SELECT * from Question_3')
    # Fetch all data
    rows = cur.fetchall()
    print('\nQuestion #3: On which days did more than'
          ' 1% of requests lead to errors?\n')
    # Loop through all rows
    for row in rows:
        print('{0} -- {1}% Errors'.format(row[0], row[1]))
    print('\n')
    # Close connection to the database
    db.close()
except Exception as e:
    print('Unable to connect!\n{0}').format(e)
