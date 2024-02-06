import numpy as np

def make_roux(n):
  """returns a roux array of length n"""
  arroux = np.zeros([1, n], dtype='int64')
  arroux[:, ::-2] = [x**2 for x in np.arange(1, (n/2) + 1)]
  
  print(arroux[0])
  
  
make_roux(12)