# APMA 3100-006 S2020 Project 1
# Group 7(2):
#   Penn Bauman, David Hasani, Jennifer Long, Erick Tian
from math import log, exp
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
p_unanswered = 0.3 + p_busy
## Output settings
prints = 0
    # 0 none
    # 1 pseudo-random numbers
    # 2 results
    # 3 all



## Time before answer from random value
##   T(F) = -12 ln(1 - F(1 - e^(-25/12)))
def answer_time(x):
    return -12 * log(1 - x*(1 - exp(-25/12)))


### Generate table of random values
rands = rand16bit()



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
        current_p = rands.nextU()
        time += t_dial

        ## Line is busy
        if (current_p < p_busy):
            time += t_busy + t_end
            record += ", busy"
            record_code += "b"
            if (prints > 1):
                print ("    call " + str(j) + " busy")

        ## Call is unanswered
        elif (current_p < p_unanswered):
            time += t_ring + t_end
            record += ", unanswered"
            record_code += "u"
            if (prints > 1):
                print ("    call " + str(j) + " unanswered")

        ## Call is answered
        else:
            time += answer_time(rands.nextU())
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

