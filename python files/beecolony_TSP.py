# swarm.py
# Author: Somyajit Chakraborty
# python 3.4.3
# demo of simulated bee colony (SBC) optimization
# solves a dummy Traveling Salesman Problem

import random
import copy    # array-copying convenience
import sys     # max float

# ------------------------------------

def show_path(path):
  for i in range(len(path)-1):
    print(str(path[i]) + " -> ", end="")
  print(path[len(path)-1])

# ------------------------------------

def error(path):
  d = 0.0  # total distance between cities
  for i in range(len(path)-1):
    if path[i] < path[i+1]:
      d += (path[i+1] - path[i]) * 1.0
    else:
      d += (path[i] - path[i+1]) * 1.5
  minDist = len(path)-1
  return d - minDist

# ------------------------------------

class Bee:
  def __init__(self, nc, seed):
    #self.rnd = random.Random(seed)
    self.status = 0  # 0 = inactive, 1 = active, 2 = scout
    self.path = [0 for i in range(nc)]  # potential solution

    for i in range(nc):
      self.path[i] = i  # [0,1,2, ...]

    random.shuffle(self.path)
    self.error = error(self.path) # bee's current error

# ------------------------------------

def solve(nc, nb, max_epochs):
  # solve TSP for nc cities using nb bees
  # optimal soln is [0,1,2, . . n-1]
  # assumes dist between adj cities is 1.0 or 1.5

  # create nb random bees
  hive = [Bee(nc, i) for i in range(nb)]

  best_err = sys.float_info.max  # dummy init value
  for i in range(nb):  # check each random bee
    if hive[i].error < best_err:
      best_err = hive[i].error
      best_path = copy.copy(hive[i].path)

  # assign initial statuses
  numActive = int(nb * 0.50)
  numScout = int(nb * 0.25)
  numInactive = nb - (numActive + numScout)
  for i in range(nb):
    if i < numInactive:
      hive[i].status = 0
    elif i < numInactive + numScout:
      hive[i].status = 2
    else:
      hive[i].status = 1

  epoch = 0
  while epoch < max_epochs:
    if best_err == 0.0: break
    for i in range(nb):  # process each bee
      if hive[i].status == 1:    # active bee
        # find a neighbor path and associated error
        neighbor_path = copy.copy(hive[i].path)
        ri = random.randint(0, nc-1)  # random index
        ai = 0  # adjacent index. assume last->first
        if ri < nc-1: ai = ri + 1
        tmp = neighbor_path[ri]
        neighbor_path[ri] = neighbor_path[ai]
        neighbor_path[ai] = tmp
        neighbor_err = error(neighbor_path)

        # check if neighbor path is better
        p = random.random()  # [0.0 to 1.0)
        if (neighbor_err < hive[i].error or
         (neighbor_err >= hive[i].error and p < 0.05)):
          hive[i].path = neighbor_path
          hive[i].error = neighbor_err

          # new best?
          if hive[i].error < best_err:
            best_err = hive[i].error
            best_path = hive[i].path
            print("epoch = " + str(epoch) +
              " new best path found ", end="")
            print("with error = " + str(best_err))
        # active bee code

      elif hive[i].status == 2:  # scout bee
        # make random path and error
        random_path = [0 for j in range(nc)]
        for j in range(nc):
          random_path[j] = j
        random.shuffle(random_path)
        random_err = error(random_path)
        # is it better?
        if random_err < hive[i].error:
          hive[i].path = random_path  # ref assignmnt
          hive[i].error = random_err
          # new best?
          if hive[i].error < best_err:
            best_err = hive[i].error
            best_path = hive[i].path
            print("epoch = " + str(epoch) +
              " new best path found ", end="")
            print("with error = " + str(best_err))

      elif hive[i].status == 0:  # inactive
        pass  # null statement

    # for-each bee

    epoch += 1
  # while

  print("\nBest path found:")
  show_path(best_path)
  print("\nError of best path = " + str(best_err))

# ------------------------------------

print("\nBegin simulated bee colony optimization using
 Python demo\n")
print("Goal is to solve a dummy Traveling Salesman Problem")
print("\nDistance between cities A and B is (B-A) * 1.0 if B > A")
print(" or (A-B) * 1.5 if A > B. For example, d(3,5) = 2.0")
print(" and d(8,3) = 7.5. In a real scenario you'd have a
 lookup table")
print("\nFor n cities, the optimal path is 0 -> 1 -> . . -> (n-1)
print(" with a total path distance of n-1.\n")

num_cities = 20
num_bees = 50
max_epochs =10000

print("Setting num_cities = " + str(num_cities))
print("Setting num_bees   = " + str(num_bees))
print("Setting max_epochs = " + str(max_epochs) + "\n")

random.seed(1)
solve(num_cities, num_bees, max_epochs)

print("\nEnd simulated bee colony sim\n")
