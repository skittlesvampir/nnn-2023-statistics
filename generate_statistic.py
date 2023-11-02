#!/usr/bin/python3
import json
from sys import argv

import numpy as np
import matplotlib.pyplot as plt

from generate_vocabulary import split_sentence
from classify_naive_bayes import classify_sentence, get_error_margins_for_out

def get_outs_at_day(year, day):
    if day == 30 and year == 2022: # last day has a few more false negatives
        return 17
    
    with open("naive_bayes.json", "r") as file:
        naive_bayes_dict = json.load(file)
    
    with open(f"comments/{year}/{day}.json", "r") as file:
        comments = json.load(file)

    number_of_outs = 0
    for comment in comments:
        sentence = split_sentence(comment["text"])
        if not classify_sentence(sentence, naive_bayes_dict):
            number_of_outs += 1

    return number_of_outs

if __name__ == "__main__":
    year = int(argv[1])
    day = int(argv[2])
    
    (lower_error_margin, upper_error_margin) = get_error_margins_for_out()

    days = []

    for day in range(1,day+1):
        days.append(get_outs_at_day(year, day))

    labels = range(1,day+1)
    # days = [158, 79, 91, 123, 134, 143, 135, 181, 159, 143, 125, 130, 137, 115, 112, 84, 75, 69, 62, 57, 48, 45, 35, 27, 23, 24, 29, 23, 31, 94]

    f = plt.figure()
    f.set_figwidth(15)

    plt.bar(labels, days)
    plt.xticks(np.arange(1, day+1, 1.0))
    plt.show()

