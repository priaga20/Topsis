import pandas as pd
import math
import numpy as np

class Topsis:
    def __init__(self,filename):
        data = pd.read_csv(filename)
        self.d = data.iloc[:,1:].values
        self.features = len(self.d[0])
        self.samples = len(self.d)
    def fun(self,a):
        return a[1]
    def fun2(self,a):
        return a[0]
    def evaluate(self,w = None,im = None):
        d = self.d
        features = self.features
        samples = self.samples       
        if w==None:
           w=[1]*features
        if im==None:
         im=["+"]*features
        ideal_best=[]
        ideal_worst=[]
        for i in range(0,features):
            k = math.sqrt(sum(d[:,i]*d[:,i]))
            Max = 0
            Min = 1 
            for j in range(0,samples):
                d[j,i] = (d[j,i]/k)*w[i]
                if d[j,i]>Max:
                    Max = d[j,i]
                if d[j,i]<Min:
                    Min = d[j,i]
            if im[i] == "+":
                ideal_best.append(Max)
                ideal_worst.append(Min)
            else:
                ideal_best.append(Min)
                ideal_worst.append(Max)
        performance = []
        for i in range(0,samples):
            SNegative = math.sqrt(sum((d[i]-ideal_worst)*(d[i]-ideal_worst)))
            SPositive = math.sqrt(sum((d[i]-ideal_best)*(d[i]-ideal_best)))
            lst = []
            lst.append(i)
            lst.append(SNegative/(SNegative+SPositive))
            performance.append(lst)
        performance.sort(key=self.fun)
        rank = 1
        for i in range(samples-1,-1,-1):
            performance[i].append(rank)
            rank+=1
        performance.sort(key=self.fun2)
        return performance
