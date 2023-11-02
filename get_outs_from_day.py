#!/usr/bin/python3
import json
import csv
from sys import argv

from generate_vocabulary import split_sentence
from classify_naive_bayes import classify_sentence

with open("naive_bayes.json", "r") as file:
    naive_bayes_dict = json.loads(file.read())

with open(f"comments/{argv[1]}/{argv[2]}.json") as file:
    comments = json.loads(file.read())

out_count = 0

for comment in comments:
    if not classify_sentence(split_sentence(comment["text"]), naive_bayes_dict):
        out_count += 1

print(out_count)

# with open("naive_bayes.json", "r") as file:
#     naive_bayes_dict = json.loads(file.read())

# filename = "datasets/2022/potential-outs.csv"
# csvfile = open(filename, "w")

# filewriter = csv.writer(csvfile, delimiter=",",
#                         quotechar="|", quoting=csv.QUOTE_MINIMAL)

# for day in range(1,31):
#     with open(f"comments/2022/{day}.json", "r") as file:
#         comments_json = json.loads(file.read())
    
        
#     for comment in comments_json:
#         sentence = split_sentence(comment["text"])
#         if not classify_sentence(sentence, naive_bayes_dict):
#             filewriter.writerow([comment["text"], "unknown"])

# csvfile.close()
