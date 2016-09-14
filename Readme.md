______________________________________________________________________________________________
Assignment-1
Kalpish Singhal
201505513
M.tech CSE(PG2)
______________________________________________________________________________________________

===============================================================
 Implement Apriori Algorithm  
===============================================================
The code given is used to implement Apriori Algorithm:
->Algorithm for mining frequent itemsets for boolean association rules.
->Apriori is an algorithm for frequent item set mining and association rule learning over transactional databases.
->The Code is made scalable for larger datasets.


===============================================================
                      Execution  FORMAT
===============================================================
##implementation 
This application implements Apriori Algorithm Tested on :
1)retail Dataset
2)INTEGRATED-DATASET.csv
3)any large data set user derised 

## How to run code:-
-> Language used :-Python
-> $ python 201505513_Apriori.py
-> give the desired input config.csv in same folder


===============================================================
                  INPUT FORMAT
===============================================================
->Input.csv: 
Input data file will be a comma separated (.csv) file, containing one transaction per line. 
The location of the input file will be against the key “input” in the config file. 

->Config.csv: 
Text before the commas will remain the same in the actual config files, however, order of the 
lines may change. The values of the support and confidence parameters will lie in the range 
[0,1].  
The “flag” parameter in the config file can take 2 values: 0/1, as follows: 
if flag==0: 
You have to mine only the frequent itemsets for the given support. 
if flag==1: 
You have to mine both the frequent itemsets as well as the association rules for the 
given  support and confidence values. 


===============================================================
                      OUTPUT FORMAT
===============================================================
->The output file is a comma separated (.csv) file. 
->The first line specifying the total number of distinct frequent itemsets mined by the algorithm
->If the flag is 1, the N+2nd line will contain an integer M, specifying the total number of distinct association rules mined by the algorithm.
