def is_palindrome(s):
    """s を文字列と仮定
       s が回文なら True を返し, それ以外なら False を返す
       ただし、句読点, 空白, 大文字, 小文字は無視する"""

    def to_chars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters

    def is_pal(s):
        print('  is_pal called with', s)
        if len(s) <= 1:
            print('About to return True from base case')
            return True
        else:
            answer = s[0] == s[-1] and is_pal(s[1:-1])
            print('  About to return', answer, 'for', s)
            return answer

    return is_pal(to_chars(s))

def test_is_palindrome():
    print('Try dogGod')
    print(is_palindrome('dogGod'))
    print('Try doGood')
    print(is_palindrome('doGood'))

test_is_palindrome()