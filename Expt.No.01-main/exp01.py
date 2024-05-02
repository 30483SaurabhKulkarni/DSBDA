import pandas as pd

data1 = {"Roll_no":[10,20,30,40,50],"Age":[23,43,45,32,12],"Name":['Sham','dham','gandu','priya','Ramu']}

block = pd.DataFrame(data1)

block

data2 = {"ID":[1,2,3,4,5],"Name":['Sham','dham','gandu','priya','Ramu']}

block2 = pd.DataFrame(data2)

block2

data_merged = block.merge(block2)

data_merged
