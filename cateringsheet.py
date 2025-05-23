from docx import Document
from docx.shared import Pt
"""
things that needed to be accounted for:
-multiple sauces for one order and how much sauce is needed if
there ARE multiple sauces for one order (might need to ask delpin)
update: he dont know but he said he will find out for us
-calculating large/medium tins
-catering box space for each item
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
	sauce_oz = total_people * 3

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
	total_people = servings * quantity

	#i want napkins to be a multiple of 10. kinda personal preference because who wants to count exactly 76 napkins
	napkins = total_people * 3
	while napkins % 10 != 0:
		napkins +=1

	info_list.append([f'{num_banh} banh mi', protein, mayo, napkins, total_people])


def flb(size, quantity, protein, sauces):
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

	#if the amount of sauce does not go up to 24, it will just give them one container
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
	
	box_vol = 50*tin

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
name = input("Guest name: ")
# number = input("Guest's phone number: ")
# date = input("Date due: ")
# time = input("Time Due: ")
# delivery = False
# address = ""
# special_instructions = ""
# if input("Is this a delivery?: ") == "yes":
# 	delivery = True
# 	address = input("What is the address?: ")
# if input("Any special instructions?: ") == "yes":
# 	special_instructions = input("Special instructions: ")

user_input = input("What item?: ")
while user_input != 'x':
	if user_input == "magnum rolls":
		quantity = int(input("Quantity?: "))
		size = input("What size?: ")
		protein = input("What protein?: ")
		sauces = []
		sauce = input('What sauce?: ')
		while sauce != "no":
			sauces.append(sauce)
			sauce = input('Any other sauces?: ')
	
		magnum_rolls(size, quantity, protein, sauces)
		user_input = input("What item?: ")

	if user_input == "banh mi":
		quantity = int(input("Quantity?: "))
		size = input("What size?:" )
		protein = input("What protein?: ")
		mayo = input("What mayo?: ")

		banh_mi(size, quantity, protein, mayo)
		user_input = input("What item?: ")
	
	if user_input == "flb":
		quantity = int(input("Quantity?: "))
		size = input("What size?: ")
		protein = input("What protein?: ")
		sauces = []
		sauce = input("What sauce?: ")

		while sauce != "no":
			sauces.append(sauce)
			sauce = input("Any other sauces?: ")
		
		flb(size, quantity, protein, sauces)
		user_input = input("What item?: ")
		

info_dict = {}
prep_sheet = {}
sauce_list = {}

for info in info_list:
	if "magnum rolls" in info[0]:
		if "Magnum Rolls" not in info_dict.keys():
			info_dict["Magnum Rolls"] = {info[1]:int(info[0].strip(" magnum rolls"))}
		else:
			if info[1] in info_dict["Magnum Rolls"].keys():
				info_dict["Magnum Rolls"][info[1]] += int(info[0].strip(" magnum rolls"))
			else:
				info_dict["Magnum Rolls"][info[1]] = int(info[0].strip(" magnum rolls"))
		for s in info[3]:
			if sauce not in sauce_list.keys():
				sauce_list[s] = info[2]
			else:
				sauce_list[s] += info[2]
		if "Napkins" not in prep_sheet.keys():
			prep_sheet["Napkins"] = info[4]
		else:
			prep_sheet["Napkins"] += info[4]
		if "Catering Boxes" not in prep_sheet.keys():
			prep_sheet["Catering Boxes"] = info[5]
		else:
			prep_sheet["Catering Boxes"] += info[5]
		if "Ramekins" not in prep_sheet.keys():
			prep_sheet["Ramekins"] = info[6]
		else:
			prep_sheet["Ramekins"] += info[6]
		if "Plates" not in prep_sheet.keys():
			prep_sheet["Plates"] = info[7]
			while prep_sheet["Plates"] % 5 != 0:
				prep_sheet["Plates"] += 1
		else:
			prep_sheet["Plates"] += info[7]
			while prep_sheet["Plates"] % 5 != 0:
				prep_sheet["Plates"] += 1
	
	elif "banh mi" in info[0]:
		if "Banh Mi" not in info_dict.keys():
			info_dict["Banh Mi"] = {f'{info[1]} w/ {info[2]}':int(info[0].strip(" banh mi"))}
		else:
			if f'{info[1]} w/ {info[2]}' in info_dict["Banh Mi"].keys():
				info_dict["Banh Mi"][f'{info[1]} w/ {info[2]}'] += int(info[0].strip(" banh mi"))
			else:
				info_dict["Banh Mi"][f'{info[1]} w/ {info[2]}'] = int(info[0].strip(" banh mi"))
		if "Napkins" not in prep_sheet.keys():
			prep_sheet["Napkins"] = info[3]
		else:
			prep_sheet["Napkins"] = info[3]
		if "Plates" not in prep_sheet.keys():
			prep_sheet["Plates"] = info[4]
		else:
			prep_sheet["Plates"] += info[4]
	elif "tins" in info[0]:
		if "Fully Loaded Bowls" not in info_dict.keys():
			info_dict["Fully Loaded Bowls"] = {f'{info[2]} in {info[1]}':int(info[0].strip(" tins"))}
		else:
			if f'{info[2]} in {info[1]}' in info_dict["Fully Loaded Bowls"].keys():
				info_dict["Fully Loaded Bowls"][f'{info[2]} in {info[1]}'] += int(info[0].strip(" tins"))
			else:
				info_dict["Fully Loaded Bowls"][f'{info[2]} in {info[1]}'] = int(info[0].strip(" tins"))
		for s in info[4]:
			if s in sauce_list.keys():
				sauce_list[s] += info[3]
			else:
				sauce_list[s] = info[3]
		if "Napkins" not in prep_sheet.keys():
			prep_sheet["Napkins"] = info[5]
		else:
			prep_sheet["Napkins"] += info[5]
		if "Plates" not in prep_sheet.keys():
			prep_sheet["Plates"] = info[7]
		else:
			prep_sheet["Plates"] += info[7]
		if "Ramekins" not in prep_sheet.keys():
			prep_sheet["Ramekins"] = info[6]
		else:
			prep_sheet["Ramekins"] += info[6]
		if "large tins" in info[1]:
			if "Large Catering Tins + Lids" not in prep_sheet.keys():
				prep_sheet["Large Catering Tins + Lids"] = int(info[0].strip(" tins"))
			else:
				prep_sheet["Large Catering Tins + Lids"] += int(info[0].strip(" tins"))
		if "medium tins" in info[1]:
			if "Medium Catering Tins + Lids" not in prep_sheet.keys():
				prep_sheet["Medium Catering Tins + Lids"] = int(info[0].strip(" tins"))
			else:
				prep_sheet["Medium Catering Tins + Lids"] += int(info[0].strip(" tins"))
		if "Catering Boxes" not in prep_sheet.keys():
			prep_sheet["Catering Boxes"] = info[8]
		else:
			prep_sheet["Catering Boxes"] += info[8]
		if "Forks" not in prep_sheet.keys():
			prep_sheet["Forks"] = info[7]
		else:
			prep_sheet["Forks"] += info[7]
		if "Spoons" not in prep_sheet.keys():
			prep_sheet["Spoons"] = info[7]
		else:
			prep_sheet["Spoons"] += info[7]
	#fried rice 
	#pho
	#egg rolls
#making plates and utensils a multiple of 10
while prep_sheet["Plates"] % 10 != 0:
	prep_sheet["Plates"] += 1
if "Forks" in prep_sheet.keys(): 
	while prep_sheet["Forks"] % 10 != 0 and prep_sheet["Spoons"] % 10 != 0:
		prep_sheet["Forks"] +=1
		prep_sheet["Spoons"] +=1

prep_sheet["Catering Boxes"] = round(prep_sheet["Catering Boxes"], -1)//100
if prep_sheet["Catering Boxes"] == 0:
	prep_sheet["Catering Boxes"] = 1

print(info_list)
print(info_dict)
print(prep_sheet)
print(sauce_list)

#constructs the word doc
document = Document()
style = document.styles['Normal']
font = style.font
font.name = "Arial"
font.size = Pt(13)
d = document.add_paragraph(f'Guest Name: {name} \nGuest\'s Phone #: \nDate: \nTime Due: \n')
d.add_run("Delivery: \nDelivered by: \nAddress: ")
document.add_paragraph("Special Instructions: ")
for items in info_dict:
	thing = document.add_paragraph(items, style="List Bullet")
	thing.paragraph_format.space_before = 1
	thing.paragraph_format.space_after = 1
	for a in info_dict.get(items):
		protein = document.add_paragraph(f'{info_dict[items].get(a)} {a}', style="List Bullet 2")
		protein.paragraph_format.space_after = 1
		protein.paragraph_format.space_before = 1
preparation = document.add_paragraph("Prep Sheet:")
preparation.paragraph_format.space_before = Pt(3)
preparation.paragraph_format.space_after = Pt(1)
for prep in prep_sheet:
	thing = document.add_paragraph(f'{prep}: {prep_sheet[prep]}', style= "List Bullet")
	thing.paragraph_format.space_after = Pt(1)
	thing.paragraph_format.space_before = Pt(1)
sauce_prep = document.add_paragraph("Sauces (24oz):")
sauce_prep.paragraph_format.space_before = Pt(3)
sauce_prep.paragraph_format.space_after = Pt(1)
for sasa in sauce_list:
	fuck = document.add_paragraph(f'{sasa}: {sauce_list[sasa]}', style="List Bullet")
	fuck.paragraph_format.space_before = Pt(1)
	fuck.paragraph_format.space_after = Pt(1)
document.save(f'{name}.docx')