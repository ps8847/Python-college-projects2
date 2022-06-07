import csv
from os import system

def start():
  system('cls')
  print("Case Study 1: Student Database")
  choice = int(input(''' \t\t1. Printing all Student's Data
                2. Display all the students from a particular state/country
                3. Display all students from a particular state and born in a particular month
                4. Display all students with given CGPA
                5. Display all students whose name starts with a particular letter and a particular year of birth
                0. Exit
                Now Enter your Choice : '''))
  return choice

choice=start()

while choice != 0:
  
  #List all the student's data
  if choice == 1:
    system('cls')
    f = open(r"Student_Database.csv","r")
    csvreader = csv.reader(f)
    header = next(csvreader)
    print("-+------------------+----------------+--------+----------------+-----------------+----------------+-------+-")
    print(' |',header[0].center(16),'|',header[1].center(14),'|',header[2].center(6),'|',header[3].center(14),'|',header[4].center(15),'|',header[5].center(14),'|',header[6].center(5),'| ')
    print("-+------------------+----------------+--------+----------------+-----------------+----------------+-------+-")
    for i in csvreader:
      print(' |',i[0].center(16),'|',i[1].center(14),'|',i[2].center(6),'|',i[3].center(14),'|',i[4].center(15),'|',i[5].center(14),'|',i[6].center(5),'| ')
    print("-+------------------+----------------+--------+----------------+-----------------+----------------+-------+-")
    input()

  #Display all the students from a particular state/country
  elif choice == 2:
    system('cls')
    f = open(r"Student_Database.csv","r")
    csvreader = csv.reader(f)
    header = next(csvreader)
    flag = 0
    n=input("Enter  the name of the State/Country : ").upper()
    for i in csvreader:
      if i[5] == n:
        print(header[0],":",i[0].center(16),'|',header[1],":",i[1].center(9),'|',header[4],":",i[4].center(15),'|',header[5],":",i[5].center(10))
        flag = 1
    if flag == 0:
      print("Record not found")
    input()

  #Display all students from a particular state and born in a particular month
  elif choice == 3:
    system('cls')
    f = open(r"Student_Database.csv","r")
    flag = 0
    csvreader = csv.reader(f)
    header = next(csvreader)
    n = input(" enter  state : ").upper()
    p = int(input(" enter month of birth : "))
    for i in csvreader:
      if i[5] == n and int(i[3][3:5]) == p:
          print(header[0],":",i[0].center(16),'|',header[1],":",i[1].center(9),'|',header[3],":",i[3].center(12),'|',header[5],":",i[5].center(10))
          flag = 1
    if flag == 0:
      print("Record not found")
    input()

  #Display all students with a given CGPA    
  elif choice == 4:
    system('cls')
    f = open(r"Student_Database.csv","r")
    csvreader = csv.reader(f)
    header = next(csvreader)
    flag = 0
    n=eval(input("Enter CGPA : "))
    for i in csvreader:
      if  int(int(i[6]))== n:
        print(header[0],":",i[0].center(16),'|',header[1],":",i[1].center(9),'|',header[6],":",i[6].center(6))
        flag =1
    if flag == 0:
      print("Record not found")
    input()

  #Display all students whose name starts with a particular letter and a particular year of birth
  elif choice == 5:
    system('cls')
    flag = 0
    f = open(r"Student_Database.csv","r")
    csvreader = csv.reader(f)
    header = next(csvreader)
    n=input("Enter Char : ").upper()
    p=input("Enter Year of BIRTH : ")
    for i in csvreader:
      if i[0].startswith(n) and i[3][6:] == p:
          print(header[0],":",i[0].center(16),'|',header[1],":",i[1].center(9),'|',header[3],":",i[3].center(12))
          flag =1
    if flag == 0:
      print("Record not found")
    input()

  else:
    system('cls')
    print("Input Invalid")
    input()
  
  choice=start()


  
