import matplotlib.pyplot as plt 
 
# Oscar winner Movies 
oscar_movies = [ 
    "The Dark Knight", 
    "The Hurt Locker", 
    "The King's Speech", 
    "The Artist", 
    "Argo" 
] 
 
years = [2008, 2009, 2010, 2011, 2012] 
 
oscar_revenue = [1005, 170, 427, 133, 232] 
 
# Non-Oscar winner Movies 
non_oscar_movies = [ 
    "Slumdog Millionaire", 
    "Avatar", 
    "Inception", 
    "Hugo", 
    "Lincoln" 
] 
 
non_oscar_revenue = [378, 2788, 829, 185, 275] 
 
# Plot both lines 
plt.plot(years, oscar_revenue, label="Oscar Movies") 
plt.plot(years, non_oscar_revenue, label="Non-Oscar Movies") 
 
plt.title("Oscar Movies vs Non-Oscar Movies Revenue") 
plt.xlabel("Years") 
plt.ylabel("Revenue (in $M)") 
 
plt.legend() 
plt.show()     #oscar winner Movies 
movies = [
    "the Dark Knight",
    "the Hurt Locker",
    "The king' speech",
     "the Artist",
    "Argo"
]
years = [2008, 2009, 2010, 2011, 2012]
revenu = [1005, 170, 427, 133, 232]

plt.plot(movies, revenu)
plt.title("Movies Revenue")
plt.xlabel("movies")
plt.ylabel("Revenue($M)")

plt.tight_layout()
plt.savefig("final_plot.png")  #oscar winner Movies 
oscar_movies = [
    "the Dark Knight",
    "the Hurt Locker",
    "The king' speech",
     "the Artist",
    "Argo"
]
years = [2008, 2009, 2010, 2011, 2012]
oscar_revenue = [1005, 170, 427, 133, 232]
plt.bar(years, oscar_revenue, color="green")
plt.title("Revenue in each Year oscar movies")
plt.xlabel("year")
plt.ylabel("Revenue (in $M)")
for i in range(len(years)):
 plt.text(years[i], oscar_revenue[i]+20, str(oscar_revenue[i]), ha="center")

plt.ylim(0, max(oscar_revenue)+100) 