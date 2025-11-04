import sys
import math

index = input("Введите цифру в названии файла, который вы хотите открыть (к примеру X в PrecipX.txt) или -1, если вы хотите открыть свой файл: ")
if (index == "-1"):
    path_f = str(input("Введите название вашего файла (к примеру MyPrecipData.txt): "))
    file = open(path_f, "r")
else:
    file = open("./Precip" + index +".txt", "r")

print("Programmer: Mikhail Dzemyanovich")
head1 = file.readline()
print(f"{head1[:2]} {head1[2:]}")
head2 = str(file.readline())
month_str, year = file.readline().split(",")
print(f"Precipitation report for {head2[:-1]} during {month_str},{year}")
month_d = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
days_max = int(month_d[month_str])
year = int(year)
if ((year % 4 == 0 and year % 4 != 0) or year % 4 == 0):
    month_d["February"] = 29

count = 3
count = int(count)
max1 = -1
min1 = -1
sum = 0
sum = float(sum)
errors = []
days_d = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 7: -1, 8: -1, 9: -1, 10: -1, 11: -1, 12: -1, 13: -1, 14: -1, 15: -1, 16: -1, 17: -1, 18: -1, 19: -1, 20: -1, 21: -1, 22: -1, 23: -1, 24: -1, 25: -1, 26: -1, 27: -1, 28: -1, 29: -1, 30: -1, 31: -1, }
for data in file.readlines():
    day, downfall = data.split()
    count += 1
    day = int(day)
    downfall = float(downfall)
    if ( day > days_max or day < 1):
        errors.insert(0, f"Invalid {day} {count}")
    else:
        if (days_d[day] != -1):
            errors.insert(0, f"Repeated {day} {count}")
        else:
            days_d[day] = downfall
            
            if (max1 < downfall):
                max1 = downfall
            if (min1 > downfall or min1 == -1):
                min1 = downfall
            sum += downfall
if (len(errors) > 1):
    print("Error         Day    Line")
for data in reversed(errors):
    str1, str2, str3 = data.split()
    print(f"{str1:<8} {str2:>8}  {str3:>6}")
if (len(errors) > 1):
    print()    

print("Day Amount Graph")
for day_t in days_d:
    day_t = int(day_t) 
    downfall_t = float(days_d[day_t - 0])
    if (downfall_t == -1):
        print(f"{day_t:>3}   {"NA":>4}")
    else:
        stars = "*" * int(math.ceil(downfall_t / 0.25))
        print(f"{day_t:>3}   {downfall_t:>4.2f} {stars}")
print("\nMinimum     Maximum     Average")
print(f"{min1:>7.2f}  {max1:>10.2f}  {(sum/days_max):>10.2f}")