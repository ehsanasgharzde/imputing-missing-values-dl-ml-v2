########## Importing required libraries
import pandas
import seaborn
from random import choice
from matplotlib import pyplot
from sklearn.linear_model import LinearRegression
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer


########## Loading AMR-NSH-Buoy-Data1394.xls files in a Pandas DataFrame and getting a copy
dataset = pandas.read_excel("AMR-and-NSH-Buoy-Data1394.xls")

########## Multivariate:
########## Slicing out "DateTime Processor" and "SunDateTime"
gregdatetime = pandas.Series(dataset["DateTime Processor"])
solardatetime = pandas.Series(dataset["SunDateTime"])

########## Loading preprocess-normal-dataset-excel.xls files in a Pandas DataFrame and getting a copy
normalizedataset = pandas.read_excel("normalized-xls-files/preprocess-normal-dataset-excel.xls")

########## Finding the number of missing values for every column
print(normalizedataset.isnull().sum())

########## Seperating Bouy Amirabad and Bouy Nosharhr
badataset = normalizedataset[["Buoy Amirabad Battery Voltage(1)",
                              "Buoy Amirabad Air Temperature(1)", 
                              "Buoy Amirabad Air Pressure(1)", 
                              "Buoy Amirabad Air Humidity(1)", 
                              "Buoy Amirabad Wind Speed(1)", 
                              "Buoy Amirabad Wind Direction(1)", 
                              "Buoy Amirabad Wind Gust(1)", 
                              "Buoy Amirabad Water Temperature(1)", 
                              "Buoy Amirabad Water Conductivity(1)", 
                              "Buoy Amirabad Hmax(1)", 
                              "Buoy Amirabad Hm0(1)", 
                              "Buoy Amirabad Tz(1)", 
                              "Buoy Amirabad MDIR(1)"]]

bndataset = normalizedataset[["Buoy Noshahr Battery Voltage(1)",
                              "Buoy Noshahr Air Temperature(1)",
                              "Buoy Noshahr Air Pressure(1)",
                              "Buoy Noshahr Air Humidity(1)",
                              "Buoy Noshahr Wind Speed(1)",
                              "Buoy Noshahr Wind Direction(1)",
                              "Buoy Noshahr Wind Gust(1)",
                              "Buoy Noshahr Water Temperature(1)",
                              "Buoy Noshahr Water Conductivity(1)",
                              "Buoy Noshahr Hmax(1)",
                              "Buoy Noshahr Hm0(1)",
                              "Buoy Noshahr Tz(1)",
                              "Buoy Noshahr MDIR(1)"]]

########## Getting Bouy Amirabad abd Bouy Noshahr columns 
bacolumns = badataset.columns
bncolumns = bndataset.columns

########## Setting all the rows all over again
########## Gregorian date and time for "DateTime Processor"
DAY2MONTH = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,       
    5: 31,
    6: 30,       
    7: 31,       
    8: 31,       
    9: 30,       
    10: 31,  
    11: 30,       
    12: 31,            
}

YEAR = 2015
MONTH = 3
DAY = 20

HOUR = 21

for index in range(len(gregdatetime)):
    SECOND = choice([11, 10, 9, 6, 5, 8])
    
    if HOUR > 23:
        DAY += 1
        HOUR = 0
    
    if DAY2MONTH[MONTH] < DAY:
        MONTH += 1
        DAY = 1
        
    if MONTH > 12:
        YEAR += 1
        MONTH = 1
        
    if SECOND < 10:
        secondstr = f"0{SECOND}"
    else:
        secondstr = f"{SECOND}"
        
    if HOUR < 10:
        hourstr = f"0{HOUR}"
    else:
        hourstr = f"{HOUR}"
        
    if DAY < 10:
        daystr = f"0{DAY}"
    else:
        daystr = f"{DAY}"
        
    if MONTH < 10:
        monthstr = f"0{MONTH}"
    else:
        monthstr = f"{MONTH}"
        
        
    datetimestr = f"{YEAR}-{monthstr}-{daystr} {hourstr}:00:{secondstr}"
    
    gregdatetime[index] = datetimestr
    
    HOUR += 1

########## Solar date and time for "SunDateTime"
DAY2MONTH = {
    1: 31,
    2: 31,
    3: 31,
    4: 31,       
    5: 31,
    6: 31,       
    7: 30,       
    8: 30,       
    9: 30,       
    10: 30,  
    11: 30,       
    12: 29,            
}

YEAR = 1394
MONTH = 1
DAY = 1

HOUR = 1

for index in range(len(solardatetime)):
    SECOND = choice([11, 10, 9, 6, 5, 8])
    
    if HOUR > 23:
        DAY += 1
        HOUR = 0
    
    if DAY2MONTH[MONTH] < DAY:
        MONTH += 1
        DAY = 1
        
    if MONTH > 12:
        YEAR += 1
        MONTH = 1
        
    if SECOND < 10:
        secondstr = f"0{SECOND}"
    else:
        secondstr = f"{SECOND}"
        
    if HOUR < 10:
        hourstr = f"0{HOUR}"
    else:
        hourstr = f"{HOUR}"
        
    if DAY < 10:
        daystr = f"0{DAY}"
    else:
        daystr = f"{DAY}"
        
    if MONTH < 10:
        monthstr = f"0{MONTH}"
    else:
        monthstr = f"{MONTH}"
        
        
    datetimestr = f"{YEAR}-{monthstr}-{daystr} {hourstr}:30:{secondstr}"
        
    solardatetime[index] = datetimestr
    
    HOUR += 1
    

timeseriesdataset = pandas.concat([gregdatetime, solardatetime], axis=1)

########## Setting linearregression and iterativeimputer
linreg = LinearRegression()
iterimp = IterativeImputer(estimator=linreg, max_iter=5000, tol=1e-12, verbose=2, imputation_order="roman")

########## Activating the iterativeimputer
bavalues = iterimp.fit_transform(badataset)
bnvalues = iterimp.fit_transform(bndataset)

########## Creating the datasets again
badataset = pandas.DataFrame(bavalues)
badataset.columns = bacolumns

bndataset = pandas.DataFrame(bnvalues)
bndataset.columns = bncolumns

########## Combining the badataset and bndataset and timeseriesdataset
micedataset = pandas.concat([timeseriesdataset, badataset, bndataset], axis=1)

########## Finding the number of missing values for every column
print(micedataset.isnull().sum())

########## Analyse the data in non-time columns
########## Buoy Amirabad Battery Voltage(1)
figure, axus = pyplot.subplots(figsize=(10, 10))
seaborn.distplot(micedataset["Buoy Amirabad Battery Voltage(1)"])


########## Creating a csv file
micedataset.to_csv("multivariate-method-results/AMR-and-NSH-Buoy-Data1394-normalized-mice.csv")