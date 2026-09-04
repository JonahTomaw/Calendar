import sqlite3
from datetime import datetime, timedelta

def event_create(title, start, end, time_before):

    con = sqlite3.connect('events.db')
    cur = con.cursor()

    dt1 = datetime.strptime(start, "%Y-%m-%dT%H:%M")
    dt2 = datetime.strptime(end, "%Y-%m-%dT%H:%M")

    if time_before:
        first_alert = dt1 - timedelta(minutes=int(time_before))
    else:
        first_alert = None
        
    cur.execute("""
        INSERT INTO events 
        (start_time, end_time, title, prealert)
        VALUES (?, ?, ?, ?);
    """, (
        dt1.isoformat(),
        dt2.isoformat(),
        title,
        first_alert.isoformat() if first_alert else None
        ))
        
    con.commit()
    con.close()