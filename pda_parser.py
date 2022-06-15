from lexical_analyzer import token, accepted_state

non_terminal = ('S', *accepted_state)
parse_table = {
    'S':{'SB':'SB VB NN'},
    'SB':{'SB':''},
    'VB':{'VB':''},
    'NN':{'NN':''}
}

def swedish_grammar_parse(sentence):
    out={'parse_text':None, 'valid':False}

    parse_text = f"{'stack':<20} | {'Input':<20}\n{'':-^43}\n"

    input = sentence.split()
    stack = []

    stack = ['S'] + stack
    parse_text+=f"{' '.join(stack):<20} | {' '.join(input):<20}\n"
    # print(f"{' '.join(stack):<20} {' '.join(input):<20}")

    try:
        while stack or input: #is not empty
            stack_top = stack.pop(0)
            if stack_top in non_terminal:
                next_token = token(input[0])
                parsed_value = parse_table[stack_top][next_token]
                parsed_value = parsed_value if parsed_value != '' else input[0]
                stack = parsed_value.split() + stack
            else:
                input.pop(0)
            parse_text+=f"{' '.join(stack):<20} | {' '.join(input):<20}\n"
            # print(f"{' '.join(stack):<20} {' '.join(input):<20}")
        parse_text+=f"{'':-^43}\n"
        out['valid'] = True
    except (KeyError, IndexError):
        parse_text+=f"{'':-^43}\n"
        parse_text+=f"{'Error':^43}\n"
    finally:
        out['parse_text']=parse_text
        print(parse_text)
    return out

if __name__ == '__main__':
    swedish_grammar_parse("jag gillar frukt")
    swedish_grammar_parse("hello world")