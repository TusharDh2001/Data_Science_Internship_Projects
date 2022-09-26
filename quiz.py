print("You get 1 point for correct answer and none for wrong\n")
print("There are 10 questions\n")
print("For yes press Y")
print("For no press N")
c=0
a=input("Do you wnat to play a Game\n")
if a=='Y':
	print("--------------Ques1---------------")
	a=input("In what country was Elon Musk born?\n")
	if a.upper()=="SOUTH AFRICA":
		print("Correct")
		c=c+1
	else:
		print("Wrong")
	print("--------------Ques2---------------")
	a=input("How many hearts does an octopus have?\n")
	if a.upper()=="3":
		print("Correct")
		c=c+1
	else:
		print("Wrong")
	print("--------------Ques3---------------")
	a=input("What planet is closest to the sun?\n")
	if a.upper()=="MERCURY":
		print("Correct")
		c=c+1
	else:
		print("Wrong")
	print("--------------Ques4---------------")
	a=input("What is atomic number of Hydrogen?\n")
	if a.upper()=="1":
		print("Correct")
		c=c+1
	else:
		print("Wrong")
	print("--------------Ques5---------------")
	a=input("what is tool used to monitor network?\n")
	if a.upper()=="WIRESHARK":
		print("Correct")
		c=c+1
	else:
		print("Wrong")
	print("--------------Ques6---------------")
	a=input("Which festival is festival of colors?\n")
	if a.upper()=="HOLI":
		print("Correct")
		c=c+1
	else:
		print("Wrong")
	print("--------------Ques7---------------")
	a=input("Which is the highest mountain peak?\n")
	if a.upper()=="MOUNT EVEREST":
		print("Correct")
		c=c+1
	else:
		print("Wrong")
	print("--------------Ques8---------------")
	a=input("Planet in out solar system that has rings?\n")
	if a.upper()=="SATURN":
		print("Correct")
		c=c+1
	else:
		print("Wrong")
	print("--------------Ques9---------------")
	a=input("What is the latest version of Python?\n")
	if a.upper()=="3.10.7":
		print("Correct")
		c=c+1
	else:
		print("Wrong")
	print("--------------Ques10---------------")
	a=input("Who is the main character of One Piece?\n")
	if a.upper()=="LUFFY":
		print("Correct")
		c=c+1
	else:
		print("Wrong")
print("Your score is :",c)
