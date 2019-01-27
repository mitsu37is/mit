def selsort(L):
    """L を > を用いて比較できる要素からなるリストとする
       L を昇順にソートする"""
    suffixStart = 0
    while suffixStart != len(L):
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1
    return L

def test_selsort():
    print('[2, 4, 3, 1, 5]')
    print(selsort([2, 4, 3, 1, 5]))

test_selsort()