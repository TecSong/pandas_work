### TEST FUNCTION: test_stations
# DO NOT REMOVE THE LINE ABOVE
from pandas import Series, DataFrame
import pandas as pd
for i in range(1,14):
    a="x"+str(i)
    exec(a+'= %r' % [])
def cla (s):
    x1.append(s[0:2])
    x2.append(s[2:3])
    x3.append(s[3:5])
    x4.append(s[5:11])
    x5.append(s[12:20])
    x6.append(s[21:30])
    x7.append(s[31:37])
    x8.append(s[38:40])
    x9.append(s[41:71])
    x10.append(s[72:78])
    x11.append(s[79:85])
    x12.append(s[86:92])
    x13.append(s[93:95])



with open('./ushcn-v2.5-stations.txt') as ff:
    doc1=ff.read().split("\n")
    
    for i in range(0,1218):
        import pdb;pdb.set_trace()
        cla(doc1[i])
    x=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13]
    stations=DataFrame(x).T
    stations.columns=["COUNTRY CODE","NETWORK CODE",
    "ID PLACEHOLDERS","COOP ID","LATITUDE","LONGITUDE","ELEVATION",
    "STATE","NAME","COMPONENT 1","COMPONENT 2",
    "COMPONENT 3","UTC OFFSET"]
    print(stations['ELEVATION'])
   

