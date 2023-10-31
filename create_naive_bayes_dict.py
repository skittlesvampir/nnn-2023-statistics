#!/usr/bin/python3
import json
import math

def create_naive_bayes_dict(word_counts):
    naive_bayes_dict = {
        "prior_ratio": word_counts["positive_count"] / word_counts["negative_count"],
        "log_prior": math.log(word_counts["positive_count"] / word_counts["negative_count"]),
        "positive_probabilities": {},
        "negative_probabilities": {},
        "lambda": {},
    }

    positive_count = word_counts["positive_count"]
    positive_count_unique = len(word_counts["positive_words"])
    for (word, count) in word_counts["positive_words"]:
        naive_bayes_dict["positive_probabilities"][word] = (count + 1) / (positive_count + positive_count_unique)

    negative_count = word_counts["negative_count"]
    negative_count_unique = len(word_counts["positive_words"])
    for (word, count) in word_counts["negative_words"]:
        naive_bayes_dict["negative_probabilities"][word] = (count + 1) / (negative_count + negative_count_unique)

    for word in naive_bayes_dict["positive_probabilities"]:
        positive_probability = naive_bayes_dict["positive_probabilities"][word]
        negative_probability = naive_bayes_dict["negative_probabilities"][word]

        naive_bayes_dict["lambda"][word] = math.log(positive_probability / negative_probability)

    return naive_bayes_dict


if __name__ == "__main__":
    with open("vocabulary.json", "r") as vocabulary:
        word_counts_json = json.loads(vocabulary.read())

    naive_bayes_dict = create_naive_bayes_dict(word_counts_json)

    with open("naive_bayes.json", "w") as naive_bayes_file:
        naive_bayes_file.write(json.dumps(naive_bayes_dict, indent=4))

