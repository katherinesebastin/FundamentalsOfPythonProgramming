# Copyright (c) 2025 Katherine
# License: MIT

from datetime import datetime, date

def convert_data(line: list) -> list:
    """
    Convert data types to meet program requirements

    Parameters:
     line (list): Unconverted reservation -> 7 columns

    Returns:
     (list): Converted data types
    """
    return [
        datetime.fromisoformat(line[0]),
        float(line[1].replace(",", ".")), #consumption
        float(line[2].replace(",", ".")), #production
        float(line[3].replace(",", ".")), #temperature
    ]

def read_data(filename: str) -> list:
    """
    Reads the CSV file and returns the rows in a suitable structure.
    
    Parameters:
     filename(str): Name of the file containing the electricity consumption and production
    
    Returns:
     cons_prod (list): Read and converted consumption and production
    """
    cons_prod = []
    with open(filename, "r", encoding="utf-8") as f:
        next(f)
        for line in f:
            line = line.strip()
            fields = line.split(";")
            cons_prod.append(convert_data(fields))
    return cons_prod

def show_main_menu() -> str:
    """
    Prints the main menu and returns the user selection as a string.

    Returns:
     selection (str): user selection
    """
    print("Choose a report type:")
    print("1) Daily summary for a date range")
    print("2) Monthly summary for one month")
    print("3) Full year 2025 summary")
    print("4) Exit the program")
    return input("Your choice: ")

def show_sub_menu(report: str) -> str:
    """
    Prints the sub menu and returns the user selection as a string.

    Parameters:
     report (string): printable report

    Returns:
     selection (str): user selection
    """
    print("What would you like to do next?") 
    print("1) Write the report to the file report.txt") 
    print("2) Create a new report")
    print("3) Exit")
    selection = input("Your choice: ")
    match selection:
        case "1":
            write_report_to_file(report)
    return selection

def create_daily_report(data: list) -> str:
    """
    Builds a daily report for a selected date range.
    
    Parameters:
     data (int): Consumption and production data + dates

    Returns:
     printable string based on the date range
    """
    start_date_str = input("Enter start date (dd.mm.yyyy): ")
    start_date = datetime.strptime(start_date_str, "%d.%m.%Y").date()
    end_date_str = input("Enter end date (dd.mm.yyyy): ")
    end_date = datetime.strptime(end_date_str, "%d.%m.%Y").date()
    cons = 0
    prod = 0
    temp = 0
    i = 0
    for per_hour in data:
        if start_date <= per_hour[0].date() <= end_date:
            cons += per_hour[1]
            prod += per_hour[2]
            temp += per_hour[3]
            i += 1
    msg = "-----------------------------------------------------\n"
    msg = f"Report for the period {start_date_str}-{end_date_str}\n"
    msg += f"- Total consumption: " + f"{cons:.2f}".replace(".", ",") + f"kWh\n"
    msg += f"- Total production: " + f"{prod:.2f}".replace(".", ",") + f"kWh\n"
    msg += f"- Average temperature: " + f"{temp/i:.2f}".replace(".", ",") + f"°C\n"
    return msg

def create_monthly_report(data: list) -> list[str]:
    """
    Builds a monthly summary report for a selected month.
    
    Parameters:
     data (list): Consumption and production data + dates

    Returns:
     (str): Printable monthly report
    """
    month_str = input("Enter month number (1–12): ")
    month = int(month_str)
    cons = 0
    prod = 0
    temp = 0
    i = 0
    for per_hour in data:
        if per_hour[0].month == month:
            cons += per_hour[1]
            prod += per_hour[2]
            temp += per_hour[3]
            i += 1
    month_names = {
        1: "January", 2: "February", 3: "March",
        4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September",
        10: "October", 11: "November", 12: "December" }
    avg_temp = temp / i if i > 0 else 0
    msg = "-----------------------------------------------------\n"
    msg += f"Report for the month: {month_names.get(month, '')}\n"
    msg += f"- Total consumption: " + f"{cons:.2f}".replace(".", ",") + " kWh\n"
    msg += f"- Total production: " + f"{prod:.2f}".replace(".", ",") + " kWh\n"
    msg += f"- Average temperature: " + f"{avg_temp:.2f}".replace(".", ",") + " °C\n"
    return msg

def create_yearly_report(data: list) -> list[str]:
    """
    Builds a full-year summary report.

    Parameters:
     data (list): Consumption and production data + dates

    Returns:
     (str): Printable monthly report
    """
    cons = 0
    prod = 0
    temp = 0
    i = 0
    for per_hour in data:
        cons += per_hour[1]
        prod += per_hour[2]
        temp += per_hour[3]
        i += 1
    avg_temp = temp / i if i > 0 else 0
    msg = "-----------------------------------------------------\n"
    msg += "Report for the year: 2025\n"
    msg += f"- Total consumption: " + f"{cons:.2f}".replace(".", ",") + " kWh\n"
    msg += f"- Total production: " + f"{prod:.2f}".replace(".", ",") + " kWh\n"
    msg += f"- Average temperature: " + f"{avg_temp:.2f}".replace(".", ",") + " °C\n"
    return msg

def print_report_to_console(lines: list[str]) -> None:
    """
    Prints report lines to the console.

    Parameter:
     lines (string): printable report
    """
    print(lines)

def write_report_to_file(lines: list[str]) -> None:
    """
    Writes report lines to the file report.txt.

    Parameters:
     content (str): Content
    """
    with open("report.txt", "w" , encoding="utf-8") as f:
        f.write(lines)

def main() -> None:
    """
    Main function: reads data, shows menus, and controls report generation.
    """
    db = read_data("2025.csv")
    while True:
        match show_main_menu():
            case "1":
                daily_report = create_daily_report(db)
                print_report_to_console(daily_report)
                match show_sub_menu(daily_report):
                    case "1":
                        continue
                    case "2":
                        continue
                    case "3":
                        print("Thank you! Bye!")
                        break
            case "2":
                monthly_report = create_monthly_report(db)
                print_report_to_console(monthly_report)
                match show_sub_menu(monthly_report):
                    case "1":
                        continue
                    case "2":
                        continue
                    case "3":
                        print("Thank you! Bye!")
                        break 
            case "3":
                yearly_report = create_yearly_report(db)
                print_report_to_console(yearly_report)
                match show_sub_menu(yearly_report):
                    case "1":
                        continue
                    case "2":
                        continue
                    case "3":
                        print("Thank you! Bye!")
                        break
            case "4":
                print("Thank you! Bye!")
                break
   
if __name__ == "__main__":
    main()