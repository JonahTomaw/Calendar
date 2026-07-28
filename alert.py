from datetime import datetime
import sqlite3 
from zoneinfo import ZoneInfo

def check_alerts():
    localtime = datetime.now(ZoneInfo("America/New_York"))
    curtime = localtime.isoformat()
    con = sqlite3.connect('events.db')
    cur = con.cursor()

    cur.execute("""
                SELECT title
                FROM events
                WHERE start_time <= ?
                AND end_time >= ? """, (curtime, curtime))

    print('on going')
    rows = cur.fetchall()
    for i in rows:
        for q in i:
            print(q)
    cur.execute("DELETE FROM events WHERE end_time <= ?", (curtime,))

    con.commit()