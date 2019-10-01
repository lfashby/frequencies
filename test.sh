#!/usr/local/bin/bash


# Unpack tarballs and put them in a frequencies directory
# Unfortunately frequencies will then be full of folders containing the actual tsv files.
cd tars/
for tarball in *
do
  stem=${tarball/.*}
  freq_file_path="${stem}/${stem}-words.txt"
  tar -C ../frequencies -xzf "$tarball" "$freq_file_path"
  > "../normalized/${stem}.tsv"
done
cd ..


cd frequencies/
for val in *
do
  name="${val}.tsv"
  while IFS=$'\t' read col1 col2 col3 col4
  do
    # Only [[:alpha:]] will filter out integers on their own, but not if they are part of a string
    # Therefore the digit class check is also used.
    # What it will do with non-Latin script languages I'm not sure. (Will match chars with an umlaut...)
    if [[ $col3 =~ [[:alpha:]] ]] && ! [[ $col3 =~ [[:digit:]] ]]
    then
      # Check to see if we've already added
      # grep -nwi ${col3} deu_news_2015_10K/deu_news_2015_10K-wordz.txt > dog.txt
      var="$(grep -nwi "${col3}" "${val}/${val}-words.txt")"
      doggy="$(python ../inputs.py "${col3}" "${col4}" "${var}")"
      col3=${col3,,}
      if [[ $doggy -ne 0 ]]
      then 
        # Meaning it does have a match
        printf "%s\t%s\n" "${col3}" "${doggy}" >> "../normalized/${name}"
      else
        # This means it doesn't have match, or it's match came before it.
        # If match came before it, we skip, "False" is returned for matchless
        if [[ $doggy = "False" ]]
        then
          printf "%s\t%s\n" "${col3}" "${col4}" >> "../normalized/${name}"
        fi
      fi
      
    fi
  done < $val/*
done

# Need to re-sort the resulting tsv's if we want high-low frequency