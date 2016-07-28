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
        keys = {
            "key1": ["key1form1", "keyform2"], 
            "key2": ["key2form1",],
            "key3": None
            }
    else:
        if len(sys.argv) < 3:
            print("Not enough parameters", file=sys.stderr)
            sys.exit(1)
        else:
            textin = sys.argv[1]
            with open(sys.argv[2], 'r', encoding='utf_8') as keyin:
                keys = json.load(keyin)

    with Pool(8) as p:
        result = p.map(word_count, ((textin, item) for item in keys.items()))
        print([item for item in result])