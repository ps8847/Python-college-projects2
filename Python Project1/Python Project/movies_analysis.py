import csv
from os import system
r=[]
f= open(r"Dataset-movies.csv","r")
csvreader= csv.reader(f)
rows=[]
for i in csvreader :
    rows.append(i)

def main():
	system('cls')
	choice=int(input('''Case Study II : Movies Dataset
		1. List the movie names and rating of all movies having a rating greater than 4.3
		2. List the movie names and release year of all movies released before 1990 and do not have a null in the rating
		3. List the movie names and rating of all movies in which movie name contains the word “boys” or the word “wild”
		4. List all movie names and release year for the movie names beginning with ‟A” and rating is null and release year is not between 1980 and 1995
		5. Count the number of movies released in the year 1989 and duration is more than 1½ hours
		0. Exit
		Enter : '''))
	return choice

choice = main()

while choice != 0:

	# Query1: List the movie names and rating of all movies having a rating greater than 4.3
	if choice == 1:
		system('cls')
		c=0
		for i in rows:
		 if i[3] not in (None,''):
		     if float(i[3])>4.3:
		      print("Movie Name :",i[1].ljust(50),"| Movie Rating :".center(15),i[3])
		      c+=1
		print("Number of Records : ",c)
		input()	

	# Query2: List the movie names and release year of all movies released before 1990 and do not have a null in the rating
	elif choice == 2:
		system('cls')
		c=0
		for i in rows:
		   if i[3] not in (None,''):
		        if int(i[2])<=1990:
		            c+=1
		            print("Movie Name :",i[1].ljust(70),"| Release Year :",i[2].ljust(5),"| Movie Rating :".center(15),i[3])
		print("Number of Records : ",c)
		input()

	#Query3: List the movie names and rating of all movies in which movie name contains the word “boys” or the word “wild”.
	elif choice == 3:
		system('cls')	
		c=0
		for i in rows:
		    if 'boys' in i[1] or 'wild' in i[1]:
		        print("Movie Name :",i[1].ljust(50),"| Movie Rating :".center(15),i[3])
		        c+=1
		print("Number of Records : ",c)
		input()
		
	#Query4: List all movie names and release year for the movie names beginning with ‟A” and rating is null and release year is not between 1980 and 1995.
	elif choice == 4:	
		system('cls')
		c=0
		for i in rows:
		    if i[3] in (None,''):
		        if i[1].startswith('A') :
		            if not  (int(i[2])>1980 and int(i[2])<1995)  :
		                print("Movie Name :",i[1].ljust(80),"| Release Year :",i[2].ljust(5),"| Movie Rating :".center(15),i[3])
		                c+=1
		print("Number of Records : ",c)
		input()

	#Query5: Count the number of movies released in the year 1989 and duration is more than 1½ hours
	elif choice == 5:
		system('cls')
		c=0
		for i in rows:
		  if i[4] not in (None,''):
		   if i[2]== str(1989) and int(i[4])>=5400:
		    c+=1
		print(f" The number of movies released in the year 1989 and having duration  more than 1½ hours : {c}")
		input()

	else:
		print("Invalid choice")
		input()

	choice = main()
