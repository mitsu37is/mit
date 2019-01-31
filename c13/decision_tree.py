class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', ' + str(self.weight) + '>'
        return result


def decision_tree(to_consider, avail, memo={}):
    """to_consider は品物のリスト, avail は重さ
       memo は再帰位呼び出しによってのみ使われるとする
       それらをパラメータとする0/1ナップサック問題の解である、総価値と品物の
       リストからなるタプルを返す"""

    if(len(to_consider), avail) in memo:
        result = memo[(len(to_consider)), avail]
    elif to_consider == [] or avail == 0:
        result = (0, ())
    elif to_consider[0].get_weight() > avail:
        result = decision_tree(to_consider[1:], avail, memo)
    else:
        next_item = to_consider[0]
        with_val, with_to_take = decision_tree(to_consider[1:], avail - next_item.get_weight(), memo)
        with_val += next_item.get_value()

        without_val, without_to_take = decision_tree(to_consider[1:], avail, memo)

        if with_val > without_val:
            result = (with_val, with_to_take + (next_item,))
        else:
            result = (without_val, without_to_take)
    memo[(len(to_consider), avail)] = result
    return result

import random
def small_test():
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    items = []
    for i in range(len(vals)):
        items.append(Item(names[i], vals[i], weights[i]))
    val, taken = decision_tree(items, 5)
    for item in taken:
        print(item)
    print('Total value of items taken =', val)

def build_many_items(num_items, max_val, max_weight):
    items = []
    for i in range(num_items):
        items.append(Item(str(i), random.randint(1, max_val), random.randint(1, max_weight)))
    return items

def big_test(num_items):
    items = build_many_items(num_items, 10, 10)
    val, taken = decision_tree(items, 40)
    print('Items taken')
    for item in taken:
        print(item)
    print('Total value of items taken =', val)


big_test(256)
