import numpy as np
import pandas as pd
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

def Precision (X, trueX):
    return TP(X, trueX)/(TP(X, trueX) + FP(X, trueX))

def Senserivity (X, trueX):
    return TP(X, trueX)/(TP(X, trueX) + FN(X, trueX))*100

def Specificity (X, tureX):
    return TN(X, trueX)/(TN(X, trueX)+FP(X, trueX))*100

def EstimateTestAndTrain(Pred_test, Ytest, Pred_train, Ytrain):
    TPtest=TP(Pred_test, Ytest)
    FNtest=FN(Pred_test, Ytest)
    FPtest=FP(Pred_test, Ytest)
    TNtest=TN(Pred_test, Ytest)
    TPtrain=TP(Pred_train, Ytrain)
    FNtrain=FN(Pred_train, Ytrain)
    FPtrain=FP(Pred_train, Ytrain)
    TNtrain=TN(Pred_train, Ytrain)

#точность
    accuracy_test = sum(Pred_test==Ytest)/len(Ytest)*100
    accuracy_train = sum(Pred_train==Ytrain)/len(Ytrain)*100
#precision_test=TPtest/(TPtest + FPtest)
#precision_train=TPtrain/(TPtrain + FPtrain)

#чувствительность
    sensitivity_test=TPtest/(TPtest + FNtest)*100
    sensitivity_train=TPtrain/(TPtrain + FNtrain)*100

#специфичность
    specificity_test=TNtest/(TNtest+FPtest)*100
    specificity_train=TNtrain/(TNtrain+FPtrain)*100


    df = pd.DataFrame([['Train', len(Ytrain),accuracy_train
                    ,sensitivity_train,specificity_train],
                   ['Test', len(Ytest), accuracy_test,
                    sensitivity_test, specificity_test]],
                  columns=[' ', 'Число объектов', 'Точность, %',
                           'Чувствительность, %', 'Специфичность, %'])
    return df
    
