
def findOptimumDataByProbsAndByIndex(prob, index):
    
    # I think data probabilities is enough.
    
    general_index = 0
    maxfdist = 0

    for i in range(len(prob)):
        # initializa fmindist
        fmindist = 1000000 # Make this value max or something
        # fmindist = abs(prob[i][index] - prob[i][1]) # We can use this instead of the upper one
    

        #find the minimum distance between data points
        for j in range(len(prob[i])):
            if fmindist > abs(prob[i][index] - prob[i][j]) and index != j:
                fmindist = abs(prob[i][index] - prob[i][j])

        # Find the general maximum distance,
        # among minimum distances
        if maxfdist < fmindist:
            print("\tMaxfdist : %s, FminDist: %s " % (maxfdist, fmindist))
            maxfdist = fmindist
            general_index = i
    
    #It should return the general index
    return general_index, prob[general_index], maxfdist




