#!/anaconda3/bin/python

import sys
import csv
import regex
from matches import MATCHES

entry = None

if len(sys.argv) >= 2:
  file_path = sys.argv[1]

print("Currently working on:", file_path)
word_freq_dict = {}
wiki_tsv_dict = {}

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

# Because I am potentially removing repeats, the best thing to do is probably write new tsvs
# Delete the old ones (although perhaps we will lose some data...)
temp_path = "./merged_tsvs/freq_" + MATCHES[file_to_match]["path"].split("/")[-1]
merged_tsv_file = open(temp_path, "w")

with open(MATCHES[file_to_match]["path"], "r") as wiki_file:
  wiki_tsv = csv.reader(wiki_file, delimiter="\t", quoting=csv.QUOTE_NONE)
  for row in wiki_tsv:
    val = row
    # Check if wiki_tsv word is in Wortschatz frequencies
    if val[0] in word_freq_dict:
      # Skip repeat transcriptions in wiki tsvs (if transcription and word are identical)
      if val[1] in wiki_tsv_dict and wiki_tsv_dict[val[1]] == val[0]:
        continue
      wiki_tsv_dict[val[1]] = val[0]
      print(f"{val[0]}\t{val[1]}\t{word_freq_dict[val[0]]}", file=merged_tsv_file)

merged_tsv_file.close()


# print(word_freq_dict)
# print(len(word_freq_dict))