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
import re

def word_count(args: tg.Tuple[str, tg.Dict[str, tg.List]]) -> tg.List:
    """function that count the number of defined keys in given text
    using tuple to store args due to Pool's map method only support one parameter
    """
    if DEBUG:
        print(args)

    row, keyin = args
    result = []
    id_, string = row.split('\t')
    is_match = False
    for type, keys in keys.items():
        if isMatch:
            break

        if type in ("abbreviation", "regular_expression"):
            for key in keyin.items:
                if re.search(key, string):
                    is_match = True
                    break
        elif type in ("full_name"):
            for key in keys:
                if re.search(key, string, re.IGNORECASE):
                    is_match = True
                    break
        result.append((id_, is_match))
    return result
    
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

    with open(textin, 'r', encoding='utf_8') as tsvin:
        tsv_reader = csv.reader(tsvin, delimiter='\t')
        with Pool(8) as p:
            result = p.imap(word_count, ((row, keys) for row in tsv_reader), 100)
            print([item for item in result])