import numpy as np
def TP (X, trueX):
    res=0
    for i in range(len(X)):
        if (X[i]==trueX[i]) and (X[i]==1):
            res=res+1
    return res

def FP (X, trueX):
    res=0
    for i in range(len(X)):
        if (X[i]!=trueX[i]) and (X[i]==1):
            res=res+1
    return res

def TN (X, trueX):
    res=0
    for i in range(len(X)):
        if (X[i]==trueX[i]) and (X[i]==0):
            res=res+1
    return res

def FN (X, trueX):
    res=0
    for i in range(len(X)):
        if (X[i]!=trueX[i]) and (X[i]==0):
            res=res+1
    return res

    
