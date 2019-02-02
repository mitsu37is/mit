import pylab
from location import Location
from odd_field import oddField
from usual_drunk import UsualDrunk
from cold_drunk import ColdDrunk
from ew_drunk import EWDrunk
from style_iterator import styleIterator

def trace_walk(drunk_kinds, num_steps):
    style_choice = styleIterator(('+', '^', 'o'))
    f = oddField(1000, 100, 200)
    for d_class in drunk_kinds:
        d = d_class()
        f.add_drunk(d, Location(0, 0))
        locs = []
        for s in range(num_steps):
            f.move_drunk(d)
            locs.append(f.get_loc(d))
        x_vals, y_vals = [], []
        for loc in locs:
            x_vals.append(loc.get_x())
            y_vals.append(loc.get_y())
        cur_style = style_choice.next_style()
        pylab.plot(x_vals, y_vals, cur_style, label=d_class.__name__)
    pylab.title('Spots Visited on Walk (' + str(num_steps) + ' steps )')
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps North_South of Origin')
    pylab.legend(loc='best')
    pylab.savefig('random_walk/trace_odd_rw')

pylab.style.use('seaborn-darkgrid')
trace_walk((UsualDrunk, ColdDrunk, EWDrunk), 500)