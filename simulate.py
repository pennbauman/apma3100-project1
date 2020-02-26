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
rands = rand16bit(n*4*2)
## Index for table of randoms based on 3d matrix
def index(i, j, k):
    return (i*2*n_calls) + (j*2) + k

### Print random values
for i in range(0):
    for j in range(n_calls):
        print(str(rands.getX(index(i, j, 0)))+ ", " + str(rands.getX(index(i, j, 1))))
    print()


### Simulate calls
results = open("results.csv", "w")
results.write("trial, time, calls code, call 0, call 1, call 2, call 3\n")
for i in range(n):
    ## Initialize trial
    print("trial: " + str(i))
    time = 0.0
    record = ""
    record_code = ""

    for j in range(n_calls):
        time += t_dial

        ## Line is busy
        if (rands.getU(index(i, j, 0)) < p_busy):
            time += t_busy + t_end
            record += ", busy"
            record_code += "b"
            print ("    call " + str(j) + " busy")

        ## Call is unanswered
        elif (rands.getU(index(i, j, 0)) < p_busy + p_unanswered):
            time += t_ring + t_end
            record += ", unanswered"
            record_code += "u"
            print ("    call " + str(j) + " unanswered")

        ## Call is answered
        else:
            time += answer_time(rands.getU(index(i, j, 1)))
            print ("    call " + str(j) + " answered")
            record += ", answered"
            record_code += "a"
            break

    ## Output final trail results
    print("  total time: " + str(time))
    while (len(record_code) < 4):
        record_code += "-"
    results.write(str(i) + ", " + str(time) + ", " + record_code + record + "\n")
