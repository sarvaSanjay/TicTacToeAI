import pygame, sys
import math
import logic
import time


# Initialise pygame
pygame.init()

#Fonts
Font = pygame.font.Font("OpenSans-Regular.ttf", 20)
mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

# Set screen size
screen = pygame.display.set_mode((400, 600))

# Set title
pygame.display.set_caption("TicTacToe")

# check wheter game is over
def game_over(state, player):
  for x in range(3):
    if state[x][0] == state[x][1] and state[x][1] == state[x][2] and state[x][0] != '':
      return (True, player)
    if state[0][x] == state[1][x] and state[1][x] == state[2][x] and state[0][x] != '': 
      return (True, player)
  if state[0][0] == state[1][1] and state[2][2] == state[0][0] and state[0][0] !='':
    return (True, player)
  if state[0][2] == state[1][1] and state[0][2] == state[2][0] and state[1][1] != '':
    return (True, player)
  rem = False
  for x in range(3):
    if '' in state[x]:
      rem = True
      break
  if not rem:
    return (True, None)
          
  
  return (False, None)

# displaying menu
def menu():
  selectcomp = False
  while True:
    # Screen background
    screen.fill((50, 50, 50))
    if selectcomp:
      # X button
      buttonXB = pygame.Rect(99, 199, 202, 102)
      pygame.draw.rect(screen, (255, 255, 255), buttonXB)
      buttonX = pygame.Rect(100, 200, 200, 100)
      pygame.draw.rect(screen, (100, 100, 100), buttonX)

      # O button
      buttonOB = pygame.Rect(99, 399, 202, 102)
      pygame.draw.rect(screen, (255, 255, 255), buttonOB)
      buttonO = pygame.Rect(100, 400, 200, 100)
      pygame.draw.rect(screen, (100, 100, 100), buttonO)

      # Displaying X text
      txt_X = largeFont.render("Play as X", True, (255, 255, 255))
      txt_X_rect = txt_X.get_rect()
      txt_X_rect.center = buttonX.center
      screen.blit(txt_X, txt_X_rect)
  
      # Displaying O text
      txt_O = largeFont.render("Play as O", True, (255, 255, 255))
      txt_O_rect = txt_O.get_rect()
      txt_O_rect.center = buttonO.center
      screen.blit(txt_O, txt_O_rect)

      # Displaying name of game
      title = moveFont.render("Tic-Tac-Toe", True, (255, 255, 255))
      title_rect = title.get_rect()
      title_rect.center = (200, 50)
      screen.blit(title, title_rect)
    
    else:
      # Comp Button
      buttonCB = pygame.Rect(49, 199, 302, 102)
      pygame.draw.rect(screen, (255, 255, 255), buttonCB)
      buttonC = pygame.Rect(50, 200, 300, 100)
      pygame.draw.rect(screen, (100, 100, 100), buttonC)

      # Human Box
      buttonHB = pygame.Rect(49, 399, 302, 102)
      pygame.draw.rect(screen, (255, 255, 255), buttonHB)
      buttonH = pygame.Rect(50, 400, 300, 100)
      pygame.draw.rect(screen, (100, 100, 100), buttonH)

      # Displaying name of game
      title = moveFont.render("Tic-Tac-Toe", True, (255, 255, 255))
      title_rect = title.get_rect()
      title_rect.center = (200, 50)
      screen.blit(title, title_rect)

      # Displaying Comp text
      txt_Comp = largeFont.render("Play Computer", True, (255, 255, 255))
      txt_Comp_rect = txt_Comp.get_rect()
      txt_Comp_rect.center = buttonC.center
      screen.blit(txt_Comp, txt_Comp_rect)
      

      # Displaying Human text
      txt_Human = largeFont.render("Play Human", True, (255, 255, 255))
      txt_Human_rect = txt_Human.get_rect()
      txt_Human_rect.center = buttonH.center
      screen.blit(txt_Human, txt_Human_rect)

    # taking in player
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.pos[0] > 100 and event.pos[0] < 300 and event.pos[1] > 200 and event.pos[1] < 300 and selectcomp:
          human = 'X'
          computer = 'O'
          print(human)
          default = False
          return (default, human, computer, selectcomp)
        elif event.pos[0] > 100 and event.pos[0] < 300 and event.pos[1] > 400 and event.pos[1] < 500 and selectcomp:
          default = False
          human = 'O'
          computer = 'X'
          print(human)
          return (default, human, computer, selectcomp)
        if event.pos[0] > 100 and event.pos[0] < 300 and event.pos[1] > 400 and event.pos[1] < 500 and not selectcomp:
          default = False
          human = None
          computer = None
          return (default, human, computer, selectcomp)
        if event.pos[0] > 100 and event.pos[0] < 300 and event.pos[1] > 200 and event.pos[1] < 300 and not selectcomp:
          selectcomp = True
    pygame.display.update()

def game(human, computer):
  # defining state
  state = [["", "", ""],
           ["", "", ""],
           ["", "", ""]]

  # Setting initial player as X
  player = 'X'

  # stating that the game is not over and winner as None
  gameover = False
  winner = None

  while True:
    # Listening for events
    for event in pygame.event.get():
      #If user wants to quit
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    
      # If user makes a move
      elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and player == human:
        # Determining relative position of button
        x = int(math.floor((event.pos[0]-47)/103))
        y = int(math.floor((event.pos[1]-253)/103))
      
        # Checking whether its a valid move
        if x  in range(3) and y in range(3) and state[y][x] == '':
          state[y][x] = player
          res = game_over(state, player)
          gameover = res[0]
          winner = res[1]
        
          # checking whether game is over
          if gameover:
            if winner:
              print(f"{winner} wins")
            else:
              print('Match tied')
        
          # swapping player positions
          player = computer
    
      # Allowing user to restart game
      elif gameover and event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          gameover = False
          winner = None
          player = 'X'
          state = [['','',''],
                 ['','',''],
                 ['','','']]
        elif event.key == pygame.K_h:
          return
    # Screen background
    screen.fill((50, 50, 50))

    # Tile description
    tile_size = 100
    tile_origin = (47,253)

    # Background Tile
    big_rect = pygame.Rect(44, 250, 312, 312)
    pygame.draw.rect(screen, (200, 200, 200), big_rect)

    # Drawing the small tiles
    for x in range(3):
      for y in range(3):
        left = tile_origin[0] + y*(tile_size + 3)
        top = tile_origin[1] + x*(tile_size + 3)
        rect = pygame.Rect(left, top, tile_size, tile_size)
        pygame.draw.rect(screen, (100, 100, 100), rect)
        if state[x][y] != "":
          text = moveFont.render(state[x][y], True, (255, 255, 255))
          text_rect = text.get_rect()
          text_rect.center = rect.center
          screen.blit(text, text_rect)

    # Displaying winner and player
    if gameover:
      if winner:
        text = 'Player ' + winner + " wins"
      else:
        text = "Match tied"
    elif player == human:
      text = 'Player ' + human + " move"
    else:
      print("Hi")
      text = "Computer thinking..."
    msg = largeFont.render(text, True, (255,255,255))
    msg_rect = msg.get_rect()
    msg_rect.center = (200, 200)
    screen.blit(msg, msg_rect)

    if gameover:
      replay = 'RETURN to replay'
      replay_msg = Font.render(replay, True, (255,255,255))
      replay_msg_rect = replay_msg.get_rect()
      replay_msg_rect.center = (200 ,575)
      screen.blit(replay_msg, replay_msg_rect)
      home = 'H for home'
      home_msg = Font.render(home, True, (255,255,255))
      home_msg_rect = home_msg.get_rect()
      home_msg_rect.center = (200 ,230)
      screen.blit(home_msg, home_msg_rect)

    # Displaying name of game
    title = moveFont.render("Tic-Tac-Toe", True, (255, 255, 255))
    title_rect = title.get_rect()
    title_rect.center = (200, 50)
    screen.blit(title, title_rect)

    pygame.display.update()

    if text == 'Computer thinking...':
      time.sleep(2)
  
    # allowing computer to play
    if player == computer and not gameover:
      if computer == 'O':
        opt_move = logic.minim(state)[1]
      else:
        opt_move = logic.maxim(state)[1]
      state[opt_move[0]][opt_move[1]] = computer
      res = game_over(state, player)
      gameover = res[0]
      winner = res[1]
      player = human

