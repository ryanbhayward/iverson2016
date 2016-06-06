def search(maze):
    # change the strings to lists of characters
    # (Python strings are immutable)
    maze = [list(line) for line in maze]
    
    # ensures the search won't try to go out of the entrance
    maze[1][0] = '*'

    def recursive_search(curr_r, curr_c):
        # if we found the exit, return True
        if curr_c == len(maze[0])-1:
            maze[curr_r][curr_c] = '*'
            return True

        # if this cell is a wall or we have already visited it
        if maze[curr_r][curr_c] != ' ':
            return False

        # leave a bread crumb, we have visited this space before
        maze[curr_r][curr_c] = '.'

        # try searching in each of the four directions from this spot
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # if we found the exit, mark the path and return True
            if recursive_search(curr_r + dr, curr_c + dc):
                maze[curr_r][curr_c] = '*'
                return True

        # no exit found
        return False

    # start the search from the right of the entrance
    recursive_search(1, 1)

    # all bread crumbs should be set to ' ' for printing
    for line in maze:
        for i in range(len(line)):
            if line[i] == '.': line[i] = ' '
    
    # print it out
    for line in maze:
        print(*line, sep = '')

test_maze = [
    "XXXXXXXXX",
    "  X     X",
    "X X XXX X",
    "X X X X X",
    "X X X X X",
    "X     X  ",
    "XXXXXXXXX"
]

search(test_maze)
