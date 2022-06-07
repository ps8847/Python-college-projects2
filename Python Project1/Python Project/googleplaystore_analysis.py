import csv
from os import system
gps = open(r"googleplaystore.csv",encoding=" utf8")
csv_reader=csv.reader(gps)
header=next(csv_reader)
r=[]
for i in csv_reader:
	r.append(i)

def main():
	system('cls')
	choice=int(input('''Google Play Store Apps Data Analysis
		1. Display all the Data
		2. Check how many Apps have installs more than 1Billions
		3. Check if app name contains word 'camera' in its name
		4. Display the name and rating of the apps having rating more than 4.8
		5. Display the name of the apps having no of reviews greater then 1 million  
		6. Display the names and rating of the apps having EDUCATION as their genre and rating of 5
		7. Display the apps name with Teen content rating
		8. Count Free and Paid Apps
		9. Print app's name with more than 90M size
		10. Display apps with price more than 50$
		11. Display APP name having install more than 50,000 and with content rating teen and is Paid
		0. Exit
		Enter here : '''))
	return choice

choice=main()

while choice != 0:

	#Display all the data of the file.
	if choice == 1:
		system('cls')
		c=0
		print(header[0].ljust(30),header[1].ljust(7),header[2].ljust(9),header[3].ljust(18),header[4].ljust(12),header[5].ljust(5),header[6].ljust(6),header[7].ljust(15),header[8].ljust(1))
		print("------------------------------------------------------------------------------------------------------------------------------------")
		for i in r:
			c+=1
			print(i[0][:30].ljust(30),i[1].ljust(7),i[2].ljust(9),i[3].ljust(18),i[4].ljust(12),i[5].ljust(5),i[6].ljust(6),i[7].ljust(15),i[8].ljust(1))
		print("Number of Records : ",c)
		input()

	#check how many apps have installs more than 1B
	elif choice == 2:
		system('cls')
		c=0
		print(header[0].ljust(30),'|',header[2].ljust(10),'|',header[4].ljust(12))
		print("-------------------------------+------------+---------------")
		for i in r:
			a=i[4][:-1]
			a=a.split(",")
			a=''.join(a)
			a=int(a)
			if a>= 1000000000:
				print(i[0][:30].ljust(30),'|',i[2].ljust(10),'|',i[4].ljust(12)) 
				c+=2
		print("Number of Records : ",c)
		input()
	
	#check if app name contains CAmera in it
	elif choice == 3:
		system('cls')
		c=0
		print(header[0].ljust(60),'|',header[4].ljust(12))
		print("-------------------------------------------------------------+---------------")
		for i in r:
			if 'camera' in i[0] or 'Camera' in i[0]:
				print(i[0].ljust(60),'|',i[4].ljust(12)) 
				c+=1
		print('Number of Records : ',c)
		input()
	
	#Display the names and rating of the apps having rating more than 4.8.
	elif choice == 4:
		system('cls')
		c=0
		print(header[0].ljust(60),'|',header[1].ljust(8))
		print("-------------------------------------------------------------+---------------")
		for i in r:
			if i[1] not in (None,'NaN'):
				if float(i[1]) > 4.8:
					print(i[0].ljust(60),'|',i[1].ljust(8))
					c+=1
		print("Number of Records : ",c)
		input()
		
	#Display the name of the apps having no of reviews greater then 1 million  
	elif choice == 5:
		system('cls')
		c=0
		print(header[0].ljust(60),'|',header[2].ljust(12))
		print("-------------------------------------------------------------+---------------") 
		for i in r:
			if int(i[2])>1000000:
				print(i[0].ljust(60),'|',i[2].ljust(12))
				c+=1
		print("Number of Records : ",c)
		input()
	
	#Display the names and rating of the apps having EDUCATION as their genre and rating of 5.
	elif choice == 6:
		system('cls')
		c=0
		print(header[0].ljust(60),'|',header[1].ljust(12),'|',header[8])
		print("-------------------------------------------------------------+--------------+---------------") 
		for i in r:
			if i[8]=='Education' and i[1]==str(5):
				print(i[0].ljust(60),'|',i[1].ljust(12),'|',i[8])
				c+=1
		print("Number of Records : ",c)
		input()
	
	# Display the apps with Teen content rating
	elif choice == 7:
		system('cls')
		c=0
		print(header[0].ljust(60),'|',header[7].ljust(12))
		print("-------------------------------------------------------------+---------------") 
		for i in r:
			if i[7] == 'Teen':
				c+=1
				print(i[0].ljust(60),'|',i[7].ljust(12))
		print("Number of Records : ",c)
		input()
	
	#count free and paid apps
	elif choice == 8:
		system('cls')
		c1=0
		c2=0
		for i in r:
			if i[5] == "Free":
				c1+=1
			else:
				c2+=1
		print("NUmber of Free Apps : ",c1)
		print("NUmber of Paid Apps : ",c2)
		input()

	#Print app's name with more than 90M size
	elif choice ==  9:
		system('cls')
		c=0
		print(header[0].ljust(60),'|',header[3].ljust(12))
		print("-------------------------------------------------------------+---------------") 
		for i in r:
			if i[3] not in ('Varies with device','0'):
				a=i[3][:-1]
				a=a.split(",")
				a="".join(a)
				if float(a) >= 90 and i[3].endswith('M'):
					print(i[0].ljust(60),'|',i[3].ljust(12))
		print("Number of Records : ",c)
		input()		

	#Display apps with price more than 50$
	elif choice == 10 :
		system('cls')
		c=0
		print(header[0].ljust(60),'|',header[6].ljust(12))
		print("-------------------------------------------------------------+---------------") 
		for i in r:
			if i[6] != '0':
				a=i[6][1:]
				a=a.split(",")
				a="".join(a)
				if float(a) >= 50:
					print(i[0].ljust(60),'|',i[6].ljust(12))
					c+=1
		print("Number of Records : ",c)
		input()		

	#Display APP name having install more than 50,000 and with content rating teen and is Paid
	elif choice == 11:
		system('cls')
		c=0
		print(header[0].ljust(60),'|',header[4].ljust(12),'|',header[5].ljust(6),'|',header[7])
		print("-------------------------------------------------------------+--------------+--------+----------------") 
		for i in r:
			a=i[4][:-1]
			a=a.split(",")
			a=''.join(a)
			if int(a)>= 50000 and i[7]=='Teen' and i[5] == 'Paid':
				print(i[0].ljust(60),'|',i[4].ljust(12),'|',i[5].ljust(6),'|',i[7])
				c+=1
		print("Number of Records : ",c)
		input()		

	else:
		print("Invalid Input")	

	choice=main()