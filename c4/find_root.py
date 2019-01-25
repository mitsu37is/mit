def find_root(x, power, epsilon):
    """x と epsilon > 0 は整数もしくは浮動小数点数, power>=1 を整数と仮定
       y**power が x の epsilon 以内になるような 浮動小数点数 y を返す
       もしそのような y が存在しなければ None を返す"""
    if x < 0 and power % 2 == 0:
        return None
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high + low) / 2.0
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans

def test_find_root():
    epsilon = 0.0001
    for x in (0.25, -0.25, 2, -2, 8, -8):
        for power in range(1, 4):
            print('Testing x = ', str(x), 'and power = ', power)
            result = find_root(x, power, epsilon)
            if result is None:
                print('No root')
            else:
                print(' ', result**power, '~=', x)
