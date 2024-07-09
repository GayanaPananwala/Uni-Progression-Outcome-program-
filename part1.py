# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20191136         
  
# Date:  10/12/2020




#Creating variables 
pass1 = 0 
defer = 0
fail  = 0 
total = 0

need_to_continue = "yes" #This can be used to control inputs for giving an accurate output 


def print_errors():
	"""This function checks the validity of inputs."""

	if need_to_continue == "no" or total != 120:
		print("Invalid inputs.Please try again with valid inputs.")
	


def outcome():
	"""This function prints the progression outcome."""

	if  total == 120 and need_to_continue == "yes":			
		if pass1 == 120 :
			print("Progress")
		elif pass1 == 100:
			print("Progress (module trailer) ")
		elif fail >= 80:
			print("Exclude")	
		else:
			print("Do not progress - module retriever")
				



try:
	print("------------------------------------------------") #To display the output in a pleasant way

	pass1 = int(input("Please enter your credits at pass : "))#Taking user inputs for pass 

	if pass1  % 20 != 0 or pass1 > 120 or pass1 < 0:#checking the validity of credits at pass
		need_to_continue = "no"
							
	else:
		defer = int(input("Please enter your credits at defer : "))#Taking user inputs for defer
		need_to_continue ="yes" 

		if defer  % 20 != 0 or defer > 120 or defer < 0:#checking the validity of credits at defer
			need_to_continue = "no"

		else:
			fail = int(input("Please enter your credits at fail : "))#Taking the user inputs for fail 
			need_to_continue ="yes"

			if fail  % 20 != 0 or fail > 120 or fail < 0:#checking the validity of credits at fail
				need_to_continue = "no"
			else:
				need_to_continue = "yes"

except ValueError:#If student enter an input in another data type except integer this line will be executed 
		need_to_continue = "no"

	
total = pass1 + defer + fail#Calculating the total of credits
print()
#Calling the outcome and print_errors functions
outcome()
print()
print_errors()
print("------------------------------------------------")



