def ask_user():
    print('original number:')
    number = int(input())
    print('divisor')
    is_correct = False
    while not is_correct:
        try:
            divisor = int(input())
            is_correct = True
        except ValueError:
            print('zadaj korektne cislo')