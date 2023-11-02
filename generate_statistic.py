#!/usr/bin/python3
import json
from sys import argv

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

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
    yerr = [
        [],
        []
    ]

    for day in range(1,day+1):
        outs = get_outs_at_day(year, day)
        days.append(outs)
        yerr[0].append(outs * (lower_error_margin))
        yerr[1].append(outs * (upper_error_margin))

    labels = range(1,day+1)

    plt.rcParams["font.family"] = "Carlito"
    plt.rcParams["font.size"] = 14

    f = plt.figure()
    f.set_figwidth(15)
    f.set_figheight(8)
    plt.margins(x=0.01, y=0.1)


    ax = plt.bar(labels, days, path_effects=[pe.Stroke(linewidth=1, foreground="black")], color="#95d0fc")
    plt.errorbar(labels, days, yerr=yerr, capsize=3, fmt="none", ecolor="firebrick")
    plt.xticks(np.arange(1, day+1, 1.0))

    plt.xlabel("Day")
    plt.ylabel("Number of people")
    plt.title(f"How many people admitted they were out (2022)")
    
    plt.savefig("graphs/2023-outs.jpeg", dpi=300)

