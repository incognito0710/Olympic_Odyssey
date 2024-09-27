
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    username="root",
    password="12345",
    database="olympic"
)

if db.is_connected():
    print("Connected to the database")

cur = db.cursor()

# Query to get the total number of players by birth place
query = """SELECT birth_place, COUNT(name) AS total_number_of_players 
           FROM athletes 
           GROUP BY birth_place;"""
cur.execute(query)
data = cur.fetchall()

# Filter out rows with None values
data = [(birth_place, total) for birth_place, total in data if birth_place is not None]

# Create the DataFrame
df = pd.DataFrame(data, columns=["birth_place", "total_number_of_players"])

# Create the bar chart
plt.bar(df["birth_place"], df["total_number_of_players"])
plt.xlabel('Birth Place')
plt.ylabel('Total Number of Players')
plt.title('Number of Players by Birth Place')
plt.xticks(rotation=90)
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

# Print the DataFrame
print(df)

cur.close()
db.close()
