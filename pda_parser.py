from lexical_analyzer import token, accepted_state

non_terminal = ('S', *accepted_state)
parse_table = {
    'S':{'SB':'SB VB NN'},
    'SB':{'SB':''},
    'VB':{'VB':''},
    'NN':{'NN':''}
}

def swedish_grammar_parse(sentence):
    out={'valid':False, 'parse_text':None, 'parse_stack':None, 'parse_input':None}

    parse_text = f"{'stack':<22} | {'Input':<22}\n{'':-^43}\n"
    parse_stack = ''
    parse_input = ''

    input = sentence.split()
    stack = []

    stack = ['S'] + stack
    parse_text+=f"{{{' '.join(stack):<20}}} | {{{' '.join(input):<20}}}\n"
    parse_stack+=f"{{{' '.join(stack)}}}\n"
    parse_input+=f"{{{' '.join(input)}}}\n"
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
            parse_text+=f"{{{' '.join(stack):<20}}} | {{{' '.join(input):<20}}}\n"
            parse_stack+=f"{{{' '.join(stack)}}}\n"
            parse_input+=f"{{{' '.join(input)}}}\n"
            # print(f"{' '.join(stack):<20} {' '.join(input):<20}")
        # parse_text+=f"{{{' '.join(stack):<20}}} | {{{' '.join(input):<20}}}\n"
        # parse_stack+=f"{{{' '.join(stack)}}}\n"
        # parse_input+=f"{{{' '.join(input)}}}\n"
        parse_text+=f"{'':-^43}\n"
        out['valid'] = True
    except (KeyError, IndexError):
        parse_text+=f"{'':-^43}\n"
    finally:
        out['parse_text']=parse_text
        out['parse_stack']=parse_stack
        out['parse_input']=parse_input
    return out

if __name__ == '__main__':
    print(swedish_grammar_parse("jag gillar frukt")['parse_text'])
    print(swedish_grammar_parse("hello world")['parse_text'])