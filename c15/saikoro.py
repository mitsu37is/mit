import pylab
import scipy.special

def n2_probable(k):
    a = scipy.special.comb(k, 2, exact=True)
    return a * (1/6)**2 * (5/6)**(k-2)

def make_plot(x_vals, y_vals, title, x_label, y_label, style):
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.plot(x_vals, y_vals, style)

def throw_dice(k):
    x_vals, y_vals = [], []
    for i in range(2, k+1):
        x_vals.append(i)
        y_vals.append(n2_probable(i))
    make_plot(x_vals, y_vals, 'The Probability of Getting 3 Exactly Twice', 'number of roll die', 'probability', '-')
    pylab.savefig('rolldie/probabilityof3')


pylab.style.use('seaborn-darkgrid')
throw_dice(100)
