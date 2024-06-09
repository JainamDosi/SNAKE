import numpy as np
state={
 0:"sa",
  1:"sb",
  2:"sc",
3:"sd"
}
A=np.array([
  [1,0,0,0],
  [0.5,0,0.5,0],
  [0,0.2,0,0.8],
  [0,0,0,0]
]) 

#A random walk as given in further videos suggets that we remain on State 0 only
n = 15
start_state=0
print(state[start_state], end=" ")
prev_state =start_state
while n-1:
  curr_state= np.random.choice([0, 1, 2,3], p=A[prev_state])
  print(state[curr_state], "--->", end=" ")
  prev_state= curr_state
  n-=1
print("stop")

#either we can multiply the transition matrix with the initial state vector or we can multiply matrix by itself multiple times
pi=np.array([1,0,0,0])
n=10**3
for i in range(n):
  pi=np.dot(pi,A)

print(pi)
#Thus probability to reach any other state is 0 even after large number of iterations
