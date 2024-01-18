#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, passwd, db_name, state = sys.argv[1:5]
    query = """
        SELECT cities.name FROM
        cities INNER JOIN states ON states.id=cities.state_id
        WHERE states.name LIKE BINARY %s
        ORDER BY cities.id
    """
    conn = MySQLdb.connect(
        user=username, passwd=passwd, db=db_name, host="localhost", port=3306
    )
    cursor = conn.cursor()
    cursor.execute(query, (state,))
    tmp = list(row[0] for row in cursor.fetchall())
    print(*tmp, sep=", ")

    cursor.close()
    conn.close()
