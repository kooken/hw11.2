def capital_letters(word):
    word_list = list(word)
    word_in_capital = [i.upper() for i in word_list]
    print("".join(word_in_capital))

#capital_letters(input())

def up_string(input):
    return input.upper()

up_string("word")