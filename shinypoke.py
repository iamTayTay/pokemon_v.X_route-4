import random
import time

route_4 = []
attempts = []
shinycatch= []
x_version = True

for a in range(30):
	route_4.append('Combee')
for a in range(30):
	route_4.append('Flabebe (Yellow)')
for a in range(10):
	route_4.append('Ledyba')
for a in range(10):
	route_4.append('Skitty')
for a in range(10):
	route_4.append('Budew')
for a in range(5):
	route_4.append('Ralts')
for a in range(4):
	route_4.append('Flabebe (Orange)')
route_4.append('Flabebe (White)')

while x_version:
	time.sleep(12)
	pokemoncatch = random.choice(route_4)
	shiny = random.randint(1, 8192)
	if shiny == 1:
		shiny = 'shiny'
	else:
		shiny = 'regular'
	if pokemoncatch == 'Flabebe (Yellow)':
		gender = "♀"
	if pokemoncatch == 'Flabebe (Orange)':
		gender = "♀"
	if pokemoncatch == 'Flabebe (White)':
		gender = "♀"
	if pokemoncatch == 'Ledyba':
		gender = random.randint(1, 100)
		if gender < 51:
			gender = "♂"
		else:
			gender = "♀"
	if pokemoncatch == 'Budew':
		gender = random.randint(1, 100)
		if gender < 51:
			gender = "♂"
		else:
			gender = "♀"
	if pokemoncatch == 'Ralts':
		gender = random.randint(1, 100)
		if gender < 51:
			gender = "♂"
		else:
			gender = "♀"
	if pokemoncatch == 'Combee':
		gender = random.randint(1, 200)
		if gender < 26:
			gender = "♂"
		else:
			gender = "♀"
	if pokemoncatch == 'Skitty':
		gender = random.randint(1, 100)
		if gender < 26:
			gender = "♂"
		else:
			gender = "♀"
	attempts.append(pokemoncatch)
	print(f"You found a {shiny} {pokemoncatch} {gender} in attempt #: {len(attempts)}")
	if shiny == 'shiny':
		if pokemoncatch == 'Flabebe (White)':
			print(f"You've caught {len(shinycatch)} shiny pokemon in your attempt"
				"for a shiny white flower Flabebe.")
			shinycatch.append(pokemoncatch)
			x_version = False