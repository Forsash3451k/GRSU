import sys
import math

index = int(input("Введите цифру в названии файла, который вы хотите открыть (к примеру X в inmapX.dat): "))
file = open("./inmap" + str(index) + ".dat", "r")
count, scale = map(float, file.readline().split())
count = int(count)
sum = 0
print(f"Demyanovich Mikhail\nSimple Map Distance Computations\n\nMap Scale Factor:    {scale} miles per inch\n\n      Map       Mileage\n      Measure   Distance\n============================================================")
for i in range(count):
    float_tmp = float(file.readline())
    print(f"#  {(i + 1):<4}    {float_tmp:<6}       {math.ceil(float_tmp * scale * 10) / 10}")
    sum += float(math.ceil(float_tmp * scale * 10) / 10)
print(f"============================================================\nTotal Distance:    {sum} miles")
