import matplotlib.pyplot as plt


xpoint=[1,2,3,4,5,6,7]

ypoint=[1,2,3,4,5,6,7]


# plt.plot(xpoint,ypoint,marker='X',ls='dotted')
# plt.plot(xpoint,ypoint,marker='X',ls='solid')

plt.plot(xpoint,ypoint,marker='X',ls='dashed',color='r',alpha=0.0)
# plt.plot(xpoint,ypoint,marker='X',ls='dashdot')
# plt.plot(xpoint,ypoint,marker='X',ls='None')

plt.show()

#ls-solid,dotted,dashed,dashdot,None