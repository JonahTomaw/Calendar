import sqlite3
from datetime import datetime  
import time

def event_create():
    plan = input("do you want to create a new event yes or no:")
    if plan.lower() == "yes":
        con = sqlite3.connect('events.db')
        cur = con.cursor()

        title = input("Title:")

        start = input("what time do you want it to start? Format in 'MM/DD/YY/HH/MM:")
        dt1 = datetime.strptime(start, "%m/%d/%y/%H/%M")

        end = input("Do you want an end time? Format in 'MM/DD/YY/HH/MM.:")
        dt2 = datetime.strptime(end, "%m/%d/%y/%H/%M")

        cur.execute("""INSERT INTO events 
            (start_time, end_time, title)
            VALUES (?, ?, ?);
            """, (dt1.isoformat(), dt2.isoformat(), title))
        
        con.commit()
        con.close()
        time.sleep(1)
    if plan.lower() == "no":
        exit()