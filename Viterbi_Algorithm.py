# @author Vivek
# @version 1.0
# @since 19-04-2018

def compute(obs, states, start_p, trans_p, emission_p):
    viterbi = [[0.0 for j in range(states.__len__())] for i in
               range(obs.__len__())]  # the inner defines the columns and outer one the rows
    path = [[0.0 for j in range(obs.__len__())] for i in
            range(states.__len__())]

    print "\nPrinting the observation list:-"
    for i in range(obs.__len__()):
        print str(obs[i]),
    print ""

    # for i in range(obs.__len__()):
    #     for j in range(states.__len__()):
    #         print str(fwd[i][j]),
    #     print ""

    # initializing the viterbi matrix and the path matrix
    for state in states:
        viterbi[0][state] = start_p[state] * emission_p[state][obs[0] - 1]
        path[state][0] = state

    for i in range(1, obs.__len__()):
        newpath = [[0.0 for j in range(obs.__len__())] for k in
                   range(states.__len__())]

        for curr_state in states:
            prob = -1.0
            for from_state in states:
                nprob = viterbi[i - 1][from_state] * trans_p[from_state][curr_state] * emission_p[curr_state][
                    obs[i] - 1]
                if nprob > prob:  # reassign only if greater
                    prob = nprob
                    state = from_state
                    viterbi[i][curr_state] = prob
                    # for m in range(0, i):
                        # newpath[curr_state][m] = path[state][m]
                    newpath[curr_state][0:i] = path[state][0:i]
                    newpath[curr_state][i] = curr_state

        # for n1 in range(states.__len__()):
        #     for n2 in range(obs.__len__()):
        #         path[n1][n2] = newpath[n1][n2]
        path = newpath

    # Uncomment below code part to see the status of the viterbi matrix
    # for i in range(obs.__len__()):
    #     for j in range(states.__len__()):
    #         print str(viterbi[i][j]),
    #     print ""

    prob = -1.0
    state = 0
    # computing the final path
    for state1 in states:
        if viterbi[obs.__len__() - 1][state1] > prob:
            prob = viterbi[obs.__len__() - 1][state1]
            state = state1

    return path[state]


print "Viterbi algorithm example program starting off:-"
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

path_result = compute(obs, states, start_p, trans_p, emit_p)
print "Resultant path of first observation:-"
for path in path_result:
    if path == 1:
        print "hot",
    else:
        print "cold",
print ""

obs2 = [3, 3, 1, 1, 2, 3, 3, 1, 2]
path_result = compute(obs2, states, start_p, trans_p, emit_p)
print "Resultant path of second observation:-"
for path in path_result:
    if path == 1:
        print "hot",
    else:
        print "cold",
print ""
