# nnn-2023-statistics

This repo contains the files used to create the [r/NoNutNovember](https://reddit.com/r/NoNutNovember) statistics created by u/FraglicherKopierer and his kind helpers.

This repo is still in early development, but creating datasets for the current day should work as follow:
```
./get_rollcall.py YEAR DAY
./create_datasets.py YEAR DAY
```

The datasets will be available under `datasets/YEAR/DAY/NAME-day-DAY.csv`. They will be labeled in a spreadsheet software like LibreOffice.

After the files have been labeled, the classifier can be updated as follow:
```
./generate_labels_from_csv.py
./generate_vocabulary.py
./create_naive_bayes_dict.py
```

A benchmark of the dataset can be generated with:
```
./classify_naive_bayes.py
```

The current benchmark is:
```
The classifier is 97.54% correct for "in".
The classifier is 100.00% correct for "out".
The classifier is 97.57% correct in total.
```
