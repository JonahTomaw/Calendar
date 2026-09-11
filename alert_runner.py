import time
from alert import check_prealerts

while True:
    alerts = check_prealerts()

    if alerts:
        print("ALERT:", alerts)

    time.sleep(60)