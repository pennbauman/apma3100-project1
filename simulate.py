# APMA 3100-006 S2020 Project 1
# Group 7(2):
#   Penn Bauman, David Hasani, Jennifer Long, Erick Tian
from math import log
from rand16bit import rand16bit


### General variables (settings of simulation)
## Number of simulations
n = 1000
## Number of callbacks
num_calls = 4
## Times spent on parts of calling
t_dial = 6
t_busy = 3
t_ring = 25
t_end = 1
## Probablities for call results
p_busy = 0.2
p_unanswered = 0.3
## Output settings
prints = 0
    # 0 none
    # 1 pseudo-random numbers
    # 2 results
    # 3 all



## Time before answer from random value
##   T(F) = -12 ln(1 - F)
def answer_time(x):
    return -12 * log(1 - x)
## Index for table of randoms based on 3d matrix
def index(i, j):
    return i*(num_calls+1) + j


### Generate table of random values
rands = rand16bit(n*(num_calls+1))

### Print random values
if (prints%1 == 1):
        for i in range(n*(num_calls+1)):
            for j in range(num_calls+1):
                print(str(rands.getX(index(i, j))))
            print()



### Simulate calls
results = open("results.csv", "w")
results.write("trial, time, calls code, call 0, call 1, call 2, call 3\n")
for i in range(n):
    ## Initialize trial
    if (prints > 1):
        print("trial: " + str(i))
    time = 0.0
    record = ""
    record_code = ""

    for j in range(num_calls):
        time += t_dial

        ## Line is busy
        if (rands.getU(index(i, j)) < p_busy):
            time += t_busy + t_end
            record += ", busy"
            record_code += "b"
            if (prints > 1):
                print ("    call " + str(j) + " busy")

        ## Call is unanswered
        elif (rands.getU(index(i, j)) < p_busy + p_unanswered):
            time += t_ring + t_end
            record += ", unanswered"
            record_code += "u"
            if (prints > 1):
                print ("    call " + str(j) + " unanswered")

        ## Call is answered
        else:
            time += answer_time(rands.getU(index(i, num_calls + 1)))
            record += ", answered"
            record_code += "a"
            if (prints > 1):
                print ("    call " + str(j) + " answered")
            break

    ## Output final trail results
    if (prints > 1):
        print("  total time: " + str(time))
    while (len(record_code) < 4):
        record_code += "-"
    results.write(str(i) + ", " + str(time) + ", " + record_code + record + "\n")

