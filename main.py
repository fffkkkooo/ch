year1, month1, day1, hour1, min1, sec1 = map(int, input().split())
year2, month2, day2, hour2, min2, sec2 = map(int, input().split())

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]



seconds_diff = sec2 - sec1
minutes_diff = min2 - min1
hours_diff = hour2 - hour1
days_diff = day2 - day1
months_diff = month2 - month1
years_diff = year2 - year1

if seconds_diff < 0:
    seconds_diff += 60
    minutes_diff -= 1
if minutes_diff < 0:
    minutes_diff += 60
    hours_diff -= 1
if hours_diff < 0:
    hours_diff += 24
    days_diff -= 1
if days_diff < 0:
    if month1 == 1:
        days_in_prev_month = days_in_month[-1]
        days_diff += days_in_prev_month
        months_diff -= 1
    else:
        days_in_prev_month = days_in_month[month1 - 1]
        days_diff += days_in_prev_month
        months_diff -= 1
if months_diff < 0:
    months_diff += 12
    years_diff -= 1


total_days = days_diff + months_diff * days_in_month[month1] + years_diff * 365
total_seconds = seconds_diff + minutes_diff * 60 + hours_diff * 3600


print(total_days, total_seconds)