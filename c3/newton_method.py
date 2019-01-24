# 平方根を見つけるためのニュートン法
epsilon = 0.01
k = int(input('enter a number you like.'))
numGuess = 0
guess = k / 2.0
while abs(guess*guess -k) >= epsilon:
    print('guess is', guess)
    numGuess += 1
    guess = guess - (((guess**2) - k)/(2*guess))
print('numGuesses =', numGuess)
print('Square root of', k, 'is about', guess)