import numpy as np

X = np.loadtxt(
    '/home/nelle/Projects/SCCourses-reproducible-research/my_data.txt')

output_file = open("my_results.txt", 'wb')
output_file.write("This is my results file !\n")

output_file.write("\nThe mean of the data is: %0.2f\n" % X.mean())
output_file.write("The variance of the data is: %0.2f\n" % X.var())
