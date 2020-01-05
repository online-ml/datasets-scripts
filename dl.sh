#!/usr/bin/env bash

# TREC07
wget https://archive.org/download/trec07p/trec07p.tgz
tar -zxvf trec07p.tgz

# Trump approval ratings from FiveThirtyEight
wget https://projects.fivethirtyeight.com/trump-approval-data/approval_polllist.csv
wget https://projects.fivethirtyeight.com/trump-approval-data/approval_topline.csv

# Phishing
wget http://archive.ics.uci.edu/ml/machine-learning-databases/00379/PhishingData.arff
