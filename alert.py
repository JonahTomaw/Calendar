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

    rows = cur.fetchall()
    con.close()

    return rows

def check_prealerts():
    localtime = datetime.now(ZoneInfo("America/New_York"))
    curtime = localtime.strftime("%Y-%m-%dT%H:%M")

    print("Curent time:", curtime)

    con = sqlite3.connect('events.db')
    cur = con.cursor()

    cur.execute("SELECT title, prealert FROM events")

    rows = cur.fetchall()
    print("Database:", rows)
    
    cur.execute("""
                SELECT title
                FROM events
                WHERE prealert = ?""", (curtime,))
    
    matches = cur.fetchall()
    print("Matches:", matches)

    con.close()

    return matches

def delete_old_events():
    
    localtime = datetime.now(ZoneInfo("America/New_York"))
    curtime = localtime.isoformat()

    con = sqlite3.connect('events.db')
    cur = con.cursor()

    cur.execute("""
    DELETE FROM events
    WHERE end_time < ?""",
    (curtime,))

    con.commit()
    con.close()