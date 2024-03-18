import matplotlib.pyplot as plt


xpoints=[1,2,3,4,5]

ypoints=[1,2,3,4,5]

font1={'family':'serif','color':'blue','size':20}

plt.xlabel("age",fontdict=font1)
plt.ylabel("no. of students",fontdict=font1)

plt.title("Students Records",fontdict=font1)
plt.plot(xpoints,ypoints)

plt.show()