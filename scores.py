score = 0

def set_score(scoreIncrease):
    global score
    score += scoreIncrease

def get_score():
    return score

def reset_score():
    global score
    score = 0
