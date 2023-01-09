
while True: 
    game = input('Type start to begin playing: ')
    if game == 'start':
      player1 = input('Choose Rock, Paper, or Scissors: ')
      player2 = input('Choose Rock, Paper, or Scissors: ')
    else: 
        break
    
    if player1 == 'Rock'and player2 == 'Scissors':
       print('Congratulations to player1!')
    elif player1 == 'Rock' and player2 == 'Paper':
       print('Congratulations to player2!')
    elif player1 == 'Scissors' and player2 == 'Rock':
       print('Congratulations to player2!')
    elif player1 == 'Paper' and player2 == 'Rock':
       print('Congratulations to player1!')
    elif player1 == 'Scissors' and player2 == 'Paper':
       print('Congratulations to player1!')
    elif player1 == 'Paper' and player2 == 'Scissors':
       print('Congratulations to player2!')
    else:
      print('Both players have chosen the same object. Please try again')

