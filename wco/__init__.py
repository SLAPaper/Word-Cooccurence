"""Word Co-occurence finder tool
"""
import os
import sys
import mmap
import json
import typing as tg
from multiprocessing import Pool
import csv
import pdb

def word_count(args: tg.Tuple[str, tg.Dict]) -> tg.List:
    if DEBUG:
        print(args)

    textin = args[0]
    key = args[1]

    with open(textin, 'r', encoding='utf_8') as tsvin:
        tsv_reader = csv.reader(tsvin, delimiter='\t')
        text = [row for row in tsv_reader]
    return len(text)
    
DEBUG = True

if __name__ == "__main__":
    if DEBUG:
        textin = "TEST.tsv"
        with open("TEST.json", 'r', encoding='utf_8') as keyin:
            keys = json.load(keyin)
    else:
        if len(sys.argv) < 3:
            sys.exit("Not enough parameters")
        else:
            textin = sys.argv[1]
            with open(sys.argv[2], 'r', encoding='utf_8') as keyin:
                keys = json.load(keyin)

    with Pool(8) as p:
        result = p.map(word_count, ((textin, item) for item in keys.items()))
        print([item for item in result])