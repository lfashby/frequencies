#!/anaconda3/bin/python

import sys
import csv
import itertools

# Downward match should print added frequencies
# Upward match should print 0 (meaning they are not added to tsv by bash script)
# Matchless should print False

entry = None
count = 0

if len(sys.argv) >= 2:
  entry = sys.argv[1:]

# An entry with a match would look like:
# ['Sie', '453', '66:136\tsie\tsie\t502\n73:143\tSie\tSie\t453']

# Sort of assuming we only ever get two matches...
grep_val = entry[-1]
matches = grep_val.split("\n")

# Meaning we actually have a match
if len(matches) >= 2:
  first_match = matches.pop(0).split("\t")
  # first_match = matches[0].split("\t")

  # Check that we are moving downward
  if entry[0] == first_match[1]:
    # Cycle through all matches
    for remaining in matches:
      remaining = remaining.split("\t")
      # Eliminate false matches like "muss" and "muss gehen"
      if first_match[1].lower() == remaining[1].lower():
        count += int(first_match[-1]) + int(remaining[-1])
else:
  count = False


print(count)