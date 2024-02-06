import numpy as np

field = np.zeros(shape = (10, 10), dtype='int64')

np.set_printoptions(linewidth=100000)
# print(field)
# [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]

generator = np.random.default_rng(seed=123)
num_eggs = 20

eggs = np.array([[i, j] for j in range(10) for i in range(10)])
eggs = generator.permutation(eggs, axis=0)[:num_eggs].T
print(eggs, '\n')
field[eggs[0], eggs[1]] = np.arange(1, num_eggs+1)
print(field)

# locs = generator.choice(field.size, num_eggs, replace=False)
# field.ravel()[locs] = np.arange(1, num_eggs+1)
# print(field)