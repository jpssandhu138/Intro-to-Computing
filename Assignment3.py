#Q1

sentence=input('Write a sentence ')
space=sentence.count(" ")
#c=print(b+1)

if space>=1:
    print(space+1)

else:
    print(len(sentence))

#Q2

year=int(input('Enter the year '))

if year%400==0:
    leap_year= True
elif year%100==0:
    leap_year= False
elif year%4==0:
    leap_year= True
else:
    leap_year= False

month=int(input('Enter the month '))

if month in [1,3,5,7,8,10,12]:
    month_length=31

elif month==2 and leap_year==True:
    month_length=29
elif month==2 and leap_year==False:
    month_length=28
elif month>13:
    print('Please input the right month')
elif month in [4,6,9,11]:
    month_length=30

day=int(input('Enter the date '))

if day<month_length:
    day+=1
elif day==month_length and month<12:
    day=1
    month+=1
if day==month_length and month==12:
    day=1
    month=1
    year+=1

print("The next date is:%d-%d-%d." % (day, month, year))

#Q3

lower_range=int(input("Enter the lower range:"))
upper_range=int(input("Enter the upper range:"))
square=[(x,x**2) for x in range(lower_range,upper_range+1)]
print(square)

#Q4

grade=float(input("Enter the marks "))

if grade >=0 and grade <25:
    grade1='F'
    print("Your grade is: "+grade1)

elif grade >=25 and grade < 45:
    grade1='E'
    print("Your grade is: "+grade1)

elif grade >=45 and grade < 50:
    grade1='D'
    print("Your grade is: "+grade1)

elif grade >=50 and grade < 60:
    grade1='C'
    print("Your grade is: "+grade1)

elif grade >= 60 and grade < 80:
    grade1='B'
    print("Your grade is: "+grade1)

elif grade >=80 and grade <= 100:
    grade1='A'
    print("Your grade is: "+grade1)

else:
    print("Marks not in range")

#Q5

string=('ABCDEFGHIJK')
i=0
while len(string)-i*2>=1:
    print(' '*i, string[0:len(string)-i*2])
    i+=1

#Q6

repeat="Y"
dic={}
dic2={}

liste=["Y","y","n","N"]
while repeat=="Y" or repeat=="y":
    name = str(input("Enter student name : "))
    sid = int(input("Enter student SID : "))
    if sid<0:
        print("\nError\nSID can't be negative\n")
    else:
        dic.update({sid: name})
        dic2.update({name:sid})
        repeat = str(input("Enter Y to continue or N to end : "))
    if repeat=="N" or repeat=="n":
        break
    elif (not (repeat in liste)):
        print("\nError\nPlease enter valid input['Y' or 'N']")
        repeat=str(input("\nEnter Y to continue or N to end : "))
# a

print("\nQ.6(a)")
print("The Dictionary containing {'SID':'Name'} is shown below")
print(dic)
# b

print("\nQ.6(b)")
list_k=sorted(dic2)
dic3={}
for ele in list_k:
    dic3.update({dic2.get(ele):ele})
print("The Dictionary after sorting according to name : ")
print(dic3)
# c

print("\nQ.6(c)")
sort_dic = sorted(dic)
dic4 = {}
for va in sort_dic:
    dic4.update({va: dic.get(va)})
print("The Dictionary after sorting according to SID : ")
print(dic4)
# d
print("\nQ.6(d)")

enter_sid = int(input("Enter SID to get name of student : "))

output_name = str(dic.get(enter_sid))

print(f"Name of student with SID {enter_sid} is {output_name}.")


#Q7

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

nterms = int(input('Enter the number of terms'))

list1=[]
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fibo(i))
       list1.append(fibo(i))
print(sum(list1)/len(list1))

#Q8

set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

#a

a=set1^set2
print(a)

#b

b1=set1-set2-set3
b2=set2-set1-set3
b3=set3-set1-set2
b=b1|b2|b3
print(b)

#c

set_union=set1|set2|set3
c1=set1&set2&set3
c = set_union-b-c1
print(c)

#d

set={1,2,3,4,5,6,7,8,9,10}
print(set-set1)

#e

set={1,2,3,4,5,6,7,8,9,10}
print(set-set1-set2-set3)