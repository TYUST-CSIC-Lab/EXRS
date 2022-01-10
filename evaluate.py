import pandas as pd
import random
from random import choice
import warnings
warnings.filterwarnings("ignore")
import numpy as np
shuju1 = pd.read_csv(r'C:\Users\Administrator\Desktop\event.csv', engine='python', encoding="utf-8")
houxuanfinal = shuju1.values

shuju4 = pd.read_csv(r'C:\Users\Administrator\Desktop\sim.csv', engine='python', encoding="utf-8")
sim = shuju4.values

shuju5 = pd.read_csv(r'C:\Users\Administrator\Desktop\topsuoyin.csv', engine='python', encoding="utf-8")
topsuoyin = shuju5.values


def evaluate1(suoyin,D,topsuoyin):
    common = [x for x in suoyin if x in topsuoyin]
    f1=len(common)/D
    return f1


def evaluate2(suoyin, D,houxuanfinal):
    bizhi=[]
    for s in range(len(suoyin)):
        itemsuoyin=int(suoyin[s])
        rated=float(houxuanfinal[itemsuoyin][4])/339.5
        bizhi.append(rated*houxuanfinal[itemsuoyin][9])
    f2=sum(bizhi)
    return f2



def evaluate3(suoyin, D,houxuanfinal,sim):
    itemid = list()
    similarity = []
    simtemp = np.zeros(shape=[1, 10000])
    for b in range(len(suoyin)):
        itemsuoyin = int(suoyin[b])
        itemid.append(houxuanfinal[itemsuoyin][5])
    newitemid = sorted(itemid)
    for c in range(len(suoyin)):
        e = c
        for d in range(len(sim)):
            if (newitemid[c] == sim[d][0]):
                simtemp = sim[d]
        while (e < len(newitemid) - 1):
            e = e + 1
            similarity.append(simtemp[newitemid[e]])
    f3 = 1-2 * sum(similarity) / (D * (D - 1))
    return f3


def evaluate4(suoyin, D,houxuanfinal):
    novelty = list()
    for i in range(len(suoyin)):
        itemsuoyin = int(suoyin[i])
        novelty.append(houxuanfinal[itemsuoyin][11])
    f4 = sum(novelty) / D
    return f4