def vshuman():
  # defining state
  state = [["", "", ""],
           ["", "", ""],
           ["", "", ""]]
  
  # Setting initial player as X
  player = 'X'

  # stating that the game is not over and winner as None
  gameover = False
  winner = None

  while True:
    # Listening for events
    for event in pygame.event.get():
      #If user wants to quit
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    
      # If user makes a move
      elif event.type == pygame.MOUSEBUTTONDOWN and not gameover:
        # Determining relative position of button
        x = int(math.floor((event.pos[0]-47)/103))
        y = int(math.floor((event.pos[1]-253)/103))
      
        # Checking whether its a valid move
        if x  in range(3) and y in range(3) and state[y][x] == '':
          print(x,y)
          state[y][x] = player
          res = game_over(state, player)
          gameover = res[0]
          winner = res[1]
        
          # swapping player positions
          if player == 'X':
            player = 'O'
          else:
            player = 'X'
    
      # Allowing user to restart game
      elif gameover and event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          gameover = False
          winner = None
          player = 'X'
          state = [['','',''],
                   ['','',''],
                   ['','','']]
        elif event.key == pygame.K_h:
          return
  
    # Screen background
    screen.fill((50, 50, 50))

    # Tile description
    tile_size = 100
    tile_origin = (47,253)

    # Background Tile
    big_rect = pygame.Rect(44, 250, 312, 312)
    pygame.draw.rect(screen, (200, 200, 200), big_rect)

    # Drawing the small tiles
    for x in range(3):
      for y in range(3):
        left = tile_origin[0] + y*(tile_size + 3)
        top = tile_origin[1] + x*(tile_size + 3)
        rect = pygame.Rect(left, top, tile_size, tile_size)
        pygame.draw.rect(screen, (100, 100, 100), rect)
        if state[x][y] != "":
          text = moveFont.render(state[x][y], True, (255, 255, 255))
          text_rect = text.get_rect()
          text_rect.center = rect.center
          screen.blit(text, text_rect)

    # Displaying winner and player
    if gameover:
      if winner:
        text = 'Player ' + winner + " wins"
      else:
        text = "Match tied"
    else:
      text = 'Player ' + player + " move"
    msg = largeFont.render(text, True, (255,255,255))
    msg_rect = msg.get_rect()
    msg_rect.center = (200, 200)
    screen.blit(msg, msg_rect)

    if gameover:
      replay = 'RETURN to replay'
      replay_msg = Font.render(replay, True, (255,255,255))
      replay_msg_rect = replay_msg.get_rect()
      replay_msg_rect.center = (200 ,575)
      screen.blit(replay_msg, replay_msg_rect)
      home = 'H for home'
      home_msg = Font.render(home, True, (255,255,255))
      home_msg_rect = home_msg.get_rect()
      home_msg_rect.center = (200 ,230)
      screen.blit(home_msg, home_msg_rect)

    # Displaying name of game
    title = moveFont.render("Tic-Tac-Toe", True, (255, 255, 255))
    title_rect = title.get_rect()
    title_rect.center = (200, 50)
    screen.blit(title, title_rect)

    pygame.display.update()

default = True
while True:
  if default:
    default, human, computer, selectcomp = menu()
  else:
    if selectcomp:
      game(human, computer)
      default = True
    else:
      vshuman()
      default = True