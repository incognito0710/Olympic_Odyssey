import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="olympic"
)

if db.is_connected():
    print("Connected to the database")

cur = db.cursor()

query = """SELECT year, medal_type FROM manubhakar;"""  
cur.execute(query)

data = cur.fetchall()

df = pd.DataFrame(data, columns=["Year", "medal_type"]) 

medal_map = {'gold': 3, 'silver': 2, 'bronze': 1}
df['medal_value'] = df['medal_type'].map(medal_map)

plt.hist(df[df['medal_type'] == 'gold']['medal_value'], bins=[2.5, 3.5], color='yellow', edgecolor='black', rwidth=0.8, label='Gold')
plt.hist(df[df['medal_type'] == 'silver']['medal_value'], bins=[1.5, 2.5], color='silver', edgecolor='black', rwidth=0.8, label='Silver')
plt.hist(df[df['medal_type'] == 'bronze']['medal_value'], bins=[0.5, 1.5], color='brown', edgecolor='black', rwidth=0.8, label='Bronze')

plt.xticks([1, 2, 3], ['Bronze', 'Silver', 'Gold'])
plt.xlabel('Medal Type')
plt.ylabel('Frequency')
plt.title('Distribution of Medals by Type')

plt.legend()
plt.tight_layout()
plt.show()

cur.close()
db.close()
