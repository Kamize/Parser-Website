from cv2 import ORB_FAST_SCORE
from lexical_analyzer import token, accepted_state

non_terminal = ('S', *accepted_state)
parse_table = {
    'S':{'SB':'SB VB NN'},
    'SB':{'SB':''},
    'VB':{'VB':''},
    'NN':{'NN':''}
}

def swedish_grammar_parse(sentence):

    input = sentence.split()
    stack = []

    stack = ['S'] + stack

    try:
        while stack: #is not empty
            stack_top = stack.pop(0)
            if stack_top in non_terminal:
                next_token = token(input[0])
                parsed_value = parse_table[stack_top][next_token]
                parsed_value = parsed_value if parsed_value != '' else input[0]
                stack = parsed_value.split() + stack
            else:
                input.pop(0)
            # print(f"{' '.join(stack):<20}")
            # print(f"{' '.join(input):>20}")
            print(f"{' '.join(stack):<20} {' '.join(input):>20}")
    except KeyError:
        pass
    except IndexError:
        pass

if __name__ == '__main__':
    swedish_grammar_parse("jag gillar frukt")