# @author Vivek
# @version 1.0
# @since 19-04-2018

def compute(obs, states, start_p, trans_p, emission_p):
    fwd = [[0.0 for j in range(states.__len__())] for i in
           range(obs.__len__())]  # the inner defines the columns and outer one the rows

    print "\nPrinting the observation list:-"
    for i in range(obs.__len__()):
        print str(obs[i]),
    print ""

    # for i in range(obs.__len__()):
    #     for j in range(states.__len__()):
    #         print str(fwd[i][j]),
    #     print ""

    # initializing the forward matrix
    for state in states:
        fwd[0][state] = start_p[state] * emission_p[state][obs[0] - 1]

    for i in range(1, obs.__len__()):
        for state1 in states:
            fwd[i][state1] = 0
            for state2 in states:
                fwd[i][state1] += fwd[i - 1][state2] * trans_p[state2][
                    state1]  # forward algo adds up everything, in contrast with the viterbi algo, which takes the max
            fwd[i][state1] *= emission_p[state1][obs[i] - 1]

    # Uncomment below code part to see the status of the fwd matrix
    # for i in range(obs.__len__()):
    #     for j in range(states.__len__()):
    #         print str(fwd[i][j]),
    #     print ""

    # calculating the final likelihood probability
    prob = 0.0
    for state in states:
        prob += fwd[obs.__len__() - 1][state]

    return prob


print "Forward algorithm example program starting off:--"
obs = [3, 3, 1, 1, 2, 2, 3, 1, 3]
states = [0, 1, 2, 3]  # 0 - start; 1 - hot; 2 - cold; 3 - end;
start_p = [1, 1, 1, 1]
trans_p = [
    [0, 0.8, 0.2, 0],
    [0, 0.6, 0.3, 0.1],
    [0, 0.4, 0.5, 0.1],
    [0, 0, 0, 0]
]
emit_p = [
    [0, 0, 0],
    [0.2, 0.4, 0.4],
    [0.5, 0.4, 0.1],
    [0, 0, 0]
]

prob_result = compute(obs, states, start_p, trans_p, emit_p)
print "Resultant path of first observation : " + str(prob_result)

obs2 = [3, 3, 1, 1, 2, 3, 3, 1, 2]
prob_result = compute(obs2, states, start_p, trans_p, emit_p)
print "Resultant path of second observation: " + str(prob_result)
