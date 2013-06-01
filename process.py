import numpy as np

X = np.loadtxt(
    '/home/nelle/Projects/SCCourses-reproducible-research/my_data.txt')
X += 10
np.savetxt(
    'my_data_2.txt', X)

print "done"
