import sys
import math

index = int(input("Введите цифру в названии файла, который вы хотите открыть (к примеру X в inmapX.dat) или -1, если вы хотите открыть свой файл: "))
if (index == -1):
    path_f = str(input("Введите название вашего файла (к примеру MyFile.txt): "))
    file = open(path_f, "r")
else:
    file = open("./inmap" + str(index) + ".dat", "r")
count, scale = map(float, file.readline().split())
count = int(count)
sum = 0
print(f"Demyanovich Mikhail\nSimple Map Distance Computations\n\nMap Scale Factor:    {scale} miles per inch\n\n      Map       Mileage\n      Measure   Distance\n============================================================")
for i in range(count):
    float_tmp = float(file.readline())
    print(f"#  {(i + 1):<4} {float_tmp:<4}       {math.ceil(float_tmp * scale * 10) / 10}")
    sum += float(math.ceil(float_tmp * scale * 10) / 10)
print(f"============================================================\nTotal Distance:    {sum} miles")
