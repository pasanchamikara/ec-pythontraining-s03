import csv
import os

fn = os.path.join(os.path.dirname(__file__), '..', 'feed', 'asia-cup-winners.csv') 
op = os.path.join(os.path.dirname(__file__), '..', 'feed', 'asia-cup-refined-winners.csv') 

try:
    with open(op, mode='w', newline='') as writefile:
        writer = csv.writer(writefile)
        with open(fn, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                writer.writerow([row[0], row[4], row[2]])
    # Print only year, Winning Team and the Host
except Exception(e):
    print(e.message)
finally:
    file.close()
    writefile.close()
