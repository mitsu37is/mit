import random

def variance(X):
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return tot/len(X)

def std_dev(X):
    return variance(X) ** 0.5

def throw_needles(num_needles):
    in_circle = 0
    for needles in range(1, num_needles + 1):
        x, y = random.random(), random.random()
        if (x**2 + y**2)**0.5 <= 1:
            in_circle += 1
    return 4*(in_circle/float(num_needles))

def get_est(num_needles, num_trials):
    estimate = []
    for t in range(num_trials):
        pi_guess = throw_needles(num_needles)
        estimate.append(pi_guess)
    s_dev = std_dev(estimate)
    cur_est = sum(estimate)/len(estimate)
    print('Est = ' + str(round(cur_est, 5)) + ',', 'Std Dev = ' + str(round(s_dev, 5)) + ',', 'Needles = ' + str(num_needles))
    return (cur_est, s_dev)

def est_pi(precision, num_trials):
    num_needles = 1000
    s_dev = precision
    while s_dev >= precision/1.96:
        cur_est, s_dev = get_est(num_needles, num_trials)
        num_needles *= 2
    return cur_est

est_pi(0.01, 100)