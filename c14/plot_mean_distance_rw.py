import pylab
from location import Location
from field import Field
from usual_drunk import UsualDrunk
from cold_drunk import ColdDrunk
from ew_drunk import EWDrunk
from style_iterator import styleIterator

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

def sim_drunk(num_trials, d_class, walk_length):
    mean_distances = []
    for num_steps in walk_length:
        print('Starting simulation of', num_steps, 'steps')
        trials = sim_walks(num_steps, num_trials, d_class)
        mean = sum(trials)/len(trials)
        mean_distances.append(mean)
    return mean_distances

def sim_all1(drunk_kinds, walk_length, num_trials):
    style_choice = styleIterator(('m-', 'r:', 'k-.'))
    for d_class in drunk_kinds:
        cur_style = style_choice.next_style()
        print('Starting simulation of', d_class.__name__)
        means = sim_drunk(num_trials, d_class, walk_length)
        pylab.plot(walk_length, means, cur_style, label=d_class.__name__)
    pylab.title('Mean Distance from Origin (' + str(num_trials) + 'trials )')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc='best')
    pylab.semilogx()
    pylab.semilogy()
    pylab.savefig('random_walk/mean_distance_rw')


pylab.style.use('seaborn-darkgrid')
sim_all1((UsualDrunk, ColdDrunk, EWDrunk), (10, 100, 1000, 10000, 100000), 100)