from docx import Document
"""
things that needed to be accounted for:
-multiple sauces for one order and how much sauce is needed if
there ARE multiple sauces for one order (might need to ask delpin)
update: he dont know but he said he will find out for us
-how calculating catering boxes will work
-napkin/utenstil system
-special instructions
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


	total_people = servings * quantity

	num_magnum = size_for_one * quantity
	sauce_oz = total_people * 3

	if sauce_oz <= 24:
		containers = 1
	else:
		containers = int(round(sauce_oz / 24, 0))

	napkins = total_people * 2

	info_list.append([f'{num_magnum} magnum rolls', protein, f'{containers} containers', sauces, f'{napkins} napkins'])

def banh_mi(size, quantity, protein, mayo):
	"""
	returns a list of the number of banh mi, the protein, and the mayo
	"""
	num_banh = 0
	servings = 0


	if size == "small":
		servings = 3
	elif size == "medium":
		servings = 5
	elif size == "large":
		servings = 10
	elif size == "x-large":
		servings = 20


	num_banh = servings * quantity
	napkins = num_banh * 3

	info_list.append([f'{num_banh} banh mi', protein, mayo, f'{napkins} napkins'])


def flb(size, quantity, protein, sauces):
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
	sauce_oz = total_people/24

	if sauce_oz <= 24:
		containers = 1
	else:
		containers = int(round(sauce_oz / 24, 0))	

	napkins = total_people * 2

	if total_people < 7:
		size_tin = "medium tins"
		tin = total_people//3
		if total_people%3 > 1:
			tin += 1
	else:
		size_tin = "large tins"
		tin = total_people // 7
		if total_people % 7 > 3:
			tin +=1


	info_list.append([f'{tin} tins', size_tin, protein, f'{containers} containers', sauces, f'{napkins} napkins'])

def fried_rice():
	pass

def pho():
	pass

def egg_rolls():
	pass

flb("large", 8, "chicken", "sweet chili")
info_dict = {}
for info in info_list:
	if "magnum rolls" in info[0]:
		if "Magnum Rolls" not in info_dict.keys():
			info_dict["Magnum Rolls"] = {info[1]:int(info[0].strip(" magnum rolls"))}
		else:
			if info[1] in info_dict["Magnum Rolls"].keys():
				info_dict["Magnum Rolls"][info[1]] += int(info[0].strip(" magnum rolls"))
			else:
				info_dict["Magnum Rolls"][info[1]] = int(info[0].strip(" magnum rolls"))
	elif "banh mi" in info[0]:
		if "Banh Mi" not in info_dict.keys():
			info_dict["Banh Mi"] = {f'{info[1]} w/ {info[2]}':int(info[0].strip(" banh mi"))}
		else:
			if f'{info[1]} w/ {info[2]}' in info_dict["Banh Mi"].keys():
				info_dict["Banh Mi"][f'{info[1]} w/ {info[2]}'] += int(info[0].strip(" banh mi"))
			else:
				info_dict["Banh Mi"][f'{info[1]} w/ {info[2]}'] = int(info[0].strip(" banh mi"))
	elif "tins" in info[0]:
		if "Fully Loaded Bowls" not in info_dict.keys():
			info_dict["Fully Loaded Bowls"] = {f'{info[2]} in {info[1]}':int(info[0].strip(" tins"))}
		else:
			if f'{info[2]} in {info[1]}' in info_dict["Fully Loaded Bowls"].keys():
				info_dict["Fully Loaded Bowls"][f'{info[2]} in {info[1]}'] += int(info[0].strip(" tins"))
			else:
				info_dict["Fully Loaded Bowls"][f'{info[2]} in {info[1]}'] = int(info[0].strip(" tins"))
print(info_dict)