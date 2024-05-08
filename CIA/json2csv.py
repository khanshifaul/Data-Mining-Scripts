import json
import csv
import sys

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as jsonfile:
        data = json.load(jsonfile)
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for item in data:
            writer.writerow(item.values())

if __name__ == '__main__':
    json_file = sys.argv[1]
    csv_file = sys.argv[2]
    json_to_csv(json_file, csv_file)
