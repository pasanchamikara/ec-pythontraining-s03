import csv

try:
    with open('asia-cup-refined-winners.csv', mode='w', newline='') as writefile:
        writer = csv.writer(writefile)
        with open('asia-cup-winners.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                writer.writerow([row[0], row[4], row[2]])
    # Print only year, Winning Team and the Host
except Exception(e):
    print(e.message)
finally:
    file.close()
    writefile.close()
