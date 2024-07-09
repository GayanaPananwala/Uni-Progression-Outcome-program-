# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20191136         
  
# Date:  10/12/2020


#Creating variables
total = 0
pass1 = 0 
defer = 0
fail  = 0 
count1 = 0 
count2 = 0
count3 = 0
count4 = 0

valid = "yes"#This can be used to control inputs for giving an accurate output 
need_to_continue = "y"#This variable can be used to control the while loop


def process():
	"""This function prints the progression outcome
	and checks the validity of total."""

	#Since the following variables are reassigning, global keyword is used.
	global count2
	global count3
	global count4
	global count1

	if total != 120  and  valid == "yes" :
		print("incorrect total")

	if  total == 120 and valid == "yes":
										
		if pass1 == 120 :
			print("Progress")			
			count1+=1
																											
		elif pass1 == 100:
			print("Progress (module trailer) ")
			count2+=1

		elif fail >= 80:
			print("Exclude")
			count3+=1

		else:
			print("Do not progress - module retriever")	
			count4+=1

		
def horizontal_histogram():
	"""This function creates the horizontal histogram."""

	
	outcome = count1+count2+count3+count4
	list1 = [count1,count2,count4,count3]
	list2 = ["Progress ","Trailer  ","Retriever","Excluded "]
	for i in range(4):
		print(list2[i],list1[i],":",list1[i] * "*")
			
	print(outcome,"outcomes in total.")


def vertical_histogram():
	"""This function creates the vertical histogram."""
	

	list1 =[count1,count2,count4,count3]
	outcome = count1+count2+count3+count4
	print(f'|{"Progress":4} {count1} | {"Trailing":4} {count2} | {"Retriever":4} {count4} | {"Excluded":4} {count3} |')
	for i in range(1,max(list1)+1):
		for x in list1:
			if x>= i:	
				print((f'    {"*":9}'),end=" ")
			else:
				print((f'    {" ":9}'),end=" ")
		print()
	print(outcome,"outcomes in total.")

	
	
	
while need_to_continue == "y":#This loop allows a staff member to continue the program.
	try:
		pass1 = int(input("Please enter your credits at pass : "))#Taking user inputs for pass

		if pass1  % 20 != 0 or pass1 > 120 or pass1 < 0:#checking the validity of credits at pass
			valid = "no"
			print()
			print("Out of range")
												
		else:
			defer = int(input("Please enter your credits at defer : "))#Taking user inputs for defer
			valid = "yes"

			if defer  % 20 != 0 or defer > 120 or defer < 0:#checking the validity of credits at defer
				print()
				print("Out of range")
				valid = "no"

			else:
				fail = int(input("Please enter your credits at fail : "))#Taking user inputs for fail
				valid = "yes"

				if fail  % 20 != 0 or fail > 120 or fail < 0:#checking the validity of credits at fail
					print()
					print("Out of range")
					valid = "no"
				else:
					valid = "yes"


	except ValueError:
			print()
			print("Integer required")#If student enter an input in another data type except integer this line will be executed 
			valid = "no"


	total = pass1 + defer + fail#Calculating the total of creditsz

	print()	#Printing a new line 
	process()#Calling the process function
	print()
	
	need_to_continue = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results (y/q): ").lower()
			
	if need_to_continue =="q":
			
		#if you want to create a horizontal histogram, you can convert following comments as statements
		#print()
		#print("----------------------------------------------------")
		#print("Horizontal Histogram")
		#print()
		#horizontal_histogram()#Calling the horizontal_histogram function
		#print("----------------------------------------------------")		

		print()
		print("----------------------------------------------------")
		print("Vertical Histogram")
		print()
		vertical_histogram()#Calling the vertical_histogram function
		print("----------------------------------------------------")
			
		
	#Printing errors
	if need_to_continue != "y" and need_to_continue != "q":
		print("Invalid inputs! Please try again with valid inputs.")
			


