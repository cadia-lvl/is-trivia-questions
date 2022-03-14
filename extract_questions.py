#!/usr/bin/env python3

import csv
import sys
import pandas as pd



def main():
    questions_csv = sys.argv[1]
    df = pd.read_csv(questions_csv, header=None)
    questions =df[4].to_list()
    with open('questions.txt', 'w') as f_out: f_out.write('\n'.join(questions))

if __name__ == '__main__':
    main()