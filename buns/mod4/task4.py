def palindrom(word):
    for i in range(len(word)):
        if word[i] == word[len(word) - i - 1]:
            continue
            #print(word[i], end=' ')
        else:
            print('Не палиндром')
            break
    else: print('Палиндром')

word = input('Введите слово для проверки: ')
palindrom(word)