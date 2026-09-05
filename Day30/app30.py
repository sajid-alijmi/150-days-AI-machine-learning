# Box plot
data = [7,8,5,6,9,4,10, 12, 15]
plt.boxplot(data, vert=False, showmeans=True, whis=2.0)
plt.grid(True)

group1 = np.random.normal(50, 10, 100)
group2 = np.random.normal(60, 15, 100)

plt.boxplot([group1, group2], tick_labels=["group1", "group2"], showmeans=True)
plt.grid()
plt.show()

#stack plot 
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
direct = [50,60,70,80,90,100,110]
organic = [30,40, 50,55, 60, 70,80]
social = [20, 25, 30, 35, 40, 50,60]
# plt.pie([direct[0], organic[0], social[0]],
#         labels=["direct", "organic", "social"], autopct="%1.1f%%")
plt.stackplot(days, direct, organic, social, labels=["direct", "organic", "social"])
plt.title("Marketing data for the week")
plt.xlabel("Days")
plt.ylabel("# of customer")
plt.legend()

# subploats 
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y1 = [np.sqrt(i) for i in x] #square Root
y2 = [i*2 for i in x] #double
y3 = [i**2 for i in x] #square
y4 = [i**3 for i in x] #cubes

plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title("plot1 - squre root")

plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.title("plot2 - double")

plt.subplot(2, 2, 3)
plt.plot(x, y3)
plt.title("plot3 - squres")

plt.subplot(2, 2, 4)
plt.plot(x, y4)
plt.title("plot4- cubes")

plt.tight_layout()