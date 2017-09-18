import matplotlib.pyplot as plt

plt.plot([2/7 * 100, 4/7 * 100, 5/7 * 100, 6/7 * 100, 6/7 * 100], [648, 916, 2062, 2631, 3585])
plt.xlabel('percentage of correctly found keyword symbols')
plt.ylabel('length of source text')
plt.show()

plt.plot([2/3 * 100, 100, 100, 100, 7/8 * 100, 8/9 * 100], [3, 4, 5, 6, 7, 8])
plt.xlabel('percentage of correctly found keyword symbols')
plt.ylabel('length of keyword')
plt.show()