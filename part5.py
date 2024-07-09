# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20191136

# Date:  10/12/2020


#Creating variables
count1 = 0
count2 = 0
count3 = 0
count4 = 0

#Creating lists
list1 =[]


def process():
	"""This function prints the progression outcome."""

	#Since the following variables are reassigning, global keyword is used.
	global count1
	global count2
	global count3
	global count4

	for i in list1:#Traverse the list1 by using for loop
		if i[0] == 120:
			print("Progress")
			count1+=1
		elif i[0] == 100:
			print("Progress (module trailer)")
			count2+=1
		elif i[2] >= 80 :
			print("Exclude")
			count3+=1
		else:
			print("Do not Progress - module retriever")
			count4+=1

def histogram():
	"""This function creates the horizontal histogram"""

	outcome = 0
	count_list = [count1,count2,count4,count3]
	header_list = ["Progress ","Trailing ","Retriever","Excluded "]

	for i in range(4):
		print(header_list[i],count_list[i],":",count_list[i] * "*")
		outcome = outcome + count_list[i]
	print()
	print(outcome,"outcomes in total.")



	
#Two-dimensional list to hold the data
list1 = [[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]
process()#calling process function
print()
print("--------------------------------")
histogram()#Calling histogram function
print("--------------------------------")

	
