import pandas as pd #importing pandas 

"""making a dataframe with duplicate values"""

employees = {
    "ID": [1, 2, 3, 4, 5, 3, 7, 8, 2, 10],  # Duplicate IDs: 2 and 3
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva",
             "Charlie", "Grace", "Hank", "Bob", "Ivy"],  # Duplicate Names: Bob, Charlie
    "Dept": ["HR", "Engineering", "Marketing", "Finance", "Sales",
             "Marketing", "HR", "Finance", "Engineering", "Sales"],  # Some duplicates
    "Salary": [50000, 70000, 65000, 60000, 55000,
               65000, 72000, 61000, 70000, 55000],  # Duplicate salaries too
    "JoiningYear": [2017, 2018, 2019, 2016, 2020,
                    2019, 2021, 2018, 2018, 2020]  # Repeated years
}

df = pd.DataFrame(employees)
print(df)

"now have made a dataframe named 'df' "

#________________________________________________________________
#DETECTING DUPLICATES IN THE DATAFRAME
#________________________________________________________________

duplicates=df.duplicated()
print(duplicates)

"""WORKING:It checks the duplicates row wise if some value 
arrives again then it sets the row to false"""  


#________________________________________________________________
# DROPING DUPLICATES
#________________________________________________________________
drop_dup=df.drop_duplicates()
print(drop_dup,"\n\n") 
"""#nothing has changed you know why because drop_duplicates()
 only deletes the row when everything is same else no change
"""

"""Now if you want to delete the rows by the column wise then
you can do this"""
drop_dupp=df.drop_duplicates(subset=["Salary"],keep="first",inplace=False)  
print(drop_dupp,"\n\n")

"""So here we can see there are 3 parameters of the 
drop_duplicates() so first is subset:in whatever column you 
want to check for the duplicates values and delete the rows

2nd is keep:This means keep the first occurence of the value
after that delete the row if that value occured again

3rd one is inplace: This tells that you want to change 
the real dataframe by keep it "True" or want a different copy
by 'False'"""

"""You can also check for the multiple columns"""
drop_dup1=df.drop_duplicates(subset=["Name","Salary"])
print(drop_dup1)


