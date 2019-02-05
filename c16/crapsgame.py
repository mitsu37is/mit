import random

def roll_die():
    return random.choice([1, 2, 3, 4, 5, 6, 1, 5, 3, 4, 5, 6])

def variance(X):
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return tot/len(X)

def std_dev(X):
    return variance(X) ** 0.5

class CrapsGame(object):
    def __init__(self):
        self.pass_wins, self.pass_losses = 0, 0
        self.dp_wins, self.dp_losses, self.dp_pushes = 0, 0, 0

    def play_hand(self):
        points_dict = {4: 1/3, 5: 2/5, 6: 5/11, 8: 5/11, 9:2/5, 10: 1/3}
        throw = roll_die() + roll_die()
        if throw == 7 or throw == 11:
            self.pass_wins += 1
            self.dp_losses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.pass_losses += 1
            if throw == 12:
                self.dp_pushes += 1
            else:
                self.dp_wins += 1
        else:
            if random.random() <= points_dict[throw]:
                self.pass_wins += 1
                self.dp_losses += 1
            else:
                self.pass_losses += 1
                self.dp_wins += 1

    def pass_results(self):
        return (self.pass_wins, self.pass_losses)

    def dp_results(self):
        return (self.dp_wins, self.dp_losses, self.dp_pushes)


def crap_sim(hands_per_game, num_games):
    games = []

    for t in range(num_games):
        c = CrapsGame()
        for i in range(hands_per_game):
            c.play_hand()
        games.append(c)

    p_roi_per_game, dp_roi_per_game = [], []
    for g in games:
        wins, losses = g.pass_results()
        p_roi_per_game.append((wins - losses)/float(hands_per_game))
        wins, losses, pushes = g.dp_results()
        dp_roi_per_game.append((wins - losses)/float(hands_per_game))

    mean_roi = str(round(100*sum(p_roi_per_game)/num_games, 4)) + '%'
    sigma = str(round(100*std_dev(p_roi_per_game), 4)) + '%'
    print('Pass:', 'Mean ROI = ', mean_roi, 'Std Dev. = ', sigma)
    mean_roi = str(round(100 * sum(dp_roi_per_game) / num_games, 4)) + '%'
    sigma = str(round(100 * std_dev(dp_roi_per_game), 4)) + '%'
    print('Don\'t:', 'Mean ROI = ', mean_roi, 'Std Dev. = ', sigma)


crap_sim(1000000, 10)