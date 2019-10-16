#!/bin/bash

mkdir tars
mkdir frequencies
python grab_data.py

# Unpack tarballs and put them in a frequencies directory
cd tars/
for tarball in *
do
  stem=${tarball/.*}
  freq_file_path="${stem}/${stem}-words.txt"
  tar -C ../frequencies -xzf "$tarball" "$freq_file_path"
done
cd ..



for val in frequencies/*/*
do
  python inputs.py $val
done


# rm -rf tars
# rm -rf frequencies