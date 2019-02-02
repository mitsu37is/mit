from location import Location
from field import Field
from usual_drunk import UsualDrunk
from cold_drunk import ColdDrunk
from ew_drunk import EWDrunk

def walk(f, d, num_steps):
    """f:Field クラスのオブジェクト
       d:Drunk クラスのオブジェクト
       num_steps: 0 以上の整数
       d を num_steps 回移動し、初期位置と最終位置との差を出力する"""
    start = f.get_loc(d)
    for s in range(num_steps):
        f.move_drunk(d)
    return start.dist_from(f.get_loc(d))

def sim_walks(num_steps, num_trials, d_class):
    """num_steps: 0 以上の整数
       num_trials: 正の整数
       d_class: Drunk のサブクラス
       「d を num_steps 回移動し、初期位置と最終位置との差」を num_trials 回計算し
       各計算の結果をリストにして出力する"""
    homer = d_class()
    origin = Location(0, 0)
    distances = []
    for t in range(num_trials):
        f = Field()
        f.add_drunk(homer, origin)
        distances.append(round(walk(f, homer, num_steps), 1))
    return distances

def drunkTest(walk_length, num_trials, d_class):
    """walk_length: 0 以上の整数のシークエンス
       num_trials: 正の整数
       d_class: Drunk のサブクラス
       walk_length の各要素を移動回数として、num_trials 回の試行を
       シミュレートする sim_walks を実行し、結果を出力する"""
    for num_steps in walk_length:
        distances = sim_walks(num_steps, num_trials, d_class)
        print(d_class.__name__, 'random walk of', num_steps, 'steps')
        print(' Mean = ', round(sum(distances)/len(distances), 4))
        print(' Max = ', max(distances), 'Min = ', min(distances))

def sim_all(drunk_kinds, walk_length, num_trials):
    for d_class in drunk_kinds:
        drunkTest(walk_length, num_trials, d_class)

sim_all((UsualDrunk, ColdDrunk, EWDrunk), (100, 1000), 10)