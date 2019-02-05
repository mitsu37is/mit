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
    pylab.plot(x_axis, ratios, 'o')
    pylab.savefig('toss_coin/ratios_toss_coin')


def variance(X):
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return tot/len(X)

def std_dev(X):
    return variance(X) ** 0.5

def make_plot(x_vals, y_vals, title, x_label, y_label, style, log_x=False, log_y=False):
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.plot(x_vals, y_vals, style)
    if log_x:
        pylab.semilogx()
    if log_y:
        pylab.semilogy()

def run_trial(num_flips):
    num_heads = 0
    for n in range(num_flips):
        if random.choice(('H', 'T')) == 'H':
            num_heads += 1
    num_tails = num_flips - num_heads
    return (num_heads, num_tails)

def flip_plot2(min_exp, max_exp, num_trials):
    """min_exp と max_exp は min_exp < max_exp を満たす正の整数
       num_trials は正の整数
       2**min_exp から 2**max_exp 回のコイン投げを num_trials 回
       行なった結果の要約をプロットする"""

    ratios_means, diffs_means, ratios_sds, diffs_sds = [], [], [], []
    x_axis = []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2**exp)
    for num_flips in x_axis:
        ratios, diffs = [], []
        for t in range(num_trials):
            num_heads, num_tails = run_trial(num_flips)
            ratios.append(num_heads/num_tails)
            diffs.append(abs(num_heads - num_tails))
        ratios_means.append(sum(ratios)/num_trials)
        diffs_means.append(sum(diffs)/num_trials)
        ratios_sds.append(std_dev(ratios))
        diffs_sds.append(std_dev(diffs))
    num_trials_string = ' (' + str(num_trials) + 'Trials) '
    title = 'Mean Heads/Tails Ratios' + num_trials_string
    make_plot(x_axis, ratios_means, title, 'Number of flips', 'Mean Heads/Tails', 'o', log_x=True)
    pylab.savefig('toss_coin/mean_heads_tails_ratios')
    title = 'SD Heads/Tails Ratios' + num_trials_string
    make_plot(x_axis, ratios_sds, title, 'Number of flips', 'Standard Deviation', 'o', log_x=True, log_y=True)
    pylab.savefig('toss_coin/sd_heads_tails_ratios')
    title = 'Mean abs(#Heads - #Tails)' + num_trials_string
    make_plot(x_axis, diffs_means, title, 'Number of flips', 'Mean abs(#Heads - #Tails)', 'o', log_x=True, log_y=True)
    pylab.savefig('toss_coin/mean_abs_heads-tails')
    title = 'SD abs(#Heads - #Tails)' + num_trials_string
    make_plot(x_axis, diffs_sds, title, 'Number of flips', 'Standard Deviation', 'o', log_x=True, log_y=True)
    pylab.savefig('toss_coin/sd_abs_heads-tails')


def cv(x):
    mean = sum(x)/len(x)
    try:
        return std_dev(x)/mean
    except ZeroDivisionError:
        return float('nan')

def flip_plot3(min_exp, max_exp, num_trials):
    """min_exp と max_exp は min_exp < max_exp を満たす正の整数
       num_trials は正の整数
       2**min_exp から 2**max_exp 回のコイン投げを num_trials 回
       行なった結果の要約をプロットする"""

    ratios_means, diffs_means, ratios_sds, diffs_sds = [], [], [], []
    ratios_cvs, diffs_cvs, x_axis = [], [], []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2**exp)
    for num_flips in x_axis:
        ratios, diffs = [], []
        for t in range(num_trials):
            num_heads, num_tails = run_trial(num_flips)
            ratios.append(num_heads/num_tails)
            diffs.append(abs(num_heads - num_tails))
        ratios_means.append(sum(ratios)/num_trials)
        diffs_means.append(sum(diffs)/num_trials)
        ratios_sds.append(std_dev(ratios))
        diffs_sds.append(std_dev(diffs))
        ratios_cvs.append(cv(ratios))
        diffs_cvs.append(cv(diffs))
    num_trials_string = ' (' + str(num_trials) + 'Trials) '

    title = 'Mean Heads/Tails Ratios' + num_trials_string
    make_plot(x_axis, ratios_means, title, 'Number of flips', 'Mean Heads/Tails', 'o', log_x=True)
    pylab.savefig('toss_coin/mean_heads_tails_ratios')
    title = 'SD Heads/Tails Ratios' + num_trials_string
    make_plot(x_axis, ratios_sds, title, 'Number of flips', 'Standard Deviation', 'o', log_x=True, log_y=True)
    pylab.savefig('toss_coin/sd_heads_tails_ratios')

    title = 'Mean abs(#Heads - #Tails)' + num_trials_string
    make_plot(x_axis, diffs_means, title, 'Number of flips', 'Mean abs(#Heads - #Tails)', 'o', log_x=True, log_y=True)
    pylab.savefig('toss_coin/mean_abs_heads-tails')
    title = 'SD abs(#Heads - #Tails)' + num_trials_string
    make_plot(x_axis, diffs_sds, title, 'Number of flips', 'Standard Deviation', 'o', log_x=True, log_y=True)
    pylab.savefig('toss_coin/sd_abs_heads-tails')

    title = 'Coeff of Var. abs(#Heads - #Tails)' + num_trials_string
    make_plot(x_axis, diffs_cvs, title, 'Number of flips', 'Coeff of Var.', 'o', log_x=True)
    pylab.savefig('toss_coin/coeff_abs_heads-tails')
    title = 'Coeff of Var. Heads/Tails ratio)' + num_trials_string
    make_plot(x_axis, ratios_cvs, title, 'Number of flips', 'Coeff of Var.', 'o', log_x=True, log_y=True)
    pylab.savefig('toss_coin/coeff_heads_tails_ratio')


random.seed(0)
pylab.style.use('seaborn-darkgrid')
flip_plot(4, 20)

random.seed(0)
pylab.style.use('seaborn-darkgrid')
flip_plot2(4, 20, 20)

random.seed(0)
pylab.style.use('seaborn-darkgrid')
flip_plot3(4, 20, 20)
