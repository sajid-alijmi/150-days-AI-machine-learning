import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
sns.get_dataset_names()
# scatter plot 
tips = sns.load_dataset("tips")

sns.scatterplot(
    data=tips,
    x = "total_bill",
    y = "tip",
    hue="time"
)
#line plot 
sns.lineplot(
    data= tips,
    x = "total_bill",
    y = "tip"
)

# line plot
flights = sns.load_dataset("flights")

sns.lineplot(
    data = flights,
    x = "year",
    y = "passengers"
)
flights.head()

# bar plots
sns.barplot(
    data = tips,
    x = "day",
    y = "tip",
    hue ="sex"
)
sns.boxplot(
    data = tips,
    x = "day",
    y = "tip",
    hue ="sex"
)

penguins = sns.load_dataset("penguins")

sns.histplot(
    data = penguins,
    x = "body_mass_g",
    bins = 30
)

flights_pivot = flights.pivot(index="month", columns="year", values="passengers")
sns.heatmap(
    flights_pivot,
    cmap = "coolwarm",
    annot=True,
    fmt="d"
)
plt.title("passengers Heatmap")
plt.tight_layout()

fig, ax = plt.subplots()

sns.lineplot(
    data = tips,
    x="day",
    y="total_bill",
    marker = "o",
    hue="sex",
    ax = ax,
    errorbar=None
)
ax.set_title("avg bill value for each day")
ax.set_xlabel("Days")
ax.set_ylabel("Total Bill Amount")
fig.tight_layout()