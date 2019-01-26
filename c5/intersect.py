def intersect(t1, t2):
    """t1 と t2 はタプルであると仮定する
       t1 と t2 両方に入っている要素を含むタプルを返す"""
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result

def test_intersect():
    print('t1 = (1, two, 3), t2 = (one, two, 3)')
    print('intersect => ', intersect((1, 'two', 3), ('one', 'two', 3)))

test_intersect()