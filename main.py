
class Solution:
  def __init__(self, i, j, sum):
    self.i = i   
    self.j = j
    self.sum = sum

  def __eq__(self, other):
    return self.i == other.i and self.j == other.j and self.sum == other.sum

  def __ne__(self, other):
    return not self == other

  def __str__(self):
    return "Solution(i = " + str(self.i) + ", j = " + str(self.j) + ", sum = " + str(self.sum) + ")"

class IllegalArgumentError(Exception):
  def __init__(self, message):
    super().__init__(self, message)

def max_sum(arr):

  if (len(arr) == 0):
    raise IllegalArgumentError("The array must not be empty.")

  tsums = []
  tsum = 0

  for tj in range(len(arr)):
    tsum += arr[tj]
    tsums.append(tsum)

  (i, j, ti) = (0, 0, 0)
  sum = tsums[0]
  tmin = min(tsums[0], 0)

  for tk in range(1, len(tsums)):
    if (tsums[tk] - tmin > sum):
      if tmin >= 0:
        i = ti
        sum = tsums[tk]
      else:
        i = ti + 1
        sum = tsums[tk] - tmin
      j = tk
    if (tsums[tk] < tmin):
      ti = tk
      tmin = tsums[ti]

  sol = Solution(i + 1, j + 1, sum)

  return sol

