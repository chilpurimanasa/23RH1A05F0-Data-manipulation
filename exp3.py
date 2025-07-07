#charts in python
#pip install matplotlib
import matplotlib.pyplot as plt
#Line plot 
#plt.plot([1,2,3],[2,4,6])
#plt.title("Line plot chart")
#plt.xlabel("X-axis")
#plt.ylabel("Y-axis")
#plt.grid(True)
#plt.show()

#bar chart
#label=["A","B","C","D","E"]
#sales=[100,200,500,700,600]
#plt.bar(label,sales,color="pink")
#plt.title("Sales report")
#plt.ylabel("Values of sales")
#plt.xlabel("Brands")
#plt.show()

#pie chart
#sizes=[20,30,40,50,60]
#plt.pie(sizes,labels=labels,autopct="%1.1f%%",startangle=90)
#plt.title("Product pie report")
#plt.show()

#histogram
gender=['m','f','m','f','f']
plt.hist(gender,bins=2,color="orange",edgecolor="black")
plt.title("Gender report")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()