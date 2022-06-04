import sqlite3

# ----------------------------------------------------------

# creates database file
conn = sqlite3.connect("user.db")
# cursor controls queries
cursor = conn.cursor()

# ----------------------------------------------------------

# create table
cursor.execute("""CREATE TABLE if not exists users(
        name text,
        phone integer
    )""")

# ----------------------------------------------------------


# insert one row
# cursor.execute("""INSERT INTO users VALUES(
#         'varun',
#         7001807604
#     )""")

# ----------------------------------------------------------

# insert many rows
# rows = [
#     ('varun', 123),
#     ('john', 2134213),
#     ('harry', 213),
# ]
# cursor.executemany("INSERT INTO users VALUES (?,?)", rows)

# ----------------------------------------------------------

# fetch data
# data = cursor.execute("SELECT * FROM users").fetchall()

# ----------------------------------------------------------

# update data
# cursor.execute("""UPDATE users SET name = 'toBeDeleted'
#                 WHERE rowid > 3
#     """)

# ----------------------------------------------------------

# delete data
# cursor.execute("""DELETE FROM users WHERE name = 'toBeDeleted'""")

# ----------------------------------------------------------

# order by
# data = cursor.execute(
#     "SELECT rowid,* FROM users ORDER BY rowid DESC").fetchall()

# ----------------------------------------------------------

# drop table
# cursor.execute("DROP TABLE users")

# ----------------------------------------------------------


# fetch data with primary key (rowid)
data = cursor.execute("SELECT rowid,* FROM users").fetchall()

print(data)


conn.commit()
conn.close()
