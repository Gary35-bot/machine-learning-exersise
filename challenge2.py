import numpy as np
import matplotlib.pyplot as plt
# histogram / bin vs Numbers
nums = ([0.5, 0.7, 1.,  1.2, 1.3, 2.1])
bins = ([0, 1, 2, 3])

print("nums: ", nums)
print("bins: ", bins)
print("Result:", np.histogram(nums, bins))
plt.title("Histogram of nums against bins")
plt.xlabel("Nums")
plt.ylabel("bins")

plt.hist(nums, bins=bins)
plt.show()
