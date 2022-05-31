#!/usr/bin/env python3

import sys
import csv
import re


icelandic_alphabet = {"A","Á","B","D","Ð","E","É","F","G","H","I","Í","J","K","L","M","N","O","Ó","P","R","S","T","U","Ú","V","X","Y","Ý","Þ","Æ","Ö","a","á","b","d","ð","e","é","f","g","h","i","í","j","k","l","m","n","o","ó","p","r","s","t","u","ú","v","x","y","ý","þ","æ","ö"}

signs_and_symbols = {" ","C","c","W","w","Z","z","Q", "q","x"}
legal_chars = icelandic_alphabet | signs_and_symbols

def is_triva():

    in_file = "is-triva/questions_sorted_filtered.tsv"
    out_file="is-triva/isquestions_sorted_filtered_cleaned.tsv"
    illegal_chars = set()
    with open(file) as csvfile, open(out_file, 'w') as f_out:
        csvreader = csv.reader(csvfile, delimiter="\t")
        for row in csvreader:
            r = row[3]

            # Tökum burt
            r = re.sub('[(),"\:_´!\';\.„\?]','',r)

            # Skiptum út fyrir bil
            r = re.sub('[\/-]',' ',r)
            r = re.sub('\s+',' ', r)
            row[3] = r
            il_char = False
            for letter in row[3]:
                        
                if letter not in legal_chars:
                    il_char=True
                    illegal_chars.add(letter)
            if il_char:
                print(row[3])
            f_out.write('\t'.join(row)+'\n')
            # print(row[3])
    for x in illegal_chars:
        print(x)

if __name__ == "__main__":
    is_triva()
