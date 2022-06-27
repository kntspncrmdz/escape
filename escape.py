from os import system

system('cls')
key = 0
blanket = 0
bat = 0
fire_extinguisher = 0

rooms = [
    'You woke up inside a small room. There is a door but no window. An empty fire extinguisher is right beside you. What will you do?\n1.) Pick up fire extinguisher.\n2.) Remain in the room and wait for someone to enter.',
    'What will you do with the fire extiguisher?\n1.) Smash the door knob and open the door.\n2.) Drop the fire extinguisher and remain in the room.',
    'You are now in a hallway into another room. There are two doors along the hallway. The first is right beside the room where you came from, and the other is across the hallway. You heard some noise beside the first door. What will you do?\n1.) Proceed down the hall and into the second room.\n2.) Check what\'s inside the first room.',
    'You are now in another room. There is an open window in that room. There is also a bed with a long blanket. What will you do?\n1.) Get the blanket.\n2.) Stay in the room and lock the door',
    'What will you do with the blanket?\n1.) Use it to climb down the window.\n2.) Return it on the bed and stay in the room.',
    'You are now outside. There\'s a bat on the ground. Your abductor noticed you\'ve escaped. What will you do?\n1.) Pick up the bat and fight\n2.) Run as fast as you can to get away.',
    'You are now face-to-face with your abductor. What will you do?\n1.) Fight with the bat\n2.) Drop the bat'

]

print('''
You are just walking along the street when suddenly 
a van stopped by and someone grab you into it. 
What will happen to you now can you. . .

- - - - - - - - - - - - 
   E  S  C  A  P  E
- - - - - - - - - - - -
''')
print('\nPlay game?')
print('0.) Exit game')
print('1.) Yes')
cont = input()
action = ''

while cont != '0':
    for i in range(len(rooms)):
        system('cls')
        print(f'''ITEMS [key: {key}     fire extinguisher: {fire_extinguisher}    blanket:    {blanket}     bat: {bat}]''')
        print(rooms[i])
        if rooms[i] == 'You woke up inside a small room. There is a door but no window. An empty fire extinguisher is right beside you. What will you do?\n1.) Pick up fire extinguisher.\n2.) Remain in the room and wait for someone to enter.':
            action = input('Your action: ')
            if action == '1':
                fire_extinguisher = fire_extinguisher + 1
                print('You picked the fire extinguisher.')
            elif action == '2':
                print('Your abductor came in and decided to kill you.')
                break
        elif rooms[i] == 'What will you do with the fire extiguisher?\n1.) Smash the door knob and open the door.\n2.) Drop the fire extinguisher and remain in the room.':
            action = input('Your action: ')
            if action == '1':
                fire_extinguisher = fire_extinguisher - 1
                print('The door is now open.')
            elif action == '2':
                print('Your abductor came in and decided to kill you.')
                break
        elif rooms[i] == 'You are now in a hallway into another room. There are two doors along the hallway. The first is right beside the room where you came from, and the other is across the hallway. You heard some noise beside the first door. What will you do?\n1.) Proceed down the hall and into the second room.\n2.) Check what\'s inside the first room.':
            action = input('Your action: ')
            if action == '1':
                print('You are now in another room. There is an open window in that room. A phone was also there in the room. What will you do?')
            elif action == '2':
                print('The abductor was in the room. He saw you and captured you again. Brought you back to the room where you came from and locked you inside there again.')
        elif rooms[i] == 'You are now in another room. There is an open window in that room. There is also a bed with a long blanket. What will you do?\n1.) Get the blanket.\n2.) Stay in the room and lock the door':
            action = input('Your action: ')
            if action == '1':
                blanket = blanket + 1
                print('You now have a blanket.')
            elif action == '2':
                phone = phone + 1
                print('Your abductor noticed you and get in the room, held you captive again.')
        elif rooms[i] == 'What will you do with the blanket?\n1.) Use it to climb down the window.\n2.) Return it on the bed and stay in the room.':
            action = input('Your action: ')
            if action == '1':
                blanket = blanket - 1
                print('You are now outside the house.')
            elif action == '2':
                print('Your abductor noticed you and get in the room, held you captive again.')
        elif rooms[i] == 'You are now outside. There\'s a bat on the ground. Your abductor noticed you\'ve escaped. What will you do?\n1.) Pick up the bat and fight\n2.) Run as fast as you can to get away.':
            action = input('Your action: ')
            if action == '1':
                bat = bat + 1
                print('You now have a bat.')
            elif action == '2':
                print('Your abductor has a gun and shoots you while you run. You died.')
                break
        elif rooms[i] == 'You are now face-to-face with your abductor. What will you do?\n1.) Fight with the bat\n2.) Drop the bat':
            action = input('Your action: ')
            if action == '1':
                bat = bat - 1
                print('You killed your abductor. You\'re free!')
            elif action == '2':
                print('Your abductor held you captive again.')
    key = 0
    blanket = 0
    phone = 0
    bat = 0
    fire_extinguisher = 0
    print('Game Over! Continue?')
    print('0.) Exit game')
    print('1.) Yes')
    cont = input()
