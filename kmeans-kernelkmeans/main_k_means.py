import sys
from LoadData import * 
from k_means import * 
from evaluation import * 
import self_plot

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "[usage] <data-file> <ground-truth-file>"
        exit(1) 
    
    dataFilename = sys.argv[1]
    groundtruthFilename = sys.argv[2]
    
    data = loadPoints(dataFilename) 
    groundtruth = loadClusters(groundtruthFilename) 
    
    nDim = len(data[0]) 
   
    K = 2  # Suppose there are 2 clusters 
    
    centers = [] 
    centers.append(data[0])
    centers.append(data[1])
    #centers.append(data[2])
    #centers.append(data[3])
    #centers.append(data[4])

    
    results = kmeans(data, centers) 

#    fr = open('newClusterId.txt','w')
#    fr.write(str(len(results))+'\n')
#    for i in results:
#        fr.write(str(i))
#        fr.write('\n')
#    fr.close()

    res_Purity = purity(groundtruth, results) 
    res_NMI = NMI(groundtruth, results) 
    
    print "Purity =", res_Purity
    print "NMI = ", res_NMI
    self_plot.plotFigure(data, results)

