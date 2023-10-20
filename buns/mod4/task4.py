def check_palindrome(word):
    letter_counts = {}
    palindrome = ''
    middle = ''
    
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    
    for letter in letter_counts:
        if letter_counts[letter] % 2 == 0:
            palindrome += letter * (letter_counts[letter] // 2)
        elif letter_counts[letter] == 1:
            if middle == '':
                middle = letter
            else:
                print('Нельзя составить палиндром')
                return
        else:
            if middle == '':
                middle = letter
                palindrome += letter * ((letter_counts[letter] - 1) // 2)
            else:
                print('Нельзя составить палиндром')
                return
    
    if middle != '':
        print(palindrome + middle + palindrome[::-1])
    else:
        print(palindrome + palindrome[::-1])

word = input('Введите слово для проверки: ')
check_palindrome(word)
