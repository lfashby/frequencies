
import os
import csv

from matches import MATCHES


word_freq_dict = {}

for dirpath, _, filename in os.walk("freq_tsvs"):
    # Filters out top-most directory
    if filename:
        file_to_match = dirpath.split("/")[1] # for accessing matches.py
        file_path = os.path.join(dirpath, filename[0])
        print("Currently working on", file_path)
        with open(file_path, "r") as frequencies_file:
            frequencies_tsv = csv.reader(frequencies_file, delimiter="\t", quoting=csv.QUOTE_NONE)
            for row in frequencies_tsv:
                word = row[2].lower()
                freq = int(row[3])
                # if regex.match(r"^\p{L}+\p{M}*+$", word):
                if str.isalpha(word):
                    if word not in word_freq_dict:
                        word_freq_dict[word] = freq
                    else:
                        word_freq_dict[word] = word_freq_dict[word] + freq


        temp_path = "merged_tsvs/freq_" + MATCHES[file_to_match]["path"].split("/")[-1]
        merged_tsv_file = open(temp_path, "w")

        with open(MATCHES[file_to_match]["path"], "r") as wiki_file:
            wiki_tsv = csv.reader(wiki_file, delimiter="\t", quoting=csv.QUOTE_NONE)
            for word, pron in wiki_tsv:
                # Check if WikiPron word is in Wortschatz frequencies
                if word in word_freq_dict:
                    print(f"{word}\t{pron}\t{word_freq_dict[word]}", file=merged_tsv_file)
                else:
                    print(f"{word}\t{pron}\t0", file=merged_tsv_file)


        merged_tsv_file.close()