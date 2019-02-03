import random
import pylab

def flip_plot(min_exp, max_exp):
    ratios, diffs, x_axis = [], [], []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2**exp)
    for num_flips in x_axis:
        num_heads = 0
        for n in range(num_flips):
            if random.choice(('H', 'T')) == 'H':
                num_heads += 1
        num_tails = num_flips - num_heads
        try:
            ratios.append(num_heads/num_tails)
            diffs.append(abs(num_heads - num_tails))
        except ZeroDivisionError:
            continue
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.semilogx()
    pylab.semilogy()
    pylab.plot(x_axis, diffs, 'o')
    pylab.savefig('toss_coin/diffs_toss_coin')
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of flips')
    pylab.ylabel('#Heads/#Tails')
    pylab.semilogx()
    pylab.semilogy()
    pylab.plot(x_axis, ratios, 'o')
    pylab.savefig('toss_coin/ratios_toss_coin')


random.seed(0)
pylab.style.use('seaborn-darkgrid')
flip_plot(4, 20)