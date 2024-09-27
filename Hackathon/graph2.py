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

# Query to get data from medals table
query = """SELECT name, medal_type, discipline, event FROM medals;"""
cur.execute(query)
data = cur.fetchall()

# Convert fetched data to a DataFrame
df = pd.DataFrame(data, columns=["Name", "Medal Type", "Discipline", "Event"])

# Count the occurrences of each medal type
medal_counts = df['Medal Type'].value_counts()

# Create a bar chart
plt.bar(medal_counts.index, medal_counts.values, color=['brown', 'silver', 'gold'])
plt.xlabel('Medal Type')
plt.ylabel('Number of Medals')
plt.title('Count of Medals by Type')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

cur.close()
db.close()
