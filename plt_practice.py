import matplotlib.pyplot as plt
import numpy as np
def f(t):
    s1=np.cos(2*np.pi*t)
    e1=np.exp(-t)
    return s1*e1
t1=np.linspace(0,2*np.pi,1000)
l=plt.plot(t1,f(t1),'ro')
plt.setp(l,markersize=5)
plt.setp(l,markerfacecolor='C0')
plt.show()
N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()