import re
import spacy # Spacy is a robust NLP library that lets us use their pre-trained models

nlp = spacy.load('en_core_web_trf') # We chose this model for its higher NER performance

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