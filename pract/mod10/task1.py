import re

def check_password(password):
    """
    Эта функция проверяет, является ли входная строка допустимым паролем в соответствии с данными ограничениями.

    Args:
    password (str): Строка, представляющая собой пароль.

    Returns:
    bool: True если входная строка является допустимым паролем, False в противном случае.
    
    >>> check_password('rtG&3FG#Tr^e')
    True
    >>> check_password('a^A1@*@1Aa')
    True
    >>> check_password('oF^a1D@y5%e6')
    True
    >>> check_password('enroi#$*rkdeR#$*092uwedchf34tguv394h')
    True
    >>> check_password('пароль')
    False
    >>> check_password('password')
    False
    >>> check_password('qwerty')
    False
    >>> check_password('lOngPa$$W0Rd')
    False
    """

    regex = r'^(?=.*[a-zA-Z]{2,}?)(?!.*[.,!?])(?=.*\d)(?=(?:.*[$%@#&^*]){3,}?).{8,}$'
    if re.match(regex, password) and len(set(re.findall(r'[$%@#&^*]', password))) >= 3:
        return True
    else:
        return False

if __name__ == "__main__":
    import doctest
    result = doctest.testmod(verbose=True)

    if result.failed == 0:
        print("Все тесты прошли успешно!")
    else:
        print("Тесты не прошли.")
        

print(check_password('rtG&3FG#Tr^e'))
#True
print(check_password('a^A1@*@1Aa'))
#True
print(check_password('oF^a1D@y5%e6'))
#True
print(check_password('enroi#$*rkdeR#$*092uwedchf34tguv394h'))
#True
print(check_password('lOngPa%*$W0Rd'))
#True

print()

print(check_password('пароль'))
#False
print(check_password('password'))
#False
print(check_password('qwerty'))
#False
print(check_password('lOngPa$$W0Rd'))
#False
print(check_password('lOngPa?$W0Rd'))
#False
