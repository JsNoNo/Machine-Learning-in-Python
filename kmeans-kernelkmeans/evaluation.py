from math import log, sqrt

def countClassNum(assignment):
	classType=[]
	classType.append(assignment[0])
	for i in range(1,len(assignment)):
	    	if assignment[i] not in classType:
	    		classType.append(assignment[i])
    	return len(classType)

def  purity(groundtruthAssignment, algorithmAssignment):

    purity = 0 
    # 计算purity 
    total = len(groundtruthAssignment)
    classNum1=countClassNum(algorithmAssignment)
    classNum2=countClassNum(groundtruthAssignment)
    classNum=max(classNum1,classNum2)
    classDivide=[[0.000000000000001]*classNum for i in range(classNum)]
    for i in range(total):
    	classDivide[algorithmAssignment[i]][groundtruthAssignment[i]]+=1
    sum=0.0
    for i in range(classNum):
    	sum+=max(classDivide[i])
    purity=sum/total
    	
    return purity 


def NMI(groundtruthAssignment, algorithmAssignment):

    NMI = 0
    # 计算 NMI
    classNum1=countClassNum(algorithmAssignment)
    classNum2=countClassNum(groundtruthAssignment)
    classNum=max(classNum1,classNum2)
    numT=[0.000000000000001]*classNum
    numC=[0.000000000000001]*classNum
    total=len(groundtruthAssignment)
    h_C=0.0
    h_T=0.0
    for i in range(total):
    	numT[groundtruthAssignment[i]]+=1.0
    	numC[algorithmAssignment[i]]+=1.0
    for i in range(classNum):
    	numT[i]/=float(total)
    	numC[i]/=float(total)
    	h_T += numT[i]*log(numT[i])
    	h_C += numC[i]*log(numC[i])
    h_T *=(-1.0)
    h_C *=(-1.0)
    I_CT=0.0
    classDivide=[[0.000000000000001]*classNum for i in range(classNum)]
    for i in range(total):
    	classDivide[algorithmAssignment[i]][groundtruthAssignment[i]]+=1.0
    for i in range(classNum):
    	for j in range(classNum):
    		classDivide[i][j] = (classDivide[i][j])/float(total)
    		I_CT += classDivide[i][j]*log(classDivide[i][j]/numC[i]/numT[j])
    NMI = I_CT/sqrt(h_C*h_T)

    return NMI
