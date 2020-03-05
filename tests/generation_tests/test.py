# from generator.typo.gexp import ExpertGenerator
import unittest

class TestPreperation(unittest.TestCase):

    
    def createRandomData(self):

        
        data = [
            'Index0',
            'Index1',
            'Index2',
            'Index3',
            'Index4',
            'Index5',
            'Index6'
        ]
        prob = [(0.8431,0.9313,0.235,0.7123,0.5555,0.5555),
            (0.56145,0.4673,0.72456,0.613,0.123,0.63423),
            (0.7569,0.4569,0.7235,0.2598,0.7469,0.1287),
            (0.7589,0.8596,0.1259,0.6589,0.5469,0.5845),
            (0.2547,0.7536,0.4712,0.7369,0.2698,0.3695),
            (0.9635,0.1485,0.7589,0.9965,0.4569,0.8749),
            (0.7589,0.2569,0.5846,0.2596,0.7536,0.9514)
            ]
        
        # [
        #     0.0882,
        #     0.05155,
        #     0.01,
        #     0.0151,
        #     0.033,
        #     0.0053,
        #     0.1
        # ]    
    
        return prob, data 


"""
Expert generator algorithm test codes.
This is not a method test it tests the algorithm 
with different data.
"""
class ExpertGeneratorMethodTests():
    
    def expertGeneratorOptimumDataControl(self):
        prepare = TestPreperation()
        prob, data = prepare.createRandomData()
        sindex = 0 # Searched index

        # Probability list of data
        general_index = 0
        maxfdist = 0
        for i in range(len(prob)):
            # initialize fmindist
            fmindist = 100000000
            
            # find the minimum distance between data points
            for j in range(1, len(prob[i])):
                if fmindist > abs(prob[i][sindex] - prob[i][j]) and sindex != j:
                    fmindist =  abs(prob[i][sindex] - prob[i][j])

            # Find the general maximum distance between
            # minimum distances
            if maxfdist < fmindist:
                print("Maxfdist : %s, FminDist : %s" % (maxfdist, fmindist))
                maxfdist = fmindist
                general_index = i

        
        # Control if it is ok.
        return prob[general_index], data[general_index], maxfdist


test = ExpertGeneratorMethodTests()
print(test.expertGeneratorOptimumDataControl())