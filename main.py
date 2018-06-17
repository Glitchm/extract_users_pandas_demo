import pandas as pd
from pandas import DataFrame

lastName = []
noList = ['/', '\n', '\t', ' ']

with open("security.txt") as myFile:
    data = myFile.readlines()

USUsers = pd.read_excel('employees.xls', sheet_name='US')
UKUsers = pd.read_excel('employees.xls', sheet_name='UK')
KoreaUsers = pd.read_excel('employees.xls', sheet_name='Korea')

allUsers = DataFrame(UKUsers)
allUsers = allUsers.append(USUsers, ignore_index=True)
allUsers = allUsers.append(KoreaUsers, ignore_index=True)

i = [i.split('/home', 1)[0] for i in data]
userName = [i.split(':x:', 1)[0] for i in data]
Name = [i.split(',,,', 1)[0] for i in data]
fullName = [i.split(':')[-1] for i in Name]
firstName = [i.split(' ')[0] for i in fullName]
lastNamesplit = [i.split(' ')[-1] for i in fullName]
servers = [i.split('\t') for i in data]

usersNotFound = []
firstNotFound = []

for x, y in zip(lastNamesplit, firstName):
    if x not in allUsers['Last Name'].values.tolist():
        if noList.__str__() in x:
            continue
        else:
            usersNotFound.append(x)
            firstNotFound.append(y + ' ')

firstNotFound = DataFrame(firstNotFound)
firstNotFound = firstNotFound + DataFrame(usersNotFound)

uniqueUsers = DataFrame.drop_duplicates(firstNotFound)

print(uniqueUsers)
DataFrame.to_csv(uniqueUsers, "Unique Users.csv")
