#!/usr/bin/python3
import json
from generate_vocabulary import split_sentence

def classify_sentence(sentence, naive_bayes_dict):
    product = 1 / naive_bayes_dict["prior_ratio"]

    for word in sentence:
        if word not in naive_bayes_dict["positive_probabilities"]:
            continue
        
        product *= naive_bayes_dict["positive_probabilities"][word] / naive_bayes_dict["negative_probabilities"][word]

    if product >= 1:
        return True

    return False

def test_against_labeled_dataset(test=[True, False]):
    with open("naive_bayes.json", "r") as naive_bayes_file:
        naive_bayes_dict = json.loads(naive_bayes_file.read())

    with open("labeled_comments.json", "r") as labeled_file:
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
