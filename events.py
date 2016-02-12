#!/usr/bin/python
#
# Author: Jeremy Ford
# Date: 2/12/2016
#
# Quick script to display Events in event table in the OpenNMS database.
#
# Requirements:
#       - pip install tabulate
#       - pip install psycopg2 or yum install python-psycopg2
import psycopg2
import psycopg2.extras
from tabulate import tabulate

DB_HOSTNAME = "localhost"
DB_USERNAME = "opennms"
DB_PASSWORD = "opennms"
DB_NAME = "opennms"

dsn = ("dbname=" + DB_NAME + " user=" + DB_USERNAME + " password=" + DB_PASSWORD + " host=" + DB_HOSTNAME)
try:
    db=psycopg2.connect(dsn)
except:
    print "ERROR Connecting to the database. Check your parameters."

cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
        cur.execute("""SELECT eventUEI, COUNT(eventID) AS tally FROM events GROUP BY eventUEI ORDER BY tally DESC LIMIT 20;""")
except:
    print "ERROR running SELECT query"

count = 0
rows = cur.fetchall()

for row in rows:
        count = count + row[1]

rows.append(["Total Number of Events" , count])
print tabulate(rows, headers=["Event ID", "Number of Events"], tablefmt="fancy_grid")

cur.close()
db.close()
