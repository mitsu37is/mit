def search(L, e):
    """L を要素が昇順で並んだリストとする
       e が L にあれば True を、そうでなければ False を返す"""

    def bsearch(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (high + low) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bsearch(L, e, low, mid - 1)
        else:
            return bsearch(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bsearch(L, e, 0, len(L) - 1)

def test_bsearch():
    print('Is 4 in [1,2,3,5,6,7,9,10] ?')
    print(search([1,2,3,5,6,7,9,10], 4))
    print('Is 7 in [1,2,3,5,6,7,9,10] ?')
    print(search([1, 2, 3, 5, 6, 7, 9, 10], 7))

test_bsearch()