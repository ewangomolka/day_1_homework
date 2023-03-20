
year = "2023"
month = "March"
day = "Monday"
date = "20th"

print("Today is "+ day + " the " + date + " of " + month + " " + year + ".")

current_week = 1
current_day_of_week = 1
total_course_weeks = 16
total_course_days_per_week = 5

def weeks_to_go():
    weeks_left = total_course_weeks - current_week
    days_left = total_course_days_per_week - current_day_of_week
    print(f"Only {weeks_left} weeks and {days_left} days to go!")

def motivate_me():
    print("We have got this in the bag!!")

weeks_to_go()
motivate_me()

