import urwid

def is_very_long(password):
    return len(password) > 12

def has_digits(password):
    return any(symbol.isdigit() for symbol in password)

def has_letters(password):
    return any(symbol.isalpha() for symbol in password)

def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)

def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)

def has_symbols(password):
    return any((not symbol.isdigit() and not symbol.isalpha()) for symbol in password)

def doesnt_consist_of_symbols(password):
    return not(all(not symbol.isalnum() for symbol in password))

def get_score(password):
    score = 0
    functions = [has_digits, is_very_long, has_letters,
                 has_upper_letters, has_lower_letters,
                 has_symbols, doesnt_consist_of_symbols]
    for func in functions:
        if func(password):
            score += 2
    return score

def main():
    def on_ask_change(edit, new_edit_text):
        reply.set_text('Password rating is %s of 14' % (get_score(new_edit_text)))

    ask = urwid.Edit('Enter a password: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()

if __name__ == '__main__':
    main()