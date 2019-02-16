#!/usr/bin/python3
import sys
import argparse
from datetime import date
import pickle
import os
data={}
refwait={}
if os.path.getsize('data.p')>0:
    with open('data.p', 'rb') as fp:
         data = pickle.load(fp)
    with open('refwait.p', 'rb') as fp:
        refwait = pickle.load(fp)

parser = argparse.ArgumentParser()
parser.add_argument("-i","--insert", nargs='+',help="waiting for refferal",action="store")
parser.add_argument("-a","--applied", nargs='+',help="applied",action="store")
parser.add_argument("-c","--check",help="checking companies to be applied",action="store_true")
parser.add_argument("-t","--total",help="Total Companies applied to",action="store_true")
parser.add_argument("-ck","--checkcom",nargs='+',help="To Check whether I have already applied to the company", action="store")
args = parser.parse_args()

if args.insert:
    print(args.insert)
    for i in args.insert:
        data[i]="waiting"
        refwait[i]=1
elif args.applied:
    for i in args.applied:
        data[i]="applied"
        try:
            del refwait[i]
        except:
            print("Key missing",i)

elif args.check:
    ans=[]
    for i,j in data.items():
        if j=="waiting":
            ans.append(i)
    print(ans)
elif args.total:
    ans=0
    for i,j in data.items():
        if j=="applied":
            ans+=1
    print("Total companies applied to:",ans)
elif args.checkcom:
    for i in args.checkcom:
        if data.get(i,-1)==-1:
            print("You can apply to",i)
        else:
            print("already applied to",i)

today=date.today()
yesterday=date(today.year,2,3)
if (today>yesterday):
    ans=[]
    for i,j in zip(data,refwait):
        if data[i]=='waiting':
            refwait[j]+=1
            if refwait[j]>2:
                ans.append(j)
fo = open("/home/bhavya/Desktop/companies.txt", "w")
for company,status in data.items():
    if status=="waiting" and refwait[company]>3:
        fo.write("Pls apply ASAP"+str(company)+"\n")
    elif status=="waiting" and refwait[company]>2:
        fo.write(str(company)+"\n")

print(data)
with open('data.p', 'wb') as fp:
    pickle.dump(data, fp, protocol=pickle.HIGHEST_PROTOCOL)
with open('refwait.p', 'wb') as fp:
    pickle.dump(refwait, fp, protocol=pickle.HIGHEST_PROTOCOL)