import matplotlib.pyplot as plt


# Normal line plot
year = [1, 2, 3, 4, 5]
data = [100, 200, 300, 700, 1000]

plt.plot(year, data)

plt.show()

# Scatter plot

plt.scatter(year, data)
plt.show()


# Histogram

plt.hist(year, bins=5)


# Customization

plt.xlabel("Year")
plt.ylabel("Data")
plt.title("Data in Years")
plt.yticks([0, 200, 400, 600, 800, 1000], ["0AD", "200AD", "400AD", "600AD", "800AD", "1000AD"])
plt.scatter(year, data, alpha=0.8)
plt.grid(True)
