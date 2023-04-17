import csv
count=0
with open('9_3/inp.csv', newline='') as File:
    reader = csv.reader(File)
    print("\nНужно купить:")
    next(reader)
    for row in reader:
        print(row[0]+" - " + row[1]+"шт." +" за "+row[2] + " руб.")
        count = count + int(row[1]) * int(row[2])
    print("Итоговая сумма: " + str(count) + " руб.")