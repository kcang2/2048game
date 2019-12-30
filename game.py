import numpy as np


def random_loc(grid):
    """
    Generates a random 2 or 4 at empty spaces.
    If no empty space before or after generation, gameover
    :param grid: ndarray
    :return: bool gameover
    """
    rc = np.argwhere(grid == 0)

    if len(rc) < 1:
        return True

    i = list(range(len(rc)))
    loc = rc[np.random.choice(i)]
    grid[loc[0], loc[1]] = 2

    return False


def shift_row(vector, is_reverse):
    """
    Applies shifting to each column in the row
    :param vector: Row vector
    :param is_reverse: Left or Right
    :return: score increment, int
    """
    l = len(vector)
    score_inc = 0

    if is_reverse:
        s = -1
        start = 1
        end = l
        step = 1
        wlb = 1
        wub = l
    else:
        s = 1
        start = l - 2
        end = -1
        step = -1
        wlb = 0
        wub = l-1

    for i in range(start, end, step):  # for each column except 1st
        p = i
        while wlb <= p < wub:
            if vector[p+s] == 0:  # next space is 0
                vector[p+s] = vector[p+s] + vector[p]  # move it
                vector[p] = 0  # make the previous empty
                p += s  # keep moving
            elif vector[p+s] == vector[p]:  # next space is same
                score_inc += 2 * vector[p+s]  # update score
                vector[p+s] = vector[p+s] + vector[p]  # move it
                vector[p] = 0  # make the previous empty
                break
            else:  # Different value
                break  # can no longer move
    return score_inc


def apply_move(move, score, grid):
    """
    Apply move
    :param move: movement direction 0=up, 1=down, 2=left, 3=right
    :param score: score of the game
    :param grid: grid of the game
    :return: bool gameover , int score
    """
    temp = grid.copy()

    if move == 'w' or move == 'a':
        is_reverse = True
    else:
        is_reverse = False

    if move == 'w' or move == 's':
        is_transpose = True
    else:
        is_transpose = False

    if is_transpose:
        grid = grid.T

    for i in range(grid.shape[0]):  # for each row
        score += shift_row(grid[i], is_reverse)

    if is_transpose:
        grid = grid.T

    return False if np.array_equal(temp, grid) else random_loc(grid), score


if __name__ == "__main__":

    # Init
    grid = np.zeros((4, 4), dtype=np.int32)
    score = 0
    gameover = False
    won = False
    valids = ['w', 's', 'a', 'd']

    for _ in range(2):
        x = np.random.randint(0, 3)
        y = np.random.randint(0, 3)
        grid[y, x] = 2

    while not gameover:
        if not won:
            if (grid == 2048).any():
                print("You've Won!")
                won = True
        print("Score: " + str(score))
        print(grid)
        move = input("Move: w=up, s=down, a=left, d=right")
        if move not in valids:
            print("Invalid Move")
            continue
        else:
            gameover, score = apply_move(move, score, grid)
        print("="*60)

    print("GAME OVER!")
    print("Score: "+str(score))
    print(grid)



