import pylab
from location import Location
from field import Field
from usual_drunk import UsualDrunk
from cold_drunk import ColdDrunk
from ew_drunk import EWDrunk
from style_iterator import styleIterator

def get_final_locs(num_steps, num_trials, d_class):
    locs = []
    d = d_class()
    for t in range(num_trials):
        f = Field()
        f.add_drunk(d, Location(0, 0))
        for s in range(num_steps):
            f.move_drunk(d)
        locs.append(f.get_loc(d))
    return locs

def plot_locs(drunk_kinds, num_steps, num_trials):
    style_choice = styleIterator(('+', '^', 'o'))
    for d_class in drunk_kinds:
        locs = get_final_locs(num_steps, num_trials, d_class)
        x_vals, y_vals = [], []
        for loc in locs:
            x_vals.append(loc.get_x())
            y_vals.append(loc.get_y())
        mean_x = sum(x_vals)/len(x_vals)
        mean_y = sum(y_vals)/len(y_vals)
        cur_style = style_choice.next_style()
        pylab.plot(x_vals, y_vals, cur_style, label=d_class.__name__+' mean loc = <'+str(mean_x)+', '+str(mean_y)+'>' )
        pylab.title('Location at the End of Walks (' + str(num_steps) + 'steps )')
        pylab.xlabel('Steps East/West of Origin')
        pylab.ylabel('Steps North_South of Origin')
        pylab.legend(loc='lower left')
        pylab.savefig('random_walk/final_loc_rw')

pylab.style.use('seaborn-darkgrid')
plot_locs((UsualDrunk, ColdDrunk, EWDrunk), 100, 200)