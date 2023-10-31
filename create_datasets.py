#!/usr/bin/python3

import random
import json
import csv
import os
from sys import argv

DATASET_SIZE=100

def create_unmarked_datasets(volunteers, day, year):
    with open(f"comments/{year}/{day}.json", "r") as file:
        comments = file.read()

    comments = json.loads(comments)
    
    random.shuffle(comments)

    for (i, username) in enumerate(volunteers):
        directory = f"datasets/{year}/{day}"
        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = directory + f"/{username}-day-{day}.csv"
        with open(filename, "w") as csvfile:
            filewriter = csv.writer(csvfile, delimiter=",",
                                    quotechar="|", quoting=csv.QUOTE_MINIMAL)
            for i in range(i*DATASET_SIZE,(i+1)*DATASET_SIZE):
                filewriter.writerow([comments[i]["text"], "unknown"])
            

volunteers = ["FraglicherKopierer", "Filip", "Abby"]
create_unmarked_datasets(volunteers, argv[2], argv[1])
