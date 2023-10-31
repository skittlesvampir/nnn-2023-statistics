#!/usr/bin/python3
import string
import json

def split_sentence(sentence):
    words = sentence.split()
    sentence = [word.strip(string.punctuation) for word in words]
    sentence = [word.lower() for word in sentence]
    return sentence

def add_sentence_to_frequency_dict(sentence, frequency_dict, is_positive):
    if is_positive:
        key = "positive_words"
        other_key = "negative_words"
    else:
        key = "negative_words"
        other_key = "positive_words"

    for word in sentence:
        if word not in frequency_dict[key]:
            frequency_dict[key][word] = 0
        if word not in frequency_dict[other_key]:
            frequency_dict[other_key][word] = 0

        frequency_dict[key][word] += 1

    return frequency_dict

if __name__ == "__main__":
    frequency_dict = {
        "positive_count": 0,
        "negative_count": 0,
        "positive_words": {},
        "negative_words": {},
    }
    
    with open("labeled_comments.json", "r") as labels:
        labels_json = json.loads(labels.read())

    for line in labels_json:
        sentence = split_sentence(line["text"])

        frequency_dict = add_sentence_to_frequency_dict(sentence, frequency_dict, line["positive"])

        if line["positive"]:
            frequency_dict["positive_count"] += len(sentence)
        else:
            frequency_dict["negative_count"] += len(sentence)

    frequency_dict["positive_words"] = sorted(frequency_dict["positive_words"].items(), key=lambda k:k [1], reverse=True)
    frequency_dict["negative_words"] = sorted(frequency_dict["negative_words"].items(), key=lambda k:k [1], reverse=True)

    with open("vocabulary.json", "w") as vocabulary:
        vocabulary.write(json.dumps(frequency_dict, indent=4))
    
