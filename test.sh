#!/bin/bash

# mkdir tars
# mkdir frequencies
# python grab_data.py

# # Unpack tarballs and put them in a frequencies directory
# cd tars/
# for tarball in *
# do
#   stem=${tarball/.*}
#   freq_file_path="${stem}/${stem}-words.txt"
#   tar -C ../frequencies -xzf "$tarball" "$freq_file_path"
# done
# cd ..



# for val in frequencies/*/*
# do
#   python inputs.py $val
# done


# rm -rf tars
# rm -rf frequencies


curl -f -o tars/aze_newscrawl_2013_1M http://pcai056.informatik.uni-leipzig.de/downloads/corpora/aze_newscrawl_2013_1M.tar.gz

curl -f -o tars/bak_news_2016_300K http://pcai056.informatik.uni-leipzig.de/downloads/corpora/bak_news_2016_300K.tar.gz

curl -f -o tars/cat_newscrawl_2016_1M http://pcai056.informatik.uni-leipzig.de/downloads/corpora/cat_newscrawl_2016_1M.tar.gz

curl -f -o tars/ces_news_2005-2007_1M http://pcai056.informatik.uni-leipzig.de/downloads/corpora/ces_news_2005-2007_1M.tar.gz

curl -f -o tars/fao-fo_web_2015_1M http://pcai056.informatik.uni-leipzig.de/downloads/corpora/fao-fo_web_2015_1M.tar.gz

curl -f -o tars/kat_newscrawl_2016_1M http://pcai056.informatik.uni-leipzig.de/downloads/corpora/kat_newscrawl_2016_1M.tar.gz

curl -f -o tars/deu_news_2015_1M http://pcai056.informatik.uni-leipzig.de/downloads/corpora/deu_news_2015_1M.tar.gz

curl -f -o tars/ell-gr_web_2015_1M http://pcai056.informatik.uni-leipzig.de/downloads/corpora/ell-gr_web_2015_1M.tar.gz

curl -f -o tars/hin_news_2011_1M http://pcai056.informatik.uni-leipzig.de/downloads/corpora/hin_news_2011_1M.tar.gz

curl -f -o tars/ita_news_2010_1M http://pcai056.informatik.uni-leipzig.de/downloads/corpora/ita_news_2010_1M.tar.gz

curl -f -o tars/jpn_news_2011_1M http://pcai056.informatik.uni-leipzig.de/downloads/corpora/jpn_news_2011_1M.tar.gz

curl -f -o tars/kor_news_2007_1M http://pcai056.informatik.uni-leipzig.de/downloads/corpora/kor_news_2007_1M.tar.gz

curl -f -o tars/kur_newscrawl_2011_30K http://pcai056.informatik.uni-leipzig.de/downloads/corpora/kur_newscrawl_2011_30K.tar.gz

curl -f -o tars/lav-lv_web_2015_1M http://pcai056.informatik.uni-leipzig.de/downloads/corpora/lav-lv_web_2015_1M.tar.gz

curl -f -o tars/dsb_wikipedia_2016_10K http://pcai056.informatik.uni-leipzig.de/downloads/corpora/dsb_wikipedia_2016_10K.tar.gz

curl -f -o tars/ltz-lu_web_2013_1M http://pcai056.informatik.uni-leipzig.de/downloads/corpora/ltz-lu_web_2013_1M.tar.gz

curl -f -o tars/mkd-mk_web_2015_1M http://pcai056.informatik.uni-leipzig.de/downloads/corpora/mkd-mk_web_2015_1M.tar.gz

curl -f -o tars/mlt_web_2012_300K http://pcai056.informatik.uni-leipzig.de/downloads/corpora/mlt_web_2012_300K.tar.gz

curl -f -o tars/por_newscrawl_2016_1M http://pcai056.informatik.uni-leipzig.de/downloads/corpora/por_newscrawl_2016_1M.tar.gz

curl -f -o tars/rus_news_2010_1M http://pcai056.informatik.uni-leipzig.de/downloads/corpora/rus_news_2010_1M.tar.gz

curl -f -o tars/spa_news_2011_1M http://pcai056.informatik.uni-leipzig.de/downloads/corpora/spa_news_2011_1M.tar.gz

