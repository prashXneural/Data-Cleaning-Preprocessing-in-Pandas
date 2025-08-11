import pandas as pd #inporting pandas
#--------------------------------------------------
#now we will make a data frame 
employees = {
    "ID": [1, 2, 2, 4, 5, 6],
    "Name": ["Alice", "Bob", "Bob", None, "Eva", "Frank"],
    "Dept": ["HR", "Engineering", "Engineering", "Finance", None, "Sales"],
    "Salary": [50000, 70000, 70000, None, 55000, 60000],
    "JoiningYear": [2017, 2018, 2018, 2016, 2020, None]
}#dictionary of employees having duplicate and None values

import pandas as pd
df = pd.DataFrame(employees)
print(df)
#--------------------------------------------------
#making the data frame of the dictionary named employees
#--------------------------------------------------
df = pd.DataFrame(employees)
print(df)

#--------------------------------------------------
#checking for the null values
#--------------------------------------------------
is_null= df.isnull()
print(is_null)
"""You will get the many boolean values according to the columns
in the data frame telling you that which of the value in the 
data frame is a null value"""

#--------------------------------------------------
#Counting the missing values per column so we can get the idea 
#that which column has the most none values
sum=df.isnull().sum()
print(sum)

#You can see every column in the data frame has 1 null value
#except id column as this is having the duplicate value

# ____________________________________________________________
#Dropping  missing data
#_____________________________________________________________
dropping=df.dropna()    
print(dropping)
#This drops all the rows which is having a null value

"""Now if you want to drop the columns then you can do this"""
drop_col=df.dropna(axis=1)
print(drop_col)
# There is only a single column named "id" has not null value,
#other than this all having null values so all dropped


#--------------------------------------------------
#Dropping the duplicate values
#_________________________________________________
drop_dup=df.drop_duplicates()
print(drop_dup)
#checks the values row wise if same value is occured ,it
# deleted the whole row
