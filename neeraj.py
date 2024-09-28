import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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


query = """SELECT year, score FROM neerajchopra;""" 
cur.execute(query)


data = cur.fetchall()


df = pd.DataFrame(data, columns=["year", "scores"])


plt.plot(df["year"], df["scores"], marker='o')
plt.xlabel("Year")
plt.ylabel("Score")
plt.title("Neeraj Chopra Scores Over the Years")
plt.grid(True) 
plt.show()

print(df)

cur.close()
db.close()
