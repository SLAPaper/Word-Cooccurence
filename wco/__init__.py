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

def word_count(args: tg.Tuple[tg.List[str], tg.Dict[str, tg.List]]) -> tg.List:
    """function that count the number of defined keys in given text
    using tuple to store args due to Pool's map method only support one parameter
    """
    if DEBUG:
        print(args)
        pass
    
    row, raw_key = args

    result = []
    id_, string = row
    for entity, entity_key in raw_key.items():
        is_match = False
        for key_type, key_list in entity_key.items():
            if is_match:
                break
    
            if key_type in ("abbreviation", "regular_expression"):
                for key in key_list:
                    if re.search(key, string):
                        is_match = True
                        break
            elif type in ("full_name",):
                for key in key_list:
                    if re.search(key, string, re.IGNORECASE):
                        is_match = True
                        break

        result.append((id_, entity, is_match))

    return result
    
DEBUG = True

if __name__ == "__main__":
    if DEBUG:
        text_file = "TEST.tsv"
        with open("TEST.json", 'r', encoding='utf_8') as keyin:
            keys = json.load(keyin)
        pass
    else:
        if len(sys.argv) < 3:
            sys.exit("Not enough parameters")
        else:
            text_file = sys.argv[1]
            with open(sys.argv[2], 'r', encoding='utf_8') as keyin:
                keys = json.load(keyin)

    with open(text_file, 'r', encoding='utf_8') as tsvin:
        tsv_reader = csv.reader(tsvin, delimiter='\t')
        with Pool(8) as p:
            result = p.imap_unordered(word_count, ((row, keys) for row in tsv_reader), 100)
            print([item for item in result])