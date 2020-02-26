# APMA 3100-006 S2020 Project 1
# Group 7(2):
#   Penn Bauman, David Hasani, Jennifer Long, Erick Tian
from rand16bit import rand16bit

### General variables (settings of simulation)
## Number of simulations
n = 1000
## Number of callbacks
n_calls = 4
## Times spent on parts of calling
t_dial = 6
t_busy = 3
t_ring = 25
t_end = 1
## Probablities for call results
p_busy = 0.2
p_unanswered = 0.3


### Time before answer (maps 0<=x<=1 -> 0<=t_ring<=25)
def answer_time(x):
    return x*t_ring



### Generate table of random values
rand_seeds = rand16bit(n*4*5)
probs = [0]*n
# rand_seeds.print()
for i in range(n):
    probs[i] = [0]*n_calls
    for j in range(n_calls):
        probs[i][j] = [0]*5
        for k in range(5):
            # print("({:d}, {:d}, {:d}) = {:d}".format(i,j,k, (i*20) + (j*5) + k))
            # print(rand_seeds.getX((i*20) + (j*5) + k))
            probs[i][j][k] = rand_seeds.getU((i*5*n_calls) + (j*5) + k)

### Print random values
# if True:
if False:
    for i in range(len(probs)):
        for j in range(n_calls):
            print(probs[i][j])
        print()


### Simulate calls
for i in range(len(probs)):
    time = 0.0
    print("sim: " + str(i))
    for j in range(n_calls):
        time += t_dial
        ## Line is busy
        if (probs[i][j][0] < p_busy):
            time += t_busy + t_end
            print ("    call " + str(j) + " busy")
        ## Call is unanswered
        elif (probs[i][j][0] < p_busy + p_unanswered):
            time += t_ring + t_end
            print ("    call " + str(j) + " unanswered")
        ## Call is answered
        else:
            time += answer_time(probs[i][j][1])
            print ("    call " + str(j) + " answered")
            break
    print("  total time: " + str(time))
