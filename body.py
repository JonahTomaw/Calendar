import sqlite3
from datetime import datetime  
import time

while True:
    plan = input("do you want to create a new event yes or no:")
    if plan.lower() == "yes":
        con = sqlite3.connect('events.db')
        cur = con.cursor()

        title = input("Title:")

        start = input("what time do you want it to start? Format in 'MM/DD/YY/HH/MM:")
        date1 = start[:8]
        time1 = start[9:]

        end = input("Do you want an end time? Format in 'MM/DD/YY/HH/MM.:")
        date2 = end[:8]
        time2 = end[9:]

        cur.execute(f"""INSERT INTO events 
                    (start_date, start_time, end_date, end_time, title)
                    VALUES (?, ?, ?, ?, ?);
                    """, (date1, time1, date2, time2, title))
        con.commit()
        con.close()
        
        time.sleep(1)
    elif plan.lower() == 'no':
        con.close()
        exit()