import numpy as np

generator = np.random.default_rng(123)
ratings = np.round(generator.uniform(low=0.0, high=10.0, size=(10, 2)))
ratings[[1,2,7,9], [0,0,0,0]] = np.nan

# print(ratings)
# [[ 7.  1.]
#  [nan  2.]
#  [nan  8.]
#  [ 9.  3.]
#  [ 8.  9.]
#  [ 5.  2.]
#  [ 8.  2.]
#  [nan  6.]
#  [ 9.  2.]
#  [nan  5.]]

ratings = np.hstack(
  [
    ratings, 
    np.where(
      ~np.isnan(ratings[:, [0]]), 
      ratings[:, [0]], 
      ratings[:, [1]]
    )
  ]
)
print(ratings)