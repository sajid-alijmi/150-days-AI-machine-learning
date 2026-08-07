a = 5
b = 10
# f- String

#print(f"sum of {a} & {b} is {a+b}")



'''nums.append(4)
nums.insert(2, 10)

nums.sort()

nums.reverse()'''
nums = [1, 2, 3, 10, 4]

'''x = 10
idx = 0

for val in nums:
 if(val == x): 
    print(f"x found at idx = {idx}")
    break
 idx += 1'''
'''
tup = (1, 2, 3, 4, 5, "abc", 3.14)

print(tup[2])'''

'''info = {
    "name": "shardha",
    "cgpa": 9.2,
    "subjects": ["math", "science"],
    3.14: "PI"
}

print(info["name"])'''

#sets 

'''s = {1,2,2,2,3}
s.add(5)

print(s)'''

'''s1 = {1, 2, 3, 4, 5}
s2 = {4,5,8,9,10}

print(s1.union(s2))'''

info = [
    ("Alice", "math"),
    ("bob", "science"),
    ("Alice", "science"),
    ("Charli", "math"),
    ("Bob", "math"),
    ("Alice", "english"),
    ("Charlie", "english"),
]

unique_courses = set()
for tup in info:
    unique_courses.add(tup[1])

print(unique_courses)