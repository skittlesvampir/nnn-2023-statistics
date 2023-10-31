#!/usr/bin/python3
from glob import glob
import os
import json
import csv

def generate_labeled_json():
    files = [y for x in os.walk("datasets") for y in glob(os.path.join(x[0], "*.csv"))]

    labeled_comments = []

    for file in files:
        with open(file, "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)

            for row in csv_reader:
                if row[1] != "n" and row[1] != "y":
                    continue

                is_positive = row[1] == "y"

                labeled_comments.append({
                                     "text": row[0],
                                     "positive": is_positive,
                                 })

    with open("labeled_comments.json", "w") as labeled_comments_file:
        labeled_comments_file.write(json.dumps(labeled_comments, indent=4))

            
    
if __name__ == "__main__":
    generate_labeled_json()
