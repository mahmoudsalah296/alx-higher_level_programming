#!/usr/bin/python3
"""script that lists all states with a name starting with N"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(
        user=username, passwd=passwd, db=db_name, host="localhost", port=3306
    )
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM states
        WHERE states.name LIKE "N%"
        ORDER BY states.id
    """
    )
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()
