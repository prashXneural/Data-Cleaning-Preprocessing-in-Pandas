import pandas as pd #importing pandas

"""We will use our previous dataframe instead of using a new
one because we have understood that dataframe so there will
not be any problem to understand these topic through old 
dataframe"""

employees = {
    "ID": [1, 2, 2, 4, 5, 6],
    "Name": ["Alice", "Bob", "Bob", None, "Eva", "Frank"],
    "Dept": ["HR", "Engineering", "Engineering", "Finance", None, "Sales"],
    "Salary": [50000, 70000, 70000, None, 55000, 60000],
    "JoiningYear": [2017, 2018, 2018, 2016, 2020, None]
}#dictionary of employees having duplicate and None values

df = pd.DataFrame(employees)
print(f"{df}\n\n")

#___________________________________________________________
# Replacing NaN with the 0
#___________________________________________________________
replacing=df.fillna(0)
print(replacing)

#You can see wherever the Nan and Null values these are all
#replaced by the 0

#------------------------------------------------------------
"""We can also replace any column's Nan value with the mean,
standard deviation,median,etc of its columns"""

repl_with_mean=df["Salary"].fillna(df["Salary"].mean())
print(repl_with_mean)

#____________________________________________________________
"""Now we will see the forward fill it means that if you want
to fill some column's NaN value with the upper value of the
NaN value"""
forw_fill=df["JoiningYear"].bfill()
print(forw_fill)
"""
You can see that the last digit was None so it is filled with
the upper value of its column means 2020"""

#____________________________________________________
"""Now we will see bfill in which the value will be filled with 
the down column corresponding to the None column""" 

back_fill=df["Dept"].bfill()    
print(back_fill)

# None value is filled with the sales value 


# _______________________________________________________
#Catch
# _____________________________________________
# There is a catch that if you are going to perform the bfill()
# but there is not any value after the Null value so there wil 
# not be any change it will be as it is same for the ffill()


# Solution
"""You have to perform both if big data is there and don't
know much about the data"""
