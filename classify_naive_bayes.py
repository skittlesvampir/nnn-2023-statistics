#!/usr/bin/python3
import json
import math
from generate_vocabulary import split_sentence

def classify_sentence(sentence, naive_bayes_dict):
    sum = naive_bayes_dict["log_prior"]

    for word in sentence:
        if word not in naive_bayes_dict["positive_probabilities"]:
            continue
        
        # use log likelyhood
        sum += naive_bayes_dict["lambda"][word]

    if sum >= 0:
        return True

    return False

def test_against_labeled_dataset(test=[True, False]):
    with open("naive_bayes.json", "r") as naive_bayes_file:
        naive_bayes_dict = json.loads(naive_bayes_file.read())

    with open("testset.json", "r") as labeled_file:
        labeled_comments = json.loads(labeled_file.read())

    total = 0
    correct = 0

    for comment in labeled_comments:
        if comment["positive"] not in test:
            continue

        total += 1
        
        sentence = split_sentence(comment["text"])

        if classify_sentence(sentence, naive_bayes_dict) == comment["positive"]:
            correct += 1

    return correct / total

# get the upper and lower error margins for comments that say "i'm out"
def get_error_margins_for_out():
    positives_correct = test_against_labeled_dataset([True])
    positives_false = 1 - positives_correct # comments that were labeled as "in" but are actually "out" (upper bound)

    negatives_correct = test_against_labeled_dataset([False])
    negatives_false = 1 - negatives_correct # comments that were labeled as "out" but are actualyl "in" (lower bound)

    return (negatives_false, positives_false)
    

if __name__ == "__main__":
    accuracy = test_against_labeled_dataset(test=[True])
    accuracy_percent = '%.2f'%(accuracy * 100)
    print(f"The classifier is {accuracy_percent}% correct for \"in\".")

    
    accuracy = test_against_labeled_dataset(test=[False])
    accuracy_percent = '%.2f'%(accuracy * 100)
    print(f"The classifier is {accuracy_percent}% correct for \"out\".")

    accuracy = test_against_labeled_dataset(test=[True, False])
    accuracy_percent = '%.2f'%(accuracy * 100)
    print(f"The classifier is {accuracy_percent}% correct in total.")
