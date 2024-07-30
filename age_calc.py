from datetime import date

def calculate_age(birthday):
    today = date.today()

    if today < birthday:
        return "Invalid birthdate. Please enter a valid date."
    
    day_check = (today.month, today.day) < (birthday.month, birthday.day)
    year_diff = today.year - birthday.year - day_check

    if today.day >= birthday.day:
        remaining_days = today.day - birthday.day
    else:
        previous_month = (today.month - 1) if today.month > 1 else 12
        previous_year = today.year if today.month > 1 else today.year - 1
        previous_month_days = (date(previous_year, previous_month + 1, 1) - date(previous_year, previous_month, 1)).days
        remaining_days = today.day + previous_month_days - birthday.day
        today = today.replace(month=today.month - 1 if today.month > 1 else 12)

    if today.month >= birthday.month:
        remaining_months = today.month - birthday.month
    else:
        remaining_months = 12 - (birthday.month - today.month)

    age_string = f"Age: {year_diff} years, {remaining_months} months and {remaining_days} days"
    return age_string

if __name__ == '__main__':
    print(" Age calculate by Python")

    try:
        birthyear = int(input("Enter the birth year (YYYY): "))
        birthmonth = int(input("Enter the birth month (MM): "))
        birthday = int(input("Enter the birth day (DD): "))
        dateofbirth = date(birthyear, birthmonth, birthday)

        age = calculate_age(dateofbirth)
        print(age)
    except ValueError:
        print("Invalid input. Try: XXXX, MM, DD as integers.")
