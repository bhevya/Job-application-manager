#!/usr/bin/python3
import sys
import argparse
from datetime import date
import pickle
import os
from collections import defaultdict
data=defaultdict(list)
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
    for i in range(len(args.insert)):
        if i==1:
            data[args.insert[0]].append(args.insert[i])
        elif i==2:
            data[args.insert[0]].append(args.insert[i])

    data[args.insert[0]].append("waiting")
    refwait[args.insert[0]]=1
elif args.applied:
    for i in range(len(args.applied)):
        if i==0 and data.get(args.applied[0],-1)!=-1:
            data[args.applied[i]]=[]
        elif i==1:
            data[args.applied[0]].append(args.applied[i])
    try:
        data[args.applied[0]][2]="applied"
    except:
        data[args.applied[0]].append("applied")
    try:
        del refwait[i]
        print("Done")
    except:
        print("Done")

elif args.check:
    ans=[]
    for i,j in data.items():
        if j[2]=="waiting":
            ans.append(i)
    print(ans)
elif args.total:
    ans=0
    for i,j in data.items():
        if j[2]=="applied":
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
    if status[2]=="waiting" and refwait[company]>3:
        fo.write("Pls apply ASAP"+str(company)+"\n")
    elif status[2]=="waiting" and refwait[company]>2:
        fo.write(str(company)+"\n")



if len(data)>0:
    with open('data.p', 'wb') as fp:
        pickle.dump(data, fp, protocol=pickle.HIGHEST_PROTOCOL)
    with open('refwait.p', 'wb') as fp:
        pickle.dump(refwait, fp, protocol=pickle.HIGHEST_PROTOCOL)