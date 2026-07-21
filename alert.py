from datetime import datetime
import sqlite3 

curtime = datetime.now().isoformat()
con = sqlite3.connect('events.db')
cur = con.cursor()

cur.execute("""
            SELECT title
            FROM events
            WHERE start_time <= ?
            AND end_time >- ? """, (curtime, curtime))

event = cur.fetchall()
print(event)

cur.execute("DELETE FROM events WHERE end_time <= ?", (curtime,))

con.commit()