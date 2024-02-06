import numpy as np

generator = np.random.default_rng(1010)
love_scores = np.round(generator.uniform(low=0, high=100, size=10), 2)

np.set_printoptions(linewidth=100000)
# print(love_scores)
# [ 9.5  53.58 91.77 98.15 84.88 74.61 40.94 56.49  8.39 64.69]
love_matrix = np.abs(love_scores[:, None] - love_scores[None, :])
print(love_matrix)