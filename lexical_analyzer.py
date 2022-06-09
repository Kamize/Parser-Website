#Lexical Analyzer to identify lexical
accepted_state = ['SB', 'VB', 'NN']
transition_table = {
    'q0':{
        'j':'q1',
        'd':'q2',
        'h':'q3',
        'k':'q4',
        'ä':'q5',
        'g':'q6',
        'f':'q7'
    },
    'q1':{'a':'q8'},
    'q2':{'u':'SB'},
    'q3':{
        'a':'q9',
        'o':'q10'
    },
    'q4':{
        'ö':'q11',
        'e':'q16'
    },
    'q5':{
        'l':'q12',
        't':'q13'
    },
    'q6':{
        'i':'q14',
        'o':'q17'
    },
    'q7':{'r':'q15'},
    'q8':{'g': 'SB'},
    'q9':{'n':'SB'},
    'q10':{'n':'SB'},
    'q11':{
        'p':'q18',
        't':'q20'
    },
    'q12':{'j':'q19'},
    'q13':{'e':'q27'},
    'q14':{'l':'q21'},
    'q15':{'u':'q22'},
    'q16':{'x':'NN'},
    'q17':{'d':'q23'},
    'q18':{'e':'q27'},
    'q19':{'e':'q27'},
    'q20':{'t':'NN'},
    'q21':{'l':'q24'},
    'q22':{'k':'q25'},
    'q23':{'i':'q26'},
    'q24':{'a':'q28'},
    'q25':{'t':'NN'},
    'q26':{'s':'NN'},
    'q27':{'r':'VB'},
    'q28':{'r':'VB'}
}

def token(word):
    state = 'q0'
    try:
        for char in word.lower():
                # print(state)
                # print(char)
                state = transition_table[state][char]
    except KeyError:
        state = 'error'
    state = 'error' if state not in accepted_state else state
    return state









    

def sentence_to_tokens(sentence):
    tokens = []
    for word in sentence.lower().split():
        tokens.append(token(word))
    return tokens


def test():
    sentence = input("word to analyze: ")
    tokens = sentence_to_tokens(sentence)
    print("tokens: ", end='')
    for token in tokens:
        print(token, end=' ')
    print()

if __name__ == '__main__':
    test()