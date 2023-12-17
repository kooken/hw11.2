def capital_letters(word):
    '''докстринг к старой функции'''
    word_list = list(word)
    word_in_capital = [i.upper() for i in word_list]
    print("".join(word_in_capital))

def title_letters(word):
    '''докстринг к новой функции'''
    word_title = word.title()
    print(word_title)