# name = 'Mahalakshmi'
# hours_per_day = 3
# weekday_hours = hours_per_day * 5
# is_learning = True

# print(name, type(name))
# print(hours_per_day,type(hours_per_day))
# print(weekday_hours,type(weekday_hours))
# print(is_learning, type(is_learning))
# print(f'{name} studies {weekday_hours} hours on week days')


hours_studied = input("enter how many hours you study per day ")
hours_studied = int(hours_studied)
full_week_hours = hours_studied * 7
print(f'Per day {hours_studied} studied and full week {full_week_hours} studied')
print(type(hours_studied))
print("5"*3)