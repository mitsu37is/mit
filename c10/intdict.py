class IntDict(object):
    """整数をキーとする辞書"""

    def __init__(self, numbuckets):
        """空の辞書を生成する"""
        self.buckets = []
        self.numbuckets = numbuckets
        for i in range(numbuckets):
            self.buckets.append([])

    def addentry(self, key, dictval):
        """key を int 型としエントリを追加する"""
        # 入れ物を剰余で分類している
        hashbucket = self.buckets[key % self.numbuckets]
        for i in range(len(hashbucket)):
            # すでに存在する key であれば、値を更新する。
            if hashbucket[i][0] == key:
                hashbucket[i] = (key, dictval)
                return
        hashbucket.append((key, dictval))

    def getvalue(self, key):
        """key を int 型とする
           キー key に関連づけられた値を返す"""
        hashbucket = self.buckets[key % self.numbuckets]
        for e in hashbucket:
            if e[0] == key:
                return e[1]
        return None

    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}'

def test_intdict():
    import random
    D = IntDict(17)
    for i in range(20):
        key = random.choice(range(10**5))
        D.addentry(key, i)
    print('The value of the intDict is: ')
    print(D)
    print('\n', 'The buckets are: ')
    for hashbucket in D.buckets:
        print('  ', hashbucket)

test_intdict()