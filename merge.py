
import csv
import json
import os

# from matches import MATCHES

with open("wortschatz_languages.json", "r") as langs:
    languages = json.load(langs)

word_freq_dict = {}
types = ["_phonetic.tsv", "_phonemic.tsv" ]

for freq_file in os.listdir("freq_tsvs"):
    file_to_match = freq_file.rsplit("-", 1)[0] # for accessing matches.py
    print("Currently working on", file_to_match)
    with open(f"freq_tsvs/{freq_file}", "r") as tsv:
        frequencies_tsv = csv.reader(tsv, delimiter="\t", quoting=csv.QUOTE_NONE)
        for row in frequencies_tsv:
            # TSVs are not uniformly formatted.
            try:
                word = row[2].lower()
                freq = int(row[3])
            except IndexError:
                word = row[1].lower()
                freq = int(row[2])
            # if regex.match(r"^\p{L}+\p{M}*+$", word):
            if str.isalpha(word):
                if word not in word_freq_dict:
                    word_freq_dict[word] = freq
                else:
                    word_freq_dict[word] = word_freq_dict[word] + freq
    
    for stuff in languages[file_to_match]["path"]:
        # Try phonetic and phonemic
        for phon in types:
            # Wikipron tsv
            file_to_target = stuff + phon 
            # print(file_to_target)
            try:
                # This is written to be done after remove_duplicates
                # Will this retain the sorted order of the entries though?
                with open(file_to_target, "r") as wiki_file:
                    wiki_tsv = csv.reader(wiki_file, delimiter="\t", quoting=csv.QUOTE_NONE)
                    temp_path = "merged_tsvs/freq_" + stuff.split("/")[-1] + phon
                    merged_tsv_file = open(temp_path, "w")
                    for word, pron in wiki_tsv:
                        # Check if WikiPron word is in Wortschatz frequencies
                        if word in word_freq_dict:
                            print(f"{word}\t{pron}\t{word_freq_dict[word]}", file=merged_tsv_file)
                        else:
                            print(f"{word}\t{pron}\t0", file=merged_tsv_file)
                merged_tsv_file.close()
            except FileNotFoundError as err:
                print(err)
                continue

