import sys
import csv
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load Formatters
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
# Load Unformatted Train Data (and ignore encoding errors?)
trainfile = open('train.csv', errors="ignore")
reader = csv.reader(trainfile)
# Open New File for Formatted Training Data
f = open("processed-train.txt", "x")
data = ""
# Skip First Line
next(reader, None)
progress = 0
# Process each line
for comment in reader:
    progress+=1
    print(progress)
    # Break words up and remove non-aphebetical noise (I swear I can spell)
    word_tokens = word_tokenize(re.sub(r"[^a-zA-Z]+", ' ', comment[1]))
    filtered_sentence = []
    # Go through each word, Lower Case it and then Lemmatize it (aka break down into root)
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(lemmatizer.lemmatize(w.lower()))
    label = "__label__1"
    prof_index = 0
    # Scan for any form of profanity and apply the label if it existed
    while prof_index < 6:
        if comment[2 + prof_index] == "1":
            label = "__label__2"
        prof_index+=1
    # Add new line to New File
    data += label + " " + ' '.join(filtered_sentence) + "\n"
# Write all the lines
f.write(data)
f.close()