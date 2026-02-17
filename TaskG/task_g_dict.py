# Copyright (c) 2026 Ville Heikkiniemi, Luka Hietala, Luukas Kola
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

# Modified by nnn according to given task

"""
A program that prints reservation information according to requirements

The data structure and example data record:

reservationId | name | email | phone | reservationDate | reservationTime | durationHours | price | confirmed | reservedResource | createdAt
------------------------------------------------------------------------
201 | Moomin Valley | moomin@whitevalley.org | 0509876543 | 2025-11-12 | 09:00:00 | 2 | 18.50 | True | Forest Area 1 | 2025-08-12 14:33:20
int | str | str | str | date | time | int | float | bool | str | datetime

"""

from datetime import datetime


def convert_reservation_data(reservation: list[str]) -> dict:
    """
    Convert a list of reservation fields into a dictionary.

    Parameters: 
     reservation (list): Unconverted reservation -> 11 columns 
    
    Returns: 
     converted (dict): Converted data types
    """
    return {
        "id": int(reservation[0]),
        "name": reservation[1],
        "email": reservation[2],
        "phone": reservation[3],
        "date": datetime.strptime(reservation[4], "%Y-%m-%d").date(), # reservationDate 
        "time": datetime.strptime(reservation[5], "%H:%M").time(), # reservationTime
        "duration": int(reservation[6]),
        "price": float(reservation[7]),
        "confirmed": True if reservation[8].strip() == 'True' else False, # confirmed (bool)
        "resource": reservation[9], # reservedResource (str)
        "created": datetime.strptime(str(reservation[10]).strip(), "%Y-%m-%d %H:%M:%S"), # createdAt
    }


def fetch_reservations(reservation_file: str) -> list[dict]:
    """
    Reads reservations from a file and convert each to a dictionary.
    You don't need to modify this function!

    Parameters:
     reservation_file (str): Name of the file containing the reservations

    Returns:
     reservations (dict): Read and converted reservations
    """
    reservations = []
    with open(reservation_file, "r", encoding="utf-8") as f:
        for line in f:
            if len(line.strip()) > 0:
                fields = line.strip().split("|")
                reservations.append(convert_reservation_data(fields))
    return reservations

def confirmed_reservations(reservations: list[dict]) -> None:
    """
    Print confirmed reservations

    Parameters:
     reservations (dict): Reservations
    """
    for reservation in reservations:
        if reservation["confirmed"]: # If confirmed
            print(f"- {reservation['name']}, {reservation['resource']}, {reservation['date'].strftime('%d.%m.%Y')} at {reservation['time'].strftime('%H.%M')}")

def long_reservations(reservations : list[dict]) -> None:
    """
    Print long reservations

    Parameters:
     reservations (dict): Reservations
    """
    for reservation in reservations:
        if reservation["duration"] >= 3: # If long
            print(f"- {reservation['name']}, {reservation['date'].strftime('%d.%m.%Y')} at {reservation['time'].strftime('%H.%M')}, duration {reservation['duration']} h, {reservation['resource']}")


def confirmation_statuses(reservations: list[dict]) -> None:
    """
    Print confirmation statuses

    Parameters:
     reservations (dict): Reservations
    """
    for reservation in reservations:
        print(f"{reservation['name']} → {'Confirmed' if reservation['confirmed'] else 'NOT Confirmed'}")

def confirmation_summary(reservations: list[dict]) -> None:
    """
    Print confirmation summary

    Parameters:
     reservations (dict): Reservations
    """
    confirmed_count = len([reservation for reservation in reservations if reservation["confirmed"]])
    print(f"- Confirmed reservations: {confirmed_count} pcs\n- Not confirmed reservations: {len(reservations) - confirmed_count} pcs")

def total_revenue(reservations: list[dict]) -> None:
    """
    Print total revenue

    Parameters:
     reservations (dict): Reservations
    """
    revenue = sum(reservation["duration"] * reservation["price"] for reservation in reservations if reservation["confirmed"])
    print(f"Total revenue from confirmed reservations: {revenue:.2f} €".replace(".", ","))

def main():
    """
    Prints reservation information according to requirements
    Reservation-specific printing is done in functions
    """
    reservations = fetch_reservations("reservations.txt")
    print("1) Confirmed Reservations")
    confirmed_reservations(reservations)
    print("2) Long Reservations (≥ 3 h)")
    long_reservations(reservations)
    print("3) Reservation Confirmation Status")
    confirmation_statuses(reservations)
    print("4) Confirmation Summary")
    confirmation_summary(reservations)
    print("5) Total Revenue from Confirmed Reservations")
    total_revenue(reservations)

if __name__ == "__main__":
    main()