def isIn(x, y):
    if x in y or y in x:
        return True
    else:
        return False

print(isIn('qwe', 'wer'))
print(isIn('qwe', 'qwerty'))
print(isIn('qwerty', 'qwe'))
print(isIn('wer', 'qwe'))