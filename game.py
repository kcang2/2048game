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


def apply_move(move, score, grid):
    """
    Apply move
    :param move: movement direction 0=up, 1=down, 2=left, 3=right
    :param score: score of the game
    :param grid: grid of the game
    :return: bool gameover , int score
    """
    temp = grid.copy()
    if move == 'w':
        for j in range(grid.shape[1]):  # for each column
            for i in range(1, grid.shape[0]):  # for each row except 1st
                p = i
                while 0 < p < grid.shape[0]:  # 1 to 3
                    if grid[p-1, j] == 0:  # next space is 0
                        grid[p-1, j] = grid[p-1, j] + grid[p, j]  # move it
                        grid[p, j] = 0  # make the previous empty
                        p -= 1  # keep moving
                    elif grid[p-1, j] == grid[p, j]:  # next space is same
                        score += 2 * grid[p - 1, j]  # update score
                        grid[p-1, j] = grid[p-1, j] + grid[p, j]  # move it
                        grid[p, j] = 0  # make the previous empty
                        break
                    else:  # Different value
                        break  # can no longer move

    elif move == 's':
        for j in range(grid.shape[1]):  # for each column
            for i in range(grid.shape[0]-2, -1, -1):  # for each row except last
                p = i  # pointer
                while 0 <= p < grid.shape[0]-1:  # 0 to 2
                    if grid[p+1, j] == 0:  # next space is 0
                        grid[p+1, j] = grid[p+1, j] + grid[p, j]  # move it
                        grid[p, j] = 0  # make the previous empty
                        p += 1  # keep moving
                    elif grid[p + 1, j] == grid[p, j]:  # next space is same
                        score += 2 * grid[p + 1, j]  # update score
                        grid[p+1, j] = grid[p+1, j] + grid[p, j]  # move it
                        grid[p, j] = 0  # make the previous empty
                        break
                    else:  # Different value
                        break  # can no longer move

    elif move == 'a':
        for i in range(grid.shape[0]):  # for each row
            for j in range(1, grid.shape[1]):  # for each column except 1st
                p = j
                while 0 < p < grid.shape[1]:  # 1 to 3
                    if grid[i, p-1] == 0:  # next space is 0
                        grid[i, p-1] = grid[i, p-1] + grid[i, p]  # move it
                        grid[i, p] = 0  # make the previous empty
                        p -= 1  # keep moving
                    elif grid[i, p-1] == grid[i, p]:  # next space is same
                        score += 2 * grid[i, p - 1]  # update score
                        grid[i, p-1] = grid[i, p-1] + grid[i, p]  # move it
                        grid[i, p] = 0  # make the previous empty
                        break
                    else:  # Different value
                        break  # can no longer move

    elif move == 'd':
        for i in range(grid.shape[0]):  # for each row
            for j in range(grid.shape[1]-2, -1, -1):  # for each column except last
                p = j
                while 0 <= p < grid.shape[1]-1:  # 0 to 2
                    if grid[i, p+1] == 0:  # next space is 0 or same
                        grid[i, p+1] = grid[i, p+1] + grid[i, p]  # move it
                        grid[i, p] = 0  # make the previous empty
                        p += 1  # keep moving
                    elif grid[i, p+1] == grid[i, p]:
                        score += 2 * grid[i, p + 1]  # update score
                        grid[i, p+1] = grid[i, p+1] + grid[i, p]  # move it
                        grid[i, p] = 0  # make the previous empty
                        break
                    else:  # Different value
                        break  # can no longer move

    return False if np.array_equal(temp, grid) else random_loc(grid), score


if __name__ == "__main__":

    # Init
    grid = np.zeros((4, 4), dtype=np.int32)
    score = 0
    gameover = False
    valids = ['w', 's', 'a', 'd']

    for _ in range(2):
        x = np.random.randint(0, 3)
        y = np.random.randint(0, 3)
        grid[y, x] = 2

    while not gameover:
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



