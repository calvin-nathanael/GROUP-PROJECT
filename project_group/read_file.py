from pathlib import Path
import csv

coh_path = Path.cwd()/"project_group"/"csv_reports"/"Cash On Hand.csv"

with coh_path.open(mode="r", encoding = "UTF-8") as file:
    reader = csv.reader(file)
    next(reader)

    for line in reader:
        print(line)