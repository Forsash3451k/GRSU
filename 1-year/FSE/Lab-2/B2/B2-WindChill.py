import sys
import math

index = int(input("Введите цифру в названии файла, который вы хотите открыть (к примеру X в X.WCData.txt): "))
file = open(str(index) + ".WCData.txt", "r")
lines = file.readlines()
sum = 0
print("Time     WC temp     WC Effect\n------------------------------")
for i in range(len(lines) - 2):
    time, AT, WS = map(str, lines[i + 2].split())
    WCT = round((35.74 + 0.6125 * float(AT) + (0.4275 * float(AT) - 35.75) * pow(float(WS), 0.16)) * 10) / 10
    sum += WCT
    print(f"{time}    {WCT:<5}        {round((WCT - float(AT)) * 10) / 10:<5}")
print(f"------------------------------\n\nThe average adjusted temperature, based on {len(lines) - 2} observations, was {round(round(sum/(len(lines) - 2) * 100) / 10) / 10}")