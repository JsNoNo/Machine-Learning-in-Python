from utils import * 
from math import exp 

def kernel(data, sigma):
    nData = len(data)
    Gram = [[0.0] * nData for i in range(nData)] 
    # 计算查询矩阵
    for i in range(nData):
    	for j in range(nData):
    		Gram[i][j] = -squaredDistance(data[i], data[j])
    		Gram[i][j] /=(2*sigma*sigma)
    		Gram[i][j] = exp(Gram[i][j])

    return Gram 


