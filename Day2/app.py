'''a = 10
b = 5
print(type(a/5))
ans = int(5+10.0) # type casting
print(type(ans))  #conversion


val = bool(10)

print(val, type(val))'''


#input function

'''a = input("enter value of a: ")
print(a)

b = input("entar a welcome :")
print(b)'''

# sum of two numbers

'''a = int(input("enter a : "))
b =int(input("enter b: "))

sum = a + b
print(sum)'''
# conditional Statement
age = 15

'''if age>= 18:
   print("you can vote")
   print("you can drive")
else:
    print("you can not vote")  

color = input("enter color: ")

if color == "red":
    print("stop")
elif color == "yellow":
    print("start")    
elif color == "green":
    print("go")

username = input("enter username: ")
password = input("enter password: ")

if (username == "admin" and password == "pass"):
    print("login succesful")
elif (username != "admin"):
    print("wrong Usernsme")  
else:
    print("wrong password")

n = int(input("enter num: "))

if(n %2 == 0):
        print("Even")
else:
        print("ODD")'''
#loops

'''while (count <= 10):
    print("hello world")
    count += 1
i =10
while(i>=1):
    print(i)
    i-=1'''
    # for loop
string = "hello"
for var in string:
    print(var)
for i in range(5):
    print(i+1)

word = "artificial intelligence"

ans = 0

for ch in word:
    if(ch == 'i'):
        ans += 1
        
    print("count of i = ", ans)