#!/usr/local/bin/bash


# Unpack tarballs and put them in a frequencies directory
# Unfortunately frequencies will then be full of folders containing the actual tsv files.
# cd tars/
# for tarball in *
# do
#   stem=${tarball/.*}
#   freq_file_path="${stem}/${stem}-words.txt"
#   tar -C ../frequencies -xzf "$tarball" "$freq_file_path"
#   # > "../normalized/${stem}.tsv"
# done
# cd ..



for val in frequencies/*/*
do
  python inputs.py $val
done

# Need to re-sort the resulting tsv's if we want high-low frequency