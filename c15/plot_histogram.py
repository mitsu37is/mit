import pylab
import random

def variance(X):
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return tot/len(X)

def std_dev(X):
    return variance(X) ** 0.5

def flip(num_flips):
    heads = 0
    for i in range(num_flips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads/float(num_flips)

def flip_sim(num_flips_per_trial, num_trials):
    frac_heads = []
    for i in range(num_trials):
        frac_heads.append(flip(num_flips_per_trial))
    mean = sum(frac_heads)/len(frac_heads)
    sd = std_dev(frac_heads)
    return (frac_heads, mean, sd)

def label_plot(num_flips, num_trials, mean, sd):
    pylab.title(str(num_trials) + 'trials of ' + str(num_flips) + ' flips each')
    pylab.xlabel('Fraction of heads')
    pylab.ylabel('Number of Trials')
    pylab.annotate('Mean = ' + str(round(mean, 4)) + '\nSD = ' + str(round(sd, 4)), size='x-large', xycoords='axes fraction', xy=(0.67, 0.5))

def make_plots(num_flips1, num_flips2, num_trials):
    val1, mean1, sd1 = flip_sim(num_flips1, num_trials)
    pylab.hist(val1, bins=20)
    xmin, xmax = pylab.xlim()
    label_plot(num_flips1, num_trials, mean1, sd1)
    pylab.savefig('toss_coin/mean_100toss')

    pylab.figure()
    val2, mean2, sd2 = flip_sim(num_flips2, num_trials)
    pylab.hist(val2, bins=20)
    pylab.xlim(xmin, xmax)
    label_plot(num_flips2, num_trials, mean2, sd2)
    pylab.savefig('toss_coin/mean_1000toss')


make_plots(100, 1000, 100000)