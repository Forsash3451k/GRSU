import sys

def decode(seq):
    text = ""
    for i in range(0, len(seq)):
        if(seq[i] >= '3' and seq[i] <= '9'):
            text += seq[i + 1] * int(seq[i])
            i += 1
            continue
        text += seq[i]
    return text

def search(data, seq):
    seq = decode(seq)
    print("organism				protein", file=output_file)
    found = False
    for protein in data:
        name, organism, amino = protein.split('\t')
        if amino.find(seq) != -1:
            found = True
            print(f"{organism}          {name}", file=output_file)
    if not found:
        print("NOT FOUND", file=output_file)

def diff(data, name1, name2):
    amino1 = ""
    amino2 = ""
    for protein in data:
        name, _, amino = protein.split('\t')
        amino = amino[:-1]
        if name == name1:
            amino1 = decode(amino)
        if name == name2:
            amino2 = decode(amino)
    if amino1 == "" or amino2 == "":
        print("MISSING:")
        if amino1 == "":
            print(name1, file=output_file)
        if amino2 == "":
            print(name2, file=output_file)
    else:
        res = abs(len(amino1) - len(amino2))
        for i in range(0, min(len(amino1), len(amino2))):
            if amino1[i] != amino2[i]:
                res += 1
        print("amino-acids difference:", file=output_file)
        print(res, file=output_file)

def mode(data, mname):
    seq = ""
    for protein in data:
        name, _, amino = protein.split('\t')
        if name == mname:
            seq = decode(amino)
    if seq == "":
        print("MISSING:", file=output_file)
        print(mname, file=output_file)
    else:
        acids = {f"{seq[0]}":0}
        for i in range(0, len(seq)):
            if seq[i] not in acids:
                acids[seq[i]] = 0
            acids[seq[i]] += 1
        maximal = seq[0]
        for name, count in acids.items():
            if count > acids[maximal] or (count == acids[maximal] and name < maximal):
                maximal = name
        print("amino-acid occurs:", file=output_file)
        print(f"{maximal}          {acids[maximal]}", file=output_file)

index = input("Введите цифру в названии файла, который вы хотите открыть (к примеру X в commands.X.txt и sequences.X.txt): ")
data = open("./sequences." + index +".txt", "r").readlines()
commands = open("./commands." + index +".txt", "r").readlines()

output_file = open("./genedata." + index + ".txt", "w", encoding="utf-8")

counter = 1
separator = "--------------------------------------------------------------------------"

print("Dzemyanovich Mikhail\nGenetic Searching", file=output_file)
for line in commands:
    print(separator, file=output_file)
    arguments = line.split('\t')
    arguments[-1] = arguments[-1][:-1]
    if arguments[0] == "search":
        print(f"{counter:0>3}   search   {arguments[1]}", file=output_file)
        search(data, arguments[1])
    elif arguments[0] == "diff":
        print(f"{counter:0>3}   diff   {arguments[1]}   {arguments[2]}", file=output_file)
        diff(data, arguments[1], arguments[2])
    elif arguments[0] == "mode":
        print(f"{counter:0>3}   mode   {arguments[1]}", file=output_file)
        mode(data, arguments[1])
    counter += 1
print(separator, file=output_file)