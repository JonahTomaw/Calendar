from datetime import datetime
import sqlite3 

while True:
    #curdate = datetime.strftime('%m/%d/%Y')
    #curtime = datetime.strftime('%I/%M')
    curdate = '00/00/00'
    curtime = '00/00'
    con = sqlite3.connect('events.db')
    cur = con.cursor()
    cur.execute('''SELECT title
    FROM events
    WHERE start_date = ?
    AND start_time >= ?
    AND end_time <= ?''', (curdate, curtime, curtime))
    fetch = cur.fetchall
    print(fetch)
    cur.execute('DELETE FROM events WHERE end_time = ?;', (curtime))