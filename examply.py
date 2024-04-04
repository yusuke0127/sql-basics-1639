import sqlite3

# 1st version
# conn = sqlite3.connect('data/soccer.sqlite')
# c = conn.cursor()

# c.execute("SELECT * FROM Country")
# rows = c.fetchall()
# print(rows)
# rows[1][1]

# 2nd version using Row objects
conn = sqlite3.connect('data/soccer.sqlite')
conn.row_factory = sqlite3.Row
c = conn.cursor()

c.execute("""
          SELECT 
	        League.name AS league_name, 
	        Country.name AS country_name
        FROM League 
        JOIN Country ON Country.id = League.country_id
    """)
rows = c.fetchone()
print(rows)
first_row = rows[0]
print(first_row)

# Function to get the column names
print(first_row.keys())


print(first_row['name'])
