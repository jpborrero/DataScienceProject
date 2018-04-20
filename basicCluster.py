

labelOne = ''
labelTwo = ''

plt.title(labelOne+' '+labelTwo)
plt.xlabel(labelOne)
plt.ylabel(labelTwo)
plt.plot(x_1, y_1, 'ro', x_2, y_2, 'bo')
plt.plot(x_s1, y_s1, 'rx', x_s2, y_s2, 'bx')
#plt.axis([0, 30, 0, 30])
plt.show()