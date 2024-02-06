import numpy as np

generator = np.random.default_rng(80085)
scores = np.round(generator.uniform(low=30, high=100, size=15))

np.set_printoptions(linewidth=100000)
# print(scores)
# [68. 36. 76. 57. 56. 54. 63. 64. 36. 88. 80. 82. 84. 76. 42.]

scores[(scores < 60).nonzero()[0][:3]] = 0

print(scores)