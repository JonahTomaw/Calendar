import time
from datetime import datetime
from alert import check_prealerts

def send_notifications(alerts):
    print("NOTIFICATION:", alerts)

while True:
    now = datetime.now()

    seconds = 60 - now.second
    time.sleep(seconds)

    alerts = check_prealerts()

    if alerts:
        send_notifications(alerts[0][0])