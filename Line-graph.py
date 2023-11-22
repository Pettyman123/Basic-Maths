from matplotlib.pyplot import *
data = {'apple':10, 'orange':20, 'lemon':15, 'lime':5,'cabbage':25}
names = list(data.keys())
values = list(data.values())
plot(names, values)
show()