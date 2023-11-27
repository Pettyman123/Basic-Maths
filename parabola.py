import math
from numpy import *
from matplotlib.pyplot import *

x = linspace(-10,10,5000)
y = x**2 + 2*x + 4
plot(x,y)
xlabel("xaxis") 
ylabel("yaxis")
print(x)
show()