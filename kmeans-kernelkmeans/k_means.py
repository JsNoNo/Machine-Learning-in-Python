from utils import * 
from numpy import *

def computeSSE(data, centers, clusterID):
    sse = 0 
    nData = len(data) 
    for i in range(nData):
        c = clusterID[i]
        sse += squaredDistance(data[i], centers[c]) 
        
    return sse 

def updateClusterID(data, centers):
    nData = len(data)    
    clusterID = [0] * nData   
    # 对每个样例分配隐含类别
    for i in range(nData):
    	minDistance = inf
    	minId = -1
    	for j in range(len(centers)):
    		distance=squaredDistance(data[i], centers[j])
    		if distance<minDistance:
    			minDistance=distance
    			minId=j
    	clusterID[i]=minId
    return clusterID


def updateCenters(data, clusterID, K):
    nDim = len(data[0])
    centers = [[0] * nDim for i in range(K)]

    # 内循环优化簇中心点
    for i in range(len(centers)):
    	count=0
    	temp=[0]*nDim
    	for j in range(len(clusterID)):
    		if clusterID[j]==i:
    			for k in range(nDim):
    				temp[k]+=data[j][k]
    			count+=1
    	if count != 0:
    		for j in range(nDim):
    			temp[j]/=count
    		centers[i]=temp

    return centers 

def kmeans(data, centers, maxIter = 100, tol = 1e-6):
    nData = len(data) 
    
    if nData == 0:
        return [];

    K = len(centers) 
    
    clusterID = [0] * nData
    
    if K >= nData:
        for i in range(nData):
            clusterID[i] = i
        return clusterID

    nDim = len(data[0]) 
    
    lastDistance = 1e100
    
    for iter in range(maxIter):
        clusterID = updateClusterID(data, centers) 
        centers = updateCenters(data, clusterID, K)
        
        curDistance = computeSSE(data, centers, clusterID) 
        if lastDistance - curDistance < tol or (lastDistance - curDistance)/lastDistance < tol:
            print "# of iterations:", iter 
            print "SSE = ", curDistance
            return clusterID
        
        lastDistance = curDistance
        
    print "# of iterations:", iter 
    print "SSE = ", curDistance
    return clusterID

