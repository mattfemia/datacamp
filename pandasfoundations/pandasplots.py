##### Plotting series with pandas 

# Create a plot with color='red'
df.plot(color='blue')

# Add a title
plt.title("Temperature in Austin")

# Specify the x-axis label
plt.xlabel("Hours since midnight August 1, 2010")

# Specify the y-axis label
plt.ylabel("Temperature (degrees F)")

# Display the plot
plt.show()




##### Plotting Dataframes + Subplots

# Plot all columns (default)
df.plot()
plt.show()

# Plot all columns as subplots
df.plot(subplots=True)
plt.show()

# Plot just the Dew Point data
column_list1 = ['Dew Point (deg F)']
df[column_list1].plot()
plt.show()

# Plot the Dew Point and Temperature data, but not the Pressure data
column_list2 = ['Temperature (deg F)','Dew Point (deg F)']
df[column_list2].plot()
plt.show()