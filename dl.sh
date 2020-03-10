#!/usr/bin/env bash

# MovieLens 100K
wget http://files.grouplens.org/datasets/movielens/ml-100k.zip
unzip ml-100k.zip

# TREC07
wget https://archive.org/download/trec07p/trec07p.tgz
tar -zxvf trec07p.tgz

# Trump approval ratings from FiveThirtyEight
wget https://projects.fivethirtyeight.com/trump-approval-data/approval_polllist.csv
wget https://projects.fivethirtyeight.com/trump-approval-data/approval_topline.csv

# Phishing
wget http://archive.ics.uci.edu/ml/machine-learning-databases/00379/PhishingData.arff

# Segment
wget https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/segment/segment.dat
