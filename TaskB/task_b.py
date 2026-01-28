"""
A program that reads reservation data from a file
and prints them to the console using functions:

Reservation number: 123
Booker: Anna Virtanen
Date: 31.10.2025
Start time: 10.00
Number of hours: 2
Hourly rate: 19,95 €
Total price: 39,90 €
Paid: Yes
Venue: Meeting Room A
Phone: 0401234567
Email: anna.virtanen@example.com

"""
from datetime import datetime

def print_reservation_number(reservation: list) -> None:
    """
    Prints the reservation number

    Parameters:
     reservation (lst): reservation -> columns separated by |
    """
    
    reservationID = int(reservation[0])
    print(f"Reservation number: {reservationID}")
    
def print_booker(reservation: list) -> None:
    """
    Prints the reservation number

    Parameters:
     reservation (lst): reservation -> columns separated by |
    """
    booker = reservation[1]
    print(f"Booker: {booker}")

def print_date(reservation: list) -> None:
    """
    Prints the reservation number

    Parameters:
     reservation (lst): reservation -> columns separated by |
    """
    date = datetime.strptime(reservation[2], "%Y-%m-%d").date()
    finnishDate = date.strftime("%d.%m.%Y")
    print(f"Date: {finnishDate}")

def print_start_time(reservation: list) -> None:  
    start = datetime.strptime(reservation[3], "%H:%M").time()
    finnishTime = start.strftime("%H:%M")
    print(f"Start time: {finnishTime}")

def print_hours(reservation: list) -> None:
    numberOfHours = int(reservation[4])
    print(f"Number of hours: {numberOfHours}")

def print_hourly_rate(reservation: list) -> None:
    hourly = float(reservation[5])
    print(f"Hourly price: {hourly} €")

def print_total_price(reservation: list) -> None:
    total = int(reservation[4])*float(reservation[5])
    print(f"Total price: {total:.2f} €")

def print_paid(reservation: list) -> None:
    paid = bool(reservation[6])
    print(f"Paid: {'Yes' if paid else 'No'}")

def print_venue(reservation: list) -> None:
    location = reservation[7]
    print(f"Location: {location}")

def print_phone(reservation: list) -> None:
    phone = reservation[8]
    print(f"Phone: {phone}")

def print_email(reservation: list) -> None:
    email = reservation[9]
    print(f"Email: {email}")

def main():
    """
    Reads reservation data from a file and
    prints them to the console using functions
    """
    # Define the file name directly in the code
    reservations = "reservations.txt"

    # Open the file, read it, and split the contents
    with open(reservations, "r", encoding="utf-8") as f:
        reservation = f.read().strip()
        reservation = reservation.split('|')

    print_reservation_number(reservation)
    print_booker(reservation)
    print_date(reservation)
    print_start_time(reservation)
    print_hours(reservation)
    print_hourly_rate(reservation)
    print_total_price(reservation)
    print_paid(reservation)
    print_venue(reservation)
    print_phone(reservation)
    print_email(reservation)

if __name__ == "__main__":
    main()
