#!/usr/bin/python3
"""script that lists all states with a name matches user input"""

import MySQLdb
import sys


if __name__ == "__main__":
    username, passwd, db_name = sys.argv[1:4]

    query = """SELECT * FROM states
        WHERE name LIKE BINARY %s
        ORDER BY states.id
    """
    conn = MySQLdb.connect(
        user=username, passwd=passwd, db=db_name, host="localhost", port=3306
    )
    cursor = conn.cursor()
    cursor.execute(query, (sys.argv[4],))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()
