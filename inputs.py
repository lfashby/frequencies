#!/anaconda3/bin/python

import sys
import csv
import regex
from matches import MATCHES

entry = None

if len(sys.argv) >= 2:
  file_path = sys.argv[1]

word_freq_dict = {}

file_to_match = file_path.split("/")[1]

with open(file_path, "r") as frequencies_file:
  frequencies_tsv = csv.reader(frequencies_file, delimiter="\t", quoting=csv.QUOTE_NONE)
  for row in frequencies_tsv:
    word = row[2].lower()
    freq = int(row[3])
    # ^\p{L}+$ is probably sufficient, this regexp pattern is perhaps needlessly specific
    if regex.match(r"^\p{L}+\p{M}*+$", word):
      if word not in word_freq_dict:
        word_freq_dict[word] = freq
      else:
        word_freq_dict[word] = word_freq_dict[word] + freq

merged_tsv_file = open(MATCHES[file_to_match]["file_name"], "w")

with open(MATCHES[file_to_match]["path"], "r") as wiki_file:
  wiki_tsv = csv.reader(wiki_file, delimiter="\t", quoting=csv.QUOTE_NONE)
  for i in range(200):
    val = next(wiki_tsv)
    if val[0] in word_freq_dict:
      print(f"{val[0]}\t{val[1]}\t{word_freq_dict[val[0]]}", file=merged_tsv_file)


# print(word_freq_dict)
# print(len(word_freq_dict))