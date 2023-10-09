#######################################################
### MSc Accountancy - Data Analytics
### MP0001 - Python Programming
### Session:  14
### Session Description:  Data Analytics (2/5)
###           Extracting Data
### Q1,Q2,Q3: readCSVFile, writeCSVFile, analysis
### Purpose:  Solution Demo
### Author:   Chin Chee Kai
### Date:     20230712
#######################################################

import pandas as pd, numpy as np
import os, csv

################ Q1

def readCSVFile(filename="population-cn.csv", sourceTF=False):
    fs = open(filename, "r", newline="")
    csvReader = csv.reader(fs)
    rows = []
    line = 0
    for row in csvReader:
        if line == 0:
            headerCol = row
            ncol  = len(headerCol)
            ncol2 = ncol // 2
        else:
            emptyCount = sum(map(lambda ss: len(str(ss))==0, row))
            if emptyCount > ncol2:    break
            rows.append(row)
        #
        line += 1
    #
    fs.close()
    ## Now with data in rows, we can create df
    ##print(rows)
    df  = pd.DataFrame(rows, columns=headerCol)
    ##print(df)
    df.set_index(df.columns[0], inplace=True, drop=True)
    ##print(df)
    df = df.applymap(lambda x: float(x.replace(",","").replace(" ","")))
    ##print(df)
    if sourceTF:
        df = df.applymap(lambda fx: 10000*fx)
    return df


################ Q2

def writeCSVFile(df, columns=None, filename="population3.csv"):
    if df is None or filename == "":    return
    fs = open(filename, "w", newline="")
    if columns is None:
        columns = [str(df.index.name)] + list(df.columns)
    csvWriter = csv.writer(fs)
    csvWriter.writerow(columns)
    nrow, ncol = df.shape
    for i in range(nrow):
        row = [ str(df.index[i]) ] + list(df.iloc[i,:])
        csvWriter.writerow(row)
    #
    fs.close()
    return


################ Q3
def q3(df):
    global femalePop, f1,f0,posWhere
    
    if df is None:  return
    ####### Q3(a)
    # (a) what is total population figure in 2016?
    pop2016 = df.loc[df.index.str.startswith("Total"), "2016"][0]
    print(f"Total population figure in 2016: {pop2016}")
    print("-"*30)
    ####### Q3(b)
    # (b) Which year did female population first start declining?
    femalePop = df.loc[df.index.str.startswith("Female"),:].iloc[0,:].sort_index()
    f1 = femalePop[1:].values
    f0 = femalePop[:-1].values
    diff = f1 - f0
    posWhere  = np.where(diff < 0)[0][0]
    yearFall  = femalePop.index[posWhere]
    print(f"Year when female population starts declining = {yearFall}.")
    print("-"*30)
    ####### Q3(c)
    # (c) Which year is the difference between male and female population
    #      (i) the smallest, (ii) the largest?
    malePop  = df.loc[df.index.str.startswith("Male"),:].iloc[0,:].sort_index()
    diff = abs(malePop - femalePop)
    minDiff = min(diff)
    maxDiff = max(diff)
    pos     = np.where(diff==minDiff)[0][0]
    yearSmallest = diff.index[pos]
    pos     = np.where(diff==maxDiff)[0][0]
    yearLargest  = diff.index[pos]
    print(f"Year when diff between male and female pop is smallest = {yearSmallest}.")
    print(f"Year when diff between male and female pop is largest  = {yearLargest}.")
    print("-"*30)
    
    
    ###### Q3(d)
    # Create a new column in df called “MaleFemaleRatio” which stores the ratio of male population divided by female population, rounded to 4 decimal places
    ratioVec = (malePop / femalePop).round(4)
    dfnew = pd.DataFrame(ratioVec,
                         columns=["MaleFemaleRatio"]).T
    ## malePop & femalePop are sorted ascending.  But df is sorted descending.
    df2 = df.append(dfnew)  ## The index values will auto-align.
    print(df2)
    
    #   (i) In which year was this ratio the smallest? How small was it?
    minValue = min(ratioVec)
    pos = np.where(ratioVec==minValue)[0][0]
    yearSmallest = diff.index[pos]
    print(f"Year when male-to-female ratio was smallest was {yearSmallest}, at a value of {minValue}.")
 
    #   (ii) What is this ratio for year 2020?
    ratio2020 = dfnew.at["MaleFemaleRatio", "2020"]
    print(f"Year 2020 male-to-female ratio was {ratio2020}.")
   
    #   (iii) What pattern in the data (trend/ observations) could you gather about male-to-female-ratio?
    print(dfnew.T)
    
    #   (iv) What social implications might such phenomenon possibly bring to the society/country? (inferences)

    
    
    ###### Q3(e)
    # Create a new column in df called “DiffUrbRur” which stores the difference between urban and rural population (urban – rural). In which year was the annual growth rate of this difference
    urbanPop = df.loc[df.index.str.startswith("Urban"),:].iloc[0,:].sort_index()
    ruralPop = df.loc[df.index.str.startswith("Rural"),:].iloc[0,:].sort_index()
    diffVec = urbanPop - ruralPop
    dfnew = pd.DataFrame(diffVec ,
                         columns=["DiffUrbRur"]).T
    ## urbanPop & ruralPop are sorted ascending.  But df is sorted descending.
    df3 = df.append(dfnew)  ## The index values will auto-align.
    print(df3)
    
    #   (i) the smallest,
    minValue = min(diffVec)
    pos = np.where(diffVec==minValue)[0][0]
    yearSmallest = diffVec.index[pos]
    print(f"Year when urban-rural difference was smallest was {yearSmallest}, at a value of {minValue}.")

    #   (ii) the largest,
    maxValue = max(diffVec)
    pos = np.where(diffVec==maxValue)[0][0]
    yearLargest = diffVec.index[pos]
    print(f"Year when urban-rural difference was largest was {yearLargest}, at a value of {maxValue}.")

    #   (iii) What is the average annual growth rate?
    print(diffVec)
    ur1 = diffVec[1:].values
    ur0 = diffVec[:-1].values
    growthYearly = ur1 - ur0
    print(f"Annual Growth:\n", growthYearly)
    meanGrowthRate = np.mean(growthYearly).item() ### We used sourceTF=True, so no need to (* 10000)
    print(f"Average annual growth rate of urban-rural population = {meanGrowthRate:,.0f} people per year.")
    
    # (iv) Discuss any economic implications to urban cities/ the country if such average annual growth rate of urban-rural difference continues indefinitely (inferences).
    
    
    
    

if (__name__ == "__main__"):
    df = readCSVFile()
    print(df)
    #writeCSVFile(df)
    q3(df)
    