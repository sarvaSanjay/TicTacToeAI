import copy
# defining action state of particular game
def actions(state):
  action = []
  for x in range(3):
    for y in range(3):
      if state[x][y] == '':
        action.append((x, y))
  return action

def result(state, move, player):
  restate = copy.deepcopy(state)
  restate[move[0]][move[1]] = player
  return restate

def winner(state):
  map = {'X': 1, 'O': -1}
  for x in range(3):
    if state[x][0] == state[x][1] and state[x][1] == state[x][2] and state[x][0] != '':
      return (True, map[state[x][0]])
    if state[0][x] == state[1][x] and state[1][x] == state[2][x] and state[0][x] != '': 
      return (True, map[state[0][x]])
  if state[0][0] == state[1][1] and state[2][2] == state[0][0] and state[0][0] !='':
    return (True, map[state[0][0]])
  if state[0][2] == state[1][1] and state[0][2] == state[2][0] and state[1][1] != '':
    return (True, map[state[1][1]])
  rem = False
  for x in range(3):
    if '' in state[x]:
      rem = True
      break
  if not rem:
    return (True, 0)
  return(False, 0)

def maxim(state):
  moves = actions(state)
  res = dict()
  for move in moves:
    restate = result(state, move, 'X')
    outcome = winner(restate)
    over = outcome[0]
    if over:
      victor = outcome[1]
      res[str(move[0]) + str(move[1])] = victor
    else:
      output = minim(restate)
      res[str(move[0]) + str(move[1])] = output[0]
  maxed = -2
  opt_move = [0,0]
  for move, val in res.items():
    if val > maxed:
      maxed = val
      opt_move = [int(move[0]), int(move[1])]
  return [maxed, opt_move]

def minim(state):
  moves = actions(state)
  res = dict()
  for move in moves:
    restate = result(state, move, 'O')
    outcome = winner(restate)
    over = outcome[0]
    if over:
      victor = outcome[1]
      res[str(move[0]) + str(move[1])] = victor
    else:
      output = maxim(restate)
      res[str(move[0]) + str(move[1])] = output[0]
  mined = 2
  opt_move = [0,0]
  for move, val in res.items():
    if val < mined:
      mined = val
      opt_move = [int(move[0]), int(move[1])]
  return [mined, opt_move]

tate = [['','',''],
         ['','',''],
         ['','','']]
player = 'X'
if __name__ == '__main__':
  while not winner(tate)[0]:
    if player == 'X':
      out = maxim(tate)
    else:
      out = minim(tate)
    tate[out[1][0]][out[1][1]] = player
    print(tate)
    if player == 'X':
      player = 'O'
    else:
      player = 'X'
    