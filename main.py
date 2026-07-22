from create_event import event_create
from alert import check_alerts

while True:
    print("1. Create event")
    print("2. Check alerts")
    print("3. Exit")

    choice = input("> ")

    if choice == "1":
        event_create()
    elif choice == "2":
        check_alerts()
    elif choice == "3":
        break