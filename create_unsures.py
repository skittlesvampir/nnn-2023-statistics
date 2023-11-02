#!/usr/bin/python3
import json
import csv
from classify_naive_bayes import classify_sentence
from generate_vocabulary import split_sentence

# use this file to manually sort out edge cases (like day 1 and day 30)

csvfile = open("datasets/2022/day-30-unsures.csv", "w")
csvwriter = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)

with open(f"comments/2022/30.json", "r") as file:
    comments = json.load(file)

with open("naive_bayes.json", "r") as file:
    naive_bayes_dict = json.load(file)

unsure_count = 0
for comment in comments:
    sentence = split_sentence(comment["text"])
    if not classify_sentence(sentence, naive_bayes_dict):
        unsure_count += 1
        csvwriter.writerow([comment["text"], "unknown"])

print(unsure_count)

file.close()

