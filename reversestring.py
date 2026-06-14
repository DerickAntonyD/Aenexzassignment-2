def r(text):
    if len(text) == 0:
        return text

    return r(text[1:]) + text[0]

s = input()
print(r(s))
