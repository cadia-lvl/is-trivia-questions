#!/usr/bin/env python3

import sys
import csv
import re


icelandic_alphabet = {"A","Á","B","D","Ð","E","É","F","G","H","I","Í","J","K","L","M","N","O","Ó","P","R","S","T","U","Ú","V","X","Y","Ý","Þ","Æ","Ö","a","á","b","d","ð","e","é","f","g","h","i","í","j","k","l","m","n","o","ó","p","r","s","t","u","ú","v","x","y","ý","þ","æ","ö"}

signs_and_symbols = {" ","C","c","W","w","Z","z","Q", "q","x"}
legal_chars = icelandic_alphabet | signs_and_symbols

def is_triva():

    in_file = "data_is-trivia/questions_sorted_filtered.tsv"
    out_file="data_is-trivia/questions_sorted_filtered_cleaned.tsv"

    in_file = "data_spurning-is/spuringar-is_norm.tsv"
    out_file="data_spurning-is/spuringar-is_norm_cleaned.tsv"


    illegal_chars = set()
    with open(in_file) as csvfile, open(out_file, 'w') as f_out:
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
def spurningar_is():

    in_file = "data_spurning-is/spuringar-is_norm.tsv"
    out_file="data_spurning-is/spuringar-is_norm_cleaned.tsv"

    illegal_chars = set()
    with open(in_file) as f_in, open(out_file, 'w') as f_out:
        for r in f_in:
            # Tökum burt
            r = re.sub('[\]\[(),\*☆"”’…“\:_´!\';\.„\?]','',r)

            # Skiptum út fyrir bil
            r = re.sub('[\/\-\–]',' ',r)

            # Sértækar skiptingar
            r = re.sub('đ','ð',r)
            r = re.sub('\<sil\>','',r)
            r = re.sub('[îīì]','í', r)
            r = re.sub('[ĺÎ]','Í', r)
            r = re.sub('ō', 'ö', r)
            r = re.sub('À','Á',r)
            r = re.sub('à','á', r)
            r = re.sub('[ûù]', 'ú',r)
            r = re.sub('ô', 'ó', r)
            r = re.sub('èê', 'é',r)
            # Tökum burt öll auka bil
            r = re.sub('\s+',' ', r)
            
            il_char = False
            for letter in r:      
                if letter not in legal_chars:
                    il_char=True
                    illegal_chars.add(letter)
            if il_char:
                print(r)
            f_out.write(r+'\n')
            # print(row[3])
    for x in illegal_chars:
        print(x)

if __name__ == "__main__":
    # is_triva()é
    spurningar_is()