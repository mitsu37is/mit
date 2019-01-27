def merge(left, right, compare):
    """left と right をソート済みのリストとし、
       compare を要素間の順序を定義する関数とする
       (left + right) を同じ要素からなり
       compare にしたがってソートされた新たなリストを返す"""

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def mergesort(L, compare = lambda x, y: x < y):
    """L をリストとし
       compare を L の要素間の順序を定義する関数とする
       L と同じ要素からなりソートされた新たしいリストを返す"""
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = mergesort(L[:middle], compare)
        right = mergesort(L[middle:], compare)
        return merge(left, right, compare)

def test_mergesort():
    print('[2, 1, 4, 5, 3]')
    print(mergesort([2, 1, 4, 5, 3]))
    print('[2, 1, 4, 5, 3], compare = lambda x, y: x > y')
    print(mergesort([2, 1, 4, 5, 3], lambda x, y: x > y))

test_mergesort()