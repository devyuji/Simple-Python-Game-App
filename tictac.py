# tictac by Raghavan

def display(l2):
	print('\n'*50)
	print(l2[7],'|',l2[8],'|',l2[9])
	print(l2[4],'|',l2[5],'|',l2[6])
	print(l2[1],'|',l2[2],'|',l2[3])
	check_win(l2)
	check_empty(l2)

def player_choice():
	a = input("X or O\n")
	inp = 0
	if a == 'O':
		return 'O','X'
	else:
		return 'X','O'

def player_move(l1,p,q):
	global i,j,won,b,b1
	i = int(input(f'enter your move {p}:'))
	l1[i] = p
	display(l1)
	if b:
		if won == '':
			print('DRAW!')
			b1 =  True
			b = False
			return None,None,None
		else:
			print(f'You WON {won}')
			b = False
			b1 = True
			return None,None,None
	else:
		j = int(input(f'enter your move {q}:'))
		l1[j] = q
		return l1,i,j

# checking if the user have won the tictac or not using boolean
def check_win(l3):
	global b,won
	# For 'X'
	if l3[1] == 'X' and l3[2] == 'X' and l3[3] =='X':
		b = True
		won = "X"
	elif l3[4] == 'X' and l3[5] == 'X' and l3[6] =='X':
		b = True
		won = "X"
	elif l3[7] == 'X' and l3[8] == 'X' and l3[9] == 'X':
		b = True
		won = "X"
	elif l3[1] ==  'X' and l3[5] == 'X' and l3[9] =='X':
		b = True
		won = "X"
	elif l3[7] == 'X' and l3[5] == 'X' and l3[3] == 'X':
		b = True
		won = "X"
	elif l3[7] == 'X' and l3[4] == 'X' and l3[1] == 'X':
		b = True
		won = 'X'
	elif l3[8] == 'X' and l3[5] == 'X' and l3[2] == 'X':
		b =True
		won = "X"
	elif l3[9] == 'X' and l3[6] == 'X' and l3[3] == 'X':
		b = True
		won = 'X'
	# For 'O'
	elif l3[1] == 'O' and l3[2] == 'O' and l3[3] =='O':
		b = True
		won = "O"
	elif l3[4] == 'O' and l3[5] == 'O' and l3[6] =='O':
		b = True
		won = "O"
	elif l3[7] == 'O' and l3[8] == 'O' and l3[9] == 'O':
		b = True
		won = "O"
	elif l3[1] ==  'O' and l3[5] == 'O' and l3[9] =='O':
		b = True
		won = "O"
	elif l3[7] == 'O' and l3[5] == 'O' and l3[3] == 'O':
		b = True
		won = "O"
	elif l3[7] == 'O' and l3[4] == 'O' and l3[1] == 'O':
		b = True
		won = 'O'
	elif l3[8] == 'O' and l3[5] == 'O' and l3[2] == 'O':
		b =True
		won = "O"
	elif l3[9] == 'O' and l3[6] == 'O' and l3[3] == 'O':
		b = True
		won = 'O'

def check_empty(l4): # tie function
	global b
	if (l4[1] == 'O' or l4[1] == 'X') and (l4[2] == 'O' or l4[2] == 'X') and (l4[3] == 'O' or l4[3] == 'X') and (l4[4] ==  'X' or l4[4] =='O') and (l4[5] == 'O' or l4[5] == 'X') and (l4[6] == 'O' or  l4[6] == 'X') and (l4[7] == 'X' or l4[7] =='O') and (l4[8] == "O" or l4[8] == "X") and (l4[9] == 'X' or l4[9] == "O"):
		b = True
#__main__
p1,p2 = '',''
won = ''
i,j = 0,0
repeats = []
l = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
b,b1 = False,False
x,w=0,0
p1,p2 = player_choice()
display(l)
while True:
	l,x,w = player_move(l,p1,p2)
	if b1:
		break
	check_win(l)
	check_empty(l)
	display(l)
	if b:
		print(f'You WON {won}')
		break
