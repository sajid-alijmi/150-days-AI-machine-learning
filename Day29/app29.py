import numpy as np
import matplotlib.pyplot as plt
oscar_movies = [
    "the Dark Knight",
    "the Hurt Locker",
    "The king' speech",
     "the Artist",
    "Argo"
]

oscar_revenu = [1005, 170, 427, 133, 232]
non_oscar_movies = ["slumdog millinaire", "avatar","Inception", "hugo", "lincoln"]
non_oscar_revenu = [378, 2788, 829, 185, 275]

years = [2008, 2009, 2010, 2011, 2012]
x = np.arange(len(years))
width = 0.4
plt.bar(x-width/2, oscar_revenu, width, label = "oscar movies")
plt.bar(x+width/2, non_oscar_revenu, width, label="non oscar movies")

plt.title("Oscar vs nonOscar movies revenue")
plt.xlabel("year")
plt.ylabel("Revenue ($M)")
plt.legend()
plt.xticks(x, years)

import numpy as np
oscar_movies = [
    "the Dark Knight",
    "the Hurt Locker",
    "The king' speech",
     "the Artist",
    "Argo"
]

oscar_revenu = [1005, 170, 427, 133, 232]
plt.barh(oscar_movies, oscar_revenu)
plt.xlabel("Revenu")
plt.ylabel("Movie Names") 
 # Scatter Plots

people=["person A","Person B","Person C","Person D","person E"
    , "person F","person G","person H","person I","person J"]
age = [22, 25, 30, 35, 40, 45, 50, 55, 60, 65]
bp=[110, 115, 120, 122, 125, 130, 135, 123, 145, 150]

colors = ["green" if x < 135 else "red" for x in bp]

plt.scatter(age, bp, s=bp, cmap="OrRd", c=bp)
plt.title("Age vs BP")
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.grid()
plt.colorbar()

for i in range(len(people)): 
    plt.annotate(people[i], xy=(age[i], bp[1]), xytext=(age[i]+1, bp[i]+1))

plt.xlim(min(age), max(age)+10)
plt.ylim(min(bp), max(bp)+5) 