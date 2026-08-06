'''word = "artificiail"
count = 0

for ch in word :
  if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
       
     count += 1

print("ans =", count)


for i in range(1, 10, 2):
    print(i)'''

sum = 0

for i in range(1, 6):
    sum += i
print("sum =", sum)

def hello():
    print("hello")
    print("from python")
#hello() 

# function definition 
'''
def sum(a, b): 
    s = a+b
    return s
ans = sum(3, 4)
print(ans)'''

def calc_avg(a ,b, c):
    sum = a+b+c
    return sum/3
#print(calc_avg(1, 2, 3,))
'''
def calc_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
#n = int(input("enter n: "))
#print(calc_factorial(n))'''

'''word = "python"
word2 = "I love"

print(word +" " + word2)'''

# slicing
'''
word = "python"

print(word[2:4])'''
#list
marks = [99, 89, 100, 65, 92]
print(marks[2])
#formating

a=10
b=30
sum = a+b
print("language is {}".format("python"))
print("sum is {}".format(sum))