import pandas as pd #importing pandas

# Creating data for 10 employees
data = {
    "EmployeeID": range(1, 11),
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan", "Neha", "Vikram", "Pooja", "Ravi", "Ananya"],
    "Department": ["HR", "IT", "Finance", "Marketing", "IT", "Finance", "HR", "Marketing", "IT", "Finance"],
    "Salary": [50000, 70000, 65000, 55000, 72000, 67000, 52000, 60000, 73000, 68000],
    "JoiningDate": pd.to_datetime([
        "2020-01-15", "2019-03-10", "2021-07-22", "2020-11-01", 
        "2018-05-16", "2019-09-12", "2021-01-10", "2020-06-05", 
        "2019-12-20", "2021-04-08"
    ])
}

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print(df)


#__________________________________________________________________
#CONVERTING PARTICULAR COLUMNS TO LOWERCASE
#__________________________________________________________________

lowered=df["Name"].str.lower()
print(lowered)#all names converts to lower case and returns a 
#series 

#__________________________________________________________________
#CHECKING THE PARTICULAR ELEMENTS ARE IN DATAFRAME OR NOT
#__________________________________________________________________

do_contains=df["Department"].str.contains("hr",case=False)
print(do_contains)

#case= false means do not prioritize the case just check thr word


#__________________________________________________________________
#CONVERITNG THE COLUMN INTO LIST
#__________________________________________________________________

splitting=df["Name"].str.split()
print(splitting)
"""
So this is how you can split your df column in to the list
but this can only be done on the string data type"""


""" Now if there is a an email and if you want to split it
like prashantkashyap@gmail.com, so  if you split this with
using a delimeter like @ then it will be splitted or
separated  into two parts prasahantkashyap,gmail.com and now 
you can perform any action now  lets see one example of it"""

# creating a dataframe

# Employee data
emp_data = {
    "EmployeeID": range(1, 11),
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan", "Neha", "Vikram", "Pooja", "Ravi", "Ananya"],
    "Email": [
        "amit@example.com", "priya@company.com", "rahul@workmail.com", "sneha@office.org",
        "karan@company.com", "neha@example.com", "vikram@workmail.com", "pooja@office.org",
        "ravi@company.com", "ananya@example.com"
    ],
    "Department": ["HR", "IT", "Finance", "Marketing", "IT", "Finance", "HR", "Marketing", "IT", "Finance"],
    "Salary": [50000, 70000, 65000, 55000, 72000, 67000, 52000, 60000, 73000, 68000],
    "JoiningDate": pd.to_datetime([
        "2020-01-15", "2019-03-10", "2021-07-22", "2020-11-01", 
        "2018-05-16", "2019-09-12", "2021-01-10", "2020-06-05", 
        "2019-12-20", "2021-04-08"
    ])
}

# Create DataFrame
data = pd.DataFrame(emp_data)

# Display DataFrame
print(data)

delimeter_splt=data["Email"].str.split("@")
print(delimeter_splt)

#now you can see the output what i am actually want to show you


"""One important thing to be noticed here that the column 
on which we have performed the task is splitted into the 
list, so the inner splitted strings are python lists but the
whole column is still a series"""

"""The whole column is still pandas series you can use the
.loc[],.iloc[],etc., on that column even if all the values
inside that series becomes the list of the strings. """