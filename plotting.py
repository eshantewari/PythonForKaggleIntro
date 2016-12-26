import matplotlib.pyplot as plt
import numpy as np


#When running the program, you must exit out of the graph for the next one to appear
plt.plot([1,2,3,4],[1,4,9,16]) #simple line plot
plt.show() #show the plot


plt.scatter([1,2,3,4],[1,4,9,16]) #simple scatter plot
plt.grid(True) #add Gridlines
plt.show()


plt.scatter([1,2,3,4],[10,100,1000,10000], s = [10,20,30,40]) #the s parameter sets the size of the scatter dots
plt.yscale('log') #make the y scale logarithmic
plt.xlabel('xaxis') #x axis label
plt.ylabel('yaxis') #y axis label
plt.title('title') #title
plt.xticks([2,4], ["two","four"]) #rename x axis labels
plt.show()


data = np.random.randint(1, high = 10, size = 50) #Create a random array of integers between 1 and 10
plt.hist(data, bins = 5) #create a histogram with 5 bins
plt.show()
