import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

db=mysql.connector.connect(host="localhost",
                   username="root",
                   password="12345",
                   database="olympic")
if db.is_connected():
    print("Connected to the database")
cur=db.cursor()

query="""select disciplines,count(name) as total_number_of_players from athletes group by disciplines;"""
cur.execute(query)
data=cur.fetchall()
df=pd.DataFrame(data, columns=["total_number_of_players","disciplines"])
plt.bar(df["total_number_of_players"], df["disciplines"])
plt.xticks(rotation=90)
plt.show()
print(df)

cur.close()
db.close()