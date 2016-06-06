def translate(maze):
  # this code would be cleaner if the input
  # format insisted that the left entrance
  # be _ instead of blank on top of |
  # ... either answer was ok
  newMaze = ['X'*len(maze[0])] #top border
  for j in range(1,len(maze)): #rest of maze
    newLine, newLine2  = '',''
    for k in range(len(maze[0])):
      if maze[j][k] == '|':
        newLine  += 'X'
        newLine2 += 'X'
      elif maze[j][k] == '_':
        newLine  += ' '
        newLine2 += 'X'
      else: # x must be ' '
        # this case would be simpler if input
        # format was changed as mentioned above
        newLine  += ' '
        if maze[j+1][k] == '|':
          newLine2 += 'X'
        else:
          newLine2 += ' '
    newMaze.append(newLine)
    newMaze.append(newLine2)
  return newMaze

test_maze = [
  "_________",
  "  |     |",
  "| | | | |",
  "|_____|__"
]

for line in translate(test_maze): print(line)
