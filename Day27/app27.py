import matplotlib.pyplot as plt 
x = [1,2,3,4]
y = [5, 6, 7, 8]

plt.plot(x, y)
plt.show()# Real data

#oscar winner Movies
oscar_movies = [
"the Dark Knight",
"the Hurt Locker",
"The king' speech",
"the Artist",
"Argo"
]
years = [2008, 2009, 2010, 2011, 2012]
oscar_revenu = [1005, 170, 427, 133, 232]

#plot
plt.plot(years, oscar_revenu)
plt.title("Oscar Movies Revenu in each year")
plt.xlabel("years")
plt.ylabel("Revenue (in $M)")

#non -Oscar winner Movies
non_oscar_movies = ["slumdog millinaire", "avatar","Inception", "hugo", "lincoln"]
non_oscar_revenu = [378, 2788, 829, 185, 275]