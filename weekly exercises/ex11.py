number_of_second=int(input("Enter the number of seconds: "))
number_of_minutes=number_of_second//60
number_of_hours=number_of_minutes//60
number_of_days=number_of_hours//24
number_of_weeks=number_of_days//7
if number_of_second<60:
    print(f"{number_of_second} seconds is {number_of_second} seconds")
elif number_of_second<3600:
    print(f"{number_of_second} seconds is {number_of_minutes} minutes and {number_of_second%60} seconds")
elif number_of_second<86400:
    print(f"{number_of_second} seconds is {number_of_hours} hours, {number_of_minutes%60} minutes and {number_of_second%60} seconds")
elif number_of_second<604800:
    print(f"{number_of_second} seconds is {number_of_days} days, {number_of_hours%24} hours, {number_of_minutes%60} minutes and {number_of_second%60} seconds")
else:
    print(f"{number_of_second} seconds is {number_of_weeks} weeks, {number_of_days%7} days, {number_of_hours%24} hours, {number_of_minutes%60} minutes and {number_of_second%60} seconds")