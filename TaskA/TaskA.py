"""
Program that reads reservation details from a file
and prints them to the console:

Reservation number: 123
Booker: Anna Virtanen
Date: 31.10.2025
Start time: 10.00
Number of hours: 2
Hourly price: 19,95 €
Total price: 39,90 €
Paid: Yes
Location: Meeting Room A
Phone: 0401234567
Email: anna.virtanen@example.com
"""
from datetime import datetime

def main():
    # Define the file name directly in the code
    reservations = "reservations.txt"

    # Open the file and read its contents
    with open(reservations, "r", encoding="utf-8") as f:
        reservation = f.read().strip()

    reservationId = int(reservation.split('|')[0])
    print(f"Reservation number: {reservationId}")

    booker = reservation.split('|')[1]
    print(f"Booker: {booker}")

    date = datetime.strptime(reservation.split('|')[2], "%Y-%m-%d").date()
    finnishDate = date.strftime("%d.%m.%Y")
    print(f"Date: {finnishDate}")

    start = datetime.strptime(reservation.split('|')[3], "%H:%M").time()
    finnishTime = start.strftime("%H:%M")
    print(f"Start time: {finnishTime}")

    numberOfHours = int(reservation.split('|')[4])
    print(f"Number of hours: {numberOfHours}")

    hourly = float(reservation.split('|')[5])
    print(f"Hourly price: {hourly} €")

    total = numberOfHours*hourly
    print(f"Total price: {total:.2f} €")

    paid = bool(reservation.split('|')[6])
    print(f"Paid: {'Yes' if paid else 'No'}")

    location = reservation.split('|')[7]
    print(f"Location: {location}")

    phone = reservation.split('|')[8]
    print(f"Phone: {phone}")

    email = reservation.split('|')[9]
    print(f"Email: {email}")

if __name__ == "__main__":
    main()
