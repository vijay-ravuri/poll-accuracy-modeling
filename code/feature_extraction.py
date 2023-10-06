import re
# Spacy is a robust NLP library that provides pre-trained models.
from spacy import load as load_spacy 
import numpy as np

nlp = load_spacy('en_core_web_trf') # We chose this model for its higher NER performance

def person_flag(list): # Used internally for person_finder
    for tup in list:
        if tup[0] == 'PERSON':
            return 1
    return 0

def person_finder(text): # Returns 1 if the comment includes a person, 0 otherwise
    text = re.sub(r'(\d+)', '', text)
    doc = nlp(text)

    ents = [(ent.label_, ent.text) for ent in doc.ents]

    return person_flag(ents)

def org_flag(list): # Used internally for org_finder
    for tup in list:
        if tup[0] == 'ORG':
            return 1
    return 0

def org_finder(text): # Returns 1 if the comment includes an organization, 0 otherwise
    text = re.sub(r'(\d+)', '', text)
    doc = nlp(text)

    ents = [(ent.label_, ent.text) for ent in doc.ents]

    return org_flag(ents)

def state_agg(state_code): # Records a few locations to their respective state
    map = {
        'N2' : 'NE',
        'M1' : 'ME',
        'M2' : 'ME'
    }

    if state_code in ['N2', 'M1', 'M2']:
        return map[state_code]
    else:
        return state_code
    
def imputed_checker(text): # used for imputed_600 column
    if text is not np.nan:
        return 1 if 'sample size unavailable' in text else 0
    return 0

def sample_size(num): # for consistency's sake for imputed_600
    if num == 600:
        return 1
    else:
        return 0
    
def imputed_600(df): # returns 1 for columns that were imputed with samplesize = 600
    return df['samplesize'].apply(sample_size) * df['comment'].apply(imputed_checker)