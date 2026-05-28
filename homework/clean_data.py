# Carga de datos
import glob


def load_data(input_directory):

    sequence = []
    files = glob.glob(f"{input_directory}/*")
    for file in files:
        with open(file, "rt", encoding="utf-8") as f:
            raw_text = f.read()
            sequence.append((file, raw_text))
    return sequence


sequence = load_data(input_directory="../files/input")
for file, text in sequence:
    print(f"{file}  {text[:70]}")
# Clean text
import re


def clean_text(sequence):
    cleaned_sequence = []
    for file, text in sequence:
        cleaned_text = re.sub(r"\n", " ", text)
        cleaned_text = re.sub(r"\s+", " ", cleaned_text)
        cleaned_text = cleaned_text.strip()
        cleaned_text = cleaned_text.lower()
        cleaned_sequence.append((file, cleaned_text))
    return cleaned_sequence


sequence = load_data(input_directory="../files/input")
cleaned_sequence = clean_text(sequence)
for file, text in cleaned_sequence:
    print(f"{file}  {text[:70]}")

# Tokenization

import nltk
nltk.download("punkt_tab")
from nltk.tokenize import word_tokenize




def tokenize(sequence):
    tokenized_sequence = []
    for file, text in sequence:
        tokens = word_tokenize(text)
        tokenized_sequence.append((file, tokens))
    return tokenized_sequence


sequence = load_data(input_directory="../files/input")
cleaned_sequence = clean_text(sequence)
tokenized_sequence = tokenize(cleaned_sequence)
for file, text in tokenized_sequence:
    print(f"{file}  {' '.join(text)[:70]}")