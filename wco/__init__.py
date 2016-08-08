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
from collections import defaultdict

def word_count(args: tg.Tuple[tg.List[str], tg.Dict[str, tg.List]]) -> tg.Tuple[str, str, tg.Dict[str, str]]:
    """function that count the number of defined keys in given text
    using tuple to store args due to Pool's map method only support one parameter
    """
    if DEBUG:
        #print(args)
        pass
    
    row, raw_key = args

    id_, string = row
    
    result = defaultdict()
    
    for entity, entity_key in raw_key.items():
        is_match = False
        for key_type, key_list in entity_key.items():
            if key_type in ("abbreviation", "regular_expression"):
                for key in key_list:
                    match = re.search(key, string, re.UNICODE)
                    if match:
                        is_match = True
                        break
            elif key_type in ("full_name",):
                for key in key_list:
                    match = re.search(key, string, re.UNICODE + re.IGNORECASE)
                    if match:
                        is_match = True
                        break
        if is_match:
            result[entity] = match.group()

    return id_, string, result # tg.Dict[str, str]
    
DEBUG = False
NUM_PROCESS = 8
CHUNK_SIZE = 100
COOCCURENCE_THRESHOLD = 1

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

    print("Config loaded.")

    with open(text_file, 'r', encoding='utf_8') as tsvin:
        print("Text opened, processing.")
        tsv_reader = csv.reader(tsvin, delimiter='\t')
        with Pool(NUM_PROCESS) as p:
            result = p.imap_unordered(word_count, ((row, keys) for row in tsv_reader), CHUNK_SIZE)
            with open("out_1.tsv", 'w', encoding='utf_8', newline='') as outfile1, open("out_2.tsv", 'w', encoding='utf_8', newline='') as outfile2:
                tsv_writer1 = csv.writer(outfile1, delimiter='\t')
                tsv_writer2 = csv.writer(outfile2, delimiter='\t')
                for id_, original_string, result_dict in result:
                    if len(result_dict) > COOCCURENCE_THRESHOLD:
                        tsv_writer1.writerows(([id_, entity, raw_mention] for entity, raw_mention in result_dict.items()))
                        tsv_writer2.writerow([id_, original_string] + [entity for entity in result_dict])
        print("Finished. Check out_1.tsv and out_2.tsv file for result")