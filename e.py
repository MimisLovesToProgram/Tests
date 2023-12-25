import csv

fieldnames = ["Cell", "Item"]
dict_lines = []

log_lines = []
with open("your_log.log") as log:
    log_lines = log.readlines()

with open("your_excel_or_other_csv.csv", "w") as newcsv:
    writer = csv.DictWriter(newcsv, fieldnames)

    for line in log_lines:
        cell, item = line.rstrip().split(", ")
        dict_lines.append({"Cell": cell, "Item": item})

    writer.writeheader()
    writer.writerows(dict_lines)