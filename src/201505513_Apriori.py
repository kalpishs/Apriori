"""
Description : Python implementation of the Apriori Algorithm
Name- Kalpish Singhal
Roll - 201505513

"""
import sys
from itertools import *
from collections import *
from optparse import *
import csv
from math import *

def Join(currentList, len_):
	set_join=set()
	set_join=set([i.union(j) for i in currentList for j in currentList if len_==len(i.union(j)) ])
	return set_join


#Read the input file and save the required information in the dictionary:
#itemset : (transaction no in which the itemset occurs)
def readdata(infile):
	no_of_transaction=1
	transList={}
	with open(infile, 'rU') as file_dataset:
		listing = csv.reader(file_dataset)
		lines = list(listing)
		#print lines
		#exit(0)
		for transaction in lines:
			#print transaction
			if transaction[-1]=='':
				transaction=transaction[:-1]
			#print transact
			for item in transaction:
				if item not in transList:
					temp2=set()
					temp2.add(no_of_transaction)
					transList[item] = temp2 
				else:
					transList[item].add(no_of_transaction)             
			no_of_transaction+=1

	no_of_transaction=no_of_transaction-1
	return transList,no_of_transaction

#Calculate the number of transactions in which the itemset occurs
def calculate_frequency(itemset, transactionList):
    a = set()
    for item in itemset:
    	freq = transactionList[item]
        if len(a) != 0:
            a = a & freq
        else:
            a = a | freq
    return len(a)

#Calculate the frequent items among the given itemsets
def findMinSupport(itemset, transactionList, minSupport):
    tempset=set()
    for item in itemset:
        if type(item)==type("test"):
            freq = len(transactionList[item])
        else:
        	freq = calculate_frequency(item, transactionList)
        l=[]
        if minSupport<freq:
            if type(item)==type("test"):
                l.append(item)
                fset = frozenset(l)
                tempset.add(fset)
            else:
                tempset.add(item)
    return tempset

#The main algorithm which calculates the frequent itemsets and association rules
def runApriori(inputfile, minSupport, minConfidence):
	transactionList, no_of_transaction =readdata(inputfile)
	minSupport=int(ceil(float(minSupport)*no_of_transaction))
	k,frequentitems_final=1,[]
	associationrules_final = []
	currentList = findMinSupport(set(transactionList.keys()), transactionList, minSupport)

	while(currentList != set([])):
		for item in currentList:
			frequentitems_final.append(tuple(item))
		length = k+1
		currentList = findMinSupport(Join(currentList, length),transactionList, minSupport)
		k = k + 1
	for item in frequentitems_final:
		_subsets = map(frozenset, [x for x in chain(*[combinations(frozenset(item), i + 1) for i, a in enumerate(frozenset(item))])])
		item = frozenset(item)
		for element in _subsets:
			remain = item.difference(element)
			if len(remain)>0:
				freq_item = float(calculate_frequency(item, transactionList))
				freq_element = float(calculate_frequency(element, transactionList))
				if freq_element > float(0) :
					confidence = float(freq_item)/float(freq_element)
					if float(confidence) >= float(minConfidence):
						associationrules_final.append((tuple(element), tuple(remain)))
	return frequentitems_final, associationrules_final


def tupletostring(tup):
    string=str()
    for i in range(len(tup)):
        string=string+tup[i]
        if i != len(tup)-1:
            string=string+","
                   
    return string

#write into File 
def gettingoutput(items, rules, outputfilename, flag):
    f = open(outputfilename, "w+")
    
    #Writing Frequent ItemSets
    length = str(len(items))+"\n"
    f.write(length)
    for item in items:
		templist = list(item)
		for i in range(len(templist)):
			f.write(templist[i])
			if i != len(templist)-1:
				f.write(",")
		f.write('\n')

    #Writing Association Rules
    if(flag=='1'):
    	length = str(len(rules))+"\n"
        f.write(length)
        for rule in rules:
            pre, post = rule
            to_write = tupletostring(pre)
            to_write = to_write + " => "
            to_write = to_write + tupletostring(post) + "\n"
            f.write(to_write)

    f.close()

def main():
	#read file
	open_info = open('config.csv', 'rb') 
	for eachline in open_info:
		eachline=eachline.rstrip('\n')
		eachline=eachline.split(',')
		in_,out_,supp_,cof_,flg_="input","output","support","confidence","flag"
		if eachline[0] == in_:
			inputfile=eachline[1]
		if eachline[0] == out_:
			outfile=eachline[1]
		if eachline[0] == supp_:
			support=eachline[1]
		if eachline[0] == cof_:
			confidence=eachline[1]
		if  eachline[0]== flg_:
			flag=eachline[1]
	
	items, rules = runApriori(inputfile,support, confidence)	
	gettingoutput(items, rules, outfile, flag)				


main()	
