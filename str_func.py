def capital_letters(word):
    '''описание функции'''
    word_list = list(word)
    word_in_capital = [i.upper() for i in word_list]
    print("".join(word_in_capital))
