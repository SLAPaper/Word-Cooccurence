# Word Co-occurence

Tools to find word co-occurence in given sentences.

## Format definition

### Text input

The input text file is defining like this:

a tab seperated file(TSV):

`ID \t sentence`

### Keyword(entity) input

The keyword input can should be a json file with objects(dictionaries).

```json

{
    "keyword1": {
        "abbreviation": [
            "key1_abbr1",
            "key1_abbr2"
        ],
        "full_name": [
            "key1_form1",
            "key1_form2"
        ]
    },
    "keyword2": {
        "full_name": [
            "key2_form1",
        ],
        "regular_expression":[
            "key2_re1"
        ]
    }
}

```

### ID-Entity Output

a tab seperated file(TSV):

`ID \t keyword \t key_form`

### ID-Sentence-Entities Output

a tab seperated file(TSV):

`ID \t sentence \t keyword1, keyword2, keyword3`