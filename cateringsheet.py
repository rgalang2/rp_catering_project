from docx import Document
from docx.shared import Pt
"""
things that needed to be accounted for:
-multiple sauces for one order and how much sauce is needed if
there ARE multiple sauces for one order (might need to ask delpin)
update: he dont know but he said he will find out for us
-calculating large/medium tins
-catering box space for each items
-special instructions

notes:
-box occupancy, or box_vol, is how much space the item will take up
in one catering box. it is represented as a whole number, but
it'll be like a percentage.
i think three magnum rolls would take up 3% of the box, so i set
box_vol = 3. it'll be summed up at the end then divided by 100
to determine the number of catering boxes.
-i think as of right now, napkins will be 3 per person. could change, idk
"""
info_list = []

def magnum_rolls(size, quantity, protein, sauces): 
	"""
	this returns a list of number of magnum rolls that need to be made,
	the protein that goes with it, the sauce, and the number of containers that
	will be needed.
	"""

	servings = 0
	sauce_oz = 0
	size_for_one = 0 #how many rolls are in one unit (?? idk a better word)
	containers = 0
	box_vol = 0

	if size == "small":
		size_for_one = 9
		servings = 3
		box_vol = 9

	elif size == "medium":
		size_for_one = 15
		servings = 5
		box_vol = 15

	elif size == "large":
		size_for_one = 30
		servings = 10
		box_vol = 30

	elif size == "x-large":
		size_for_one = 60
		servings = 20
		box_vol = 60


	total_people = servings * quantity
	box_vol *= quantity

	num_magnum = size_for_one * quantity
	sauce_oz = num_magnum * 2

	if sauce_oz <= 24: #if the amount of sauce does not go up to 24, it will just give them one container
		containers = 1
	else:
		containers = int(round(sauce_oz / 24, 0))
	
	containers *= len(sauces)
	
	#i want napkins to be a multiple of 10. kinda personal preference because who wants to count exactly 76 napkins
	napkins = total_people * 3
	while napkins % 10 != 0:
		napkins +=1 
	#same thing with ramekins
	ramekins = (containers * 12) * len(sauces)
	while ramekins % 10 != 0:
		ramekins += 1

	info_list.append([f'{num_magnum} magnum rolls', protein, containers, sauces, napkins, box_vol, ramekins, total_people])

def banh_mi(size, quantity, protein, mayo):
	"""
	returns a list of the number of banh mi, the protein, and the mayo
	"""
	box_vol = 0
	num_banh = 0
	servings = 0
	size = size.lower()


	if size == "small":
		servings = 3
		box_vol = 12
	elif size == "medium":
		servings = 5
		box_vol = 25
	elif size == "large":
		servings = 10
		box_vol = 55
	elif size == "x-large":
		servings = 20
		box_vol = 110


	num_banh = servings * quantity
	total_people = servings * quantity
	box_vol *= quantity

	#i want napkins to be a multiple of 10. kinda personal preference because who wants to count exactly 76 napkins
	napkins = total_people * 3
	while napkins % 10 != 0:
		napkins +=1
	
	info_list.append([f'{num_banh} banh mi', protein, mayo, napkins, total_people, box_vol])


def flb(size, quantity, protein, sauces):
	size = size.lower()
	box_vol = 1
	tin = 0
	size_tin = ""
	servings = 0

	if size == "small":
		servings = 3
	elif size == "medium":
		servings = 5
	elif size == "large":
		servings = 10
	elif size == "x-large":
		servings = 20
	
	total_people = quantity * servings
	sauce_oz = (total_people*3) /24

	if sauce_oz <= 24:
		containers = 1
	else:
		containers = int(round(sauce_oz, 0))	

	#i want napkins to be a multiple of 10. kinda personal preference because who wants to count exactly 76 napkins
	napkins = total_people * 3
	while napkins % 10 != 0:
		napkins +=1
	#same thing with ramekins
	ramekins = (containers * 12) * len(sauces)
	while ramekins % 10 != 0:
		ramekins += 1

	if total_people < 7:
		size_tin = "medium tins"
		tin = total_people//3
		if total_people%3 > 1:
			tin += 1
	else:
		size_tin = "large tins"
		tin = total_people // 7
		if total_people % 7 >= 2:
			tin +=1
	
	box_vol = 50 * tin * quantity
	#flb list indexes: [0: number of tins, size tin, protein, # of containers, sauces, napkins, ramekins, total people, box volume]
	info_list.append([f'{tin} tins', size_tin, protein, containers, sauces, napkins, ramekins, total_people, box_vol])

def fried_rice(size, quantity):
	"""
	FOR NICO
	-input is each item on the receipt, so the function would be used for one order of fried rice.
	-make a list that contains 
	[number of tins, the size of each tin, number of pairs of utensils, box occupancy, total people]
	-append it to the list 'info_list'
	"""
	
	pass

def pho(size, quantity, pho_type, pairs_of_utensils):
	"""
	FOR NICO
	-input is each item on the receipt, so the function would be used for one order of pho.
	-make a list that contains 
	[number of pho, protein, utensils, box occupancy, total people]
	-append it to the list 'info_list'
	"""
	pass

def egg_rolls(size, quantity, type_of_ER):
	"""
	FOR NICO
	-make a list that contains
	[number of tins, size of each tin, napkins, box occupancy, total people]
	-append it to the list 'info_list'
	"""
	pass

"""
FOR KIET
-this part is user input. i have no idea how to make a gui so good luck ! 
 
-right now, i have it so the user keeps giving items until they type in 'x',
but there is probably a better way for them to input stuff

-i saw you do dropdown menus on your boba website project, that could be
useful !!! 

lmk if you have questions B)
"""