import math
import numpy as np
import pandas as pd

# available investment amounts
deposits = np.array([1000, 2000, 3000, 4000, 5000, 7800])
# available annual interest rates
rates = np.array([0.03, 0.04, 0.045, 0.0510,0.03,0.06])

investors = np.array(["Sally", "Barnabas", "Donald", "Lisa", "Julio", "On-uma"])

ones = np.ones(6, dtype = int)

hundred = ones*100

# routine for simple interest
def simpInt(principal, rate, time) :
    futureVal = principal * (1 + rate * time)
    # futureVal = np.multiply(principal,np.add(1,np.multiply(rate,time)))
    return futureVal.astype(int)


# routine for compound interest
def compInt(principal, rate, freq, time) :
    cmpAmt = principal * (1 + rate / freq) ** (freq * time)
    return np.around(cmpAmt,2)

# routine for precise formula to double investment
def doubleTime(rate, freq) :
    # dblMe = math.log(2) / math.log(1 + rate / freq)
    dblMe = np.log(2)/np.log(1+rate/freq)
    return dblMe.round(decimals=2)
double_Time = doubleTime(rates*100, hundred)

def ruleOf72(rate, period):
    if np.array_equal(period,"annual"):
        return np.divide(72,rate).round(decimals=2)
    elif np.array_equal(period,"semi-annual"):
        return np.divide(72,(np.divide(rate,2))).round(decimals=2)
    else:
        print("It is invalid input.\nPlease choose either annual or semi-annual as a 2nd argument instead of >>",period)

#change rate to be in percentage by multiplying with 100
rule_72 = ruleOf72(rates*100,"annual")


#Check The accuracy of rule of 72(prediction)
def accuDoubTime(Va,Vm):
    acDoubTm = np.absolute(Va-Vm)*100/Va
    return 100-acDoubTm.round(decimals=2)
ac2Times =  accuDoubTime(double_Time,rule_72)


# routine for precise formula to double investment
def tripleTime(rate, freq) :

    trplMe = np.log(3)/np.log(1+rate/freq)
    return trplMe.round(decimals=2)
triple_Time = tripleTime(rates*100, hundred)

#Check The accuracy of rule of 115(prediction)
def ruleOf115(rate, period):
    if np.array_equal(period,"annual"):
        return np.divide(115,rate).round(decimals=2)
    elif np.array_equal(period,"semi-annual"):
        return np.divide(115,(np.divide(rate,2))).round(decimals=2)
    else:

        print("It is invalid input.\nPlease choose either annual or semi-annual as a 2nd argument instead of >>",period)

#change rate to be in percentage by multiplying with 100
rule_115 = ruleOf115(rates*100,"annual")

#Va = value of accuracy , Vm = value of measurement
def accuTripTime(Va,Vm):
    acTripTm = np.absolute(Va-Vm)*100/Va
    return 100-acTripTm.round(decimals=2)
ac3Times =  accuTripTime(triple_Time,rule_115)

print("\n-----------------------Data Frame part 1--------------------------\n")
print("\nDataFrame from Pandas using zip to combine the dataframe and call the variables from each functions\n")
ind = np.array([1,2,3,4,5,6])
col = np.array(["Invester", "Deposite", "Interest rate", "Double Time", "Rule 72","Accuracy rule 72", "Triple Time","Rule 115", "Accuracy rule115"])
df = pd.DataFrame(list(zip(investors,deposits,rates, double_Time , rule_72,ac2Times, triple_Time, rule_115, ac3Times)),columns = col, index = ind)
pd.set_option('display.max_columns', 200)


print("\nPrint all the data\n")
print(df)

#Slicing Based on columns
print("\nDisplay the prediction and correction of rule of 72 as well as the accuracy of the both of them\n"
      "Slicing using list df.iloc[list of row, list of column]\n")

print(df.iloc[[0,1,2,3,4,5],[0,1,2,3,4,5]])

#drop row of On-uma by .drop("6") or .head() it will print the first 5 rows.
print("\nRomoving On-uma's row to remain 5 investers\n"
      "Slicing using df.iloc[range of row , rang of column].head()  --> .head() will display first 5 rows\n")
print(df.iloc[:,:6].head())

#The average of double time of 5 investers without On-uma(The 6th invester)

mean_doubleTime = np.mean(double_Time[:-1]).round(decimals = 2)
#print(double_Time[0:-1])
print(f"\nMean of double time of 5 investers is {mean_doubleTime} years.\n")


print("\nDisplay the prediction and correction of rule of 115 as well as the accuracy of the both of them\n"
      "Slicing using df.iloc[].drop(index)--> drop(index) will remove that specificed row")
print(df.loc[:,list(df.columns[:3])+list(df.columns[6:])].drop(6))
#The average of triple time of 5 investers without On-uma(The 6th invester)

mean_tripleTime= np.mean(triple_Time[:-1]).round(decimals=2)
#print(triple_Time[:-1])
print(f"\nMean of triple time of 5 investers is {mean_tripleTime} years.\n")



print("Generating Descriptive Statistics on the DataFrame\n")
print(df.describe())
print("\n-----------------------Data Frame part 2--------------------------\n")
# variables for the data frame
print("\nDataFrame with the for loop\n")
cash = 0
time = 0
rows = 3
cols = 3
# generate a data frame
df = [["Ava", 3000, 6], ["Abby", 4000, 5], ["Angie", 5000, 7]]

# display the data frame
for r in range(rows) :
    print(r + 1, "\t", end = "")
    for c in range(cols) :
        print(df[r][c], "\t", end = "")
    print()
print()


print("\n-----------------------Data Frame part 3--------------------------\n")
print("DataFrame from Pandas\n"
      "1.) Adding columns\n"
      "2.) Manipulating data with apply() from existing data\n"
      "3.) Creating lambda functions to manipulate data\n"
      "4.) Finding average of doubling time & tripling time using mean().\n")
df2 =  [["Ava", 3000, 6], ["Abby", 4000, 5], ["Angie", 5000, 7],["Joe", 4500,4.5],["Chris", 5500,5.5]]


dF = pd.DataFrame(df2, columns = ["Name", "Deposit","Interest Rate"], dtype = float)


#adding more columns
# using apply()
dF["Rule of 72"] = dF["Interest Rate"].apply(lambda x : 72/x).round(decimals = 2)



dF["Double Time"] = dF["Interest Rate"].apply(lambda x : math.log(2)/math.log(1+x/100)).round(decimals=2)


dF["Rule of 115"]= dF["Interest Rate"].apply(lambda x: 115/x).round(decimals = 2)

dF["Triple Time"] = dF["Interest Rate"].apply(lambda x: math.log(3)/math.log(1+x/100)).round(decimals=2)

dF["Rule72's % Accuracy"] = dF.apply(lambda row : 100-(np.absolute(row["Double Time"]-row["Rule of 72"])*100/row["Double Time"]), axis=1).round(decimals=2)
dF["Rule115's % Accuracy"] = dF.apply(lambda row : 100-(np.absolute(row["Triple Time"]-row["Rule of 115"])*100/row["Triple Time"]), axis=1).round(decimals=2)
print(dF)
print("The Average of double time of these 5 investors is ",dF["Double Time"].mean())
print("The Average of triple time of these 5 investors is ",dF["Triple Time"].mean())

print("\nCompare compInt function and rule of 72\n")
x = compInt(1000,0.03,1,12)
y = ruleOf72(3,"annual")
print(f"Compound interest in 12 years of principal amount of 1000 of 3% interest rate is ${x}.")
print(f"Also, Rule of 72 indicates that this interest rate will double in {y} years.")