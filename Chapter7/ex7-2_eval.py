def ask_user():
    val = input('Insert a value, enter "done" to exit: ')
    if val != 'done':
        print(eval(val))
        ask_user()

ask_user()
