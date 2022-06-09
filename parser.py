from lexical_analyzer import token

text = input("word to analyze: ")
print("token: ", end='')
for word in text.lower().split():
    print(token(word), end=' ')
print()
