def magnum_rolls(size, quantity, protein, sauce): 
	"""
	this returns a list of number of magnum rolls that need to be made,
	the protein that goes with it, the sauce, and the number of containers that
	will be needed.

	things that needed to be accounted for:
	-multiple sauces for one order
	"""

	servings = 0
	sauce_for_mag = sauce
	sauce_oz = 0
	size_for_one = 0
	containers = 0


	if size == "small":
		size_for_one = 9
		servings = 3

	elif size == "medium":
		size_for_one = 15
		servings = 5

	elif size == "large":
		size_for_one = 30
		servings = 10

	elif size == "x-large":
		size_for_one = 60
		servings = 20

	num_magnum = size_for_one * quantity
	sauce_oz = servings * 3
	if sauce_oz <= 24:
		containers = 1
	else:
		containers = sauce_oz / 24


	return [num_magnum, protein, containers, sauce]

def banh_mi():
	pass

def flb():
	pass

def fried_rice():
	pass

def pho():
	pass

def egg_rolls():
	pass
