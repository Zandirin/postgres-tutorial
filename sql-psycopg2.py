import psycopg2


# connect to the database named chinook
connection = psycopg2.connect(database="chinook")

# create cursor object
cursor = connection.cursor()

# First Query - Select all record in Artist table
# cursor.execute('SELECT * FROM "Artist"')

# Second Query - Select the name column from artist table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Third Query - Find Queen in Artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Fourth Query - Select specified artistid from artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Fifth Query - Select only the albums from the album list with artist ID of 51
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Sixth Query - Select all tracks composed by Queen
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch multiple results
results = cursor.fetchall()

# fetch singular result
# results = cursor.fetchone()

# close connection
connection.close()

# print results
for result in results:
    print(result)
