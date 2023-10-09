# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 19:10:31 2021

@author: Chin Chee Kai
Date:         2021 Sep 24
Organisation: Nanyang Business School, NTU
Program:      MSc Accountancy
Course:       MAPY Python Programming
Session:      18
Title:        Exercise Solutions
Question:     Q1,Q2,Q3,Q4,Q5,Q6
Subject:      Writing A Simple but Useful App
              Robust User Input Float Function
"""
from datetime import datetime as dtt

## Q1
##

def inputDate(prompt, fmt, minValue="19700101", maxValue=None,
              exitStr=None):
    """Gets a date from the user in the format specified by
    fmt, which follows the datetime.strftime() format.
    minValue and maxValue are string dates which are converted
    to datetimes for bounds checks - ie input date must be
    within these specified dates, if not None.
    """
    minDate  = (dtt(int(minValue[:4]), int(minValue[4:6]),
                    int(minValue[6:8])) if minValue is not None
                else None)
    maxDate  = (dtt(int(maxValue[:4]), int(maxValue[4:6]),
                    int(maxValue[6:8])) if maxValue is not None
                else None)
    finalDate = None
    done = False
    while True:
        inp = input(prompt).strip()
        if inp == "":  continue
        if inp == "stop":  break
        if inp == "show":
            print("Example: 20230801 for year 2023 August 1st.")
            continue
        if inp == exitStr:   break
        try:  ### May fail if format is not right
            dtt2   = dtt.strptime(inp, fmt)
        except:
            dtt2   = None
        if dtt2 is None:
            print(f"Please enter date in the form \"{fmt}\".")
            continue
        #
        if minDate is not None and dtt2 < minDate:
            print(f"Please enter date that is not earlier than \"{minDate.strftime(fmt)}\".")
        #
        if maxDate is not None and dtt2 > maxDate:
            print(f"Please enter date that is not later than \"{maxDate.strftime(fmt)}\".")
        #
        # Ok, pass all tests
        finalDate = dtt2
        done = True
        break
    #
    return finalDate


## Q2  inputFloat()

def inputFloat(prompt, minValue=0, maxValue=999999, dp=2,
              skipStr="s", exitStr=None):
    nan = float("nan")
    v = None
    while True:
        inp = input(prompt)
        inp = inp.strip()
        if inp == "":
            print("Enter a decimal value (eg 21.34).")
            continue
        if inp.upper() == "STOP":
            print("Aborted.")
            v = None
            break
        if (exitStr is not None) and (inp == exitStr):
            return None
        if (skipStr is not None) and (inp == skipStr):
            return nan
        # Convert to float
        try:
            v = float(inp)
        except:
            continue
        ### is v in range?
        if not(minValue <= v <= maxValue):
            print(f"Entered amount \"{v}\" is not in range [{minValue}, {maxValue}].  Please re-enter.")
            continue
        # v is float and in range
        v = round(v, dp)
        print(f"Value entered is \"{v}\".")
        break
    #
    return v


# Q3(a) & (b)
def inputMoney(prompt, maxValue=10000,
              skipStr="SKIP", exitStr="EXIT"):
    money = inputFloat(prompt,minValue=0.0,
                       maxValue=maxValue, dp=2, 
                       skipStr=skipStr, exitStr=exitStr)
    return money
    ## Q3(b):  Yes, there is value in defining a 
    ## "thin" function like inputMoney(), because 
    ## (1) the name gives a clear manifest of the 
    ## intention of inputing this floating point number,
    ## and (2) the format of money is mostly fixed at 
    ## 2dp and non-negative - so this function can
    ## enforce that for all monetary floats.
    
    
# Q4
def inputAccountCode(prompt, permittedCodeList, exitStr=""):
    while True:
        codeInp = input(prompt)
        codeInp = codeInp.strip().upper()
        if codeInp == exitStr:  break
        if codeInp == "SHOW":
            print("Permitted codes are:")
            for code in permittedCodeList:
                print(f"{code}, ", sep="", end="")
            #
            print("\n")
            continue
        if codeInp == "STOP":
            print("Account code entry stopped.")
            break
        if codeInp in permittedCodeList:    return codeInp
        print(f"{codeInp} is not in permitted code list.  Type 'show' to show codes, ''stop' to stop.  Please re-enter.")
    return None

## Q5(a)
def inputText(prompt, nchar=30):
    while True:
        txt = input(prompt)
        if txt == "":
            print("Enter a text description.  Type 'stop' to stop.")
            continue
        if txt.upper() == "STOP":
            break
        ntxt = len(txt)
        if ntxt <= nchar:  return txt
        p = f"Input has {ntxt} characters which is longer than {nchar}.\n\Only the first {nchar} will be processed.\n\
Are you ok with that? Please enter 'yes' or 'no': "
        while True:
            yn = input(p)
            yn = yn.strip().lower()
            if yn in ["yes","no"]:   break
        #
        if yn == "yes":   return txt[:nchar]
        ## Otherwise yn is a "no" and so we continue
    return None

## Q5(b)
def inputDescription(prompt, nchar=30):
    desc = inputText(prompt, nchar=nchar)
    return desc


## Q6(a)
def displayMenu():
    print(f"""\
1. Enter a new transaction
2. List all entered transactions
3. Delete all entered transactions
4. Save all transactions to ledger
5. Load transactions to ledger (will delete current)
x. Exit
""")
    return


import csv, os
G_LedgerFilename = "ledger.csv"
G_EnteredTransactions = []
G_TransactionCSVHeader = ["Date", "AcctCode", "DateTransact", "Amount", "Description"]
G_PermittedAccountCodes = ["REV-MAIN", "EXP-SAL", "EXP-RENT",
                           "EXP-TRPT", "EXP-INT", "EXP-BUY",
                           "BS-ASSET", "BS-INV"]

def inputTransaction():
    global G_PermittedAccountCodes, G_EnteredTransactions
    print("Input Transaction.")
    ## A transaction is Date, AcctCode, DateTransact, Amount, Description
    dttToday = dtt.now().strftime("%Y%m%d")
    acctCode = inputAccountCode("Enter Account Code:", G_PermittedAccountCodes)
    if acctCode is None:
        print("Aborted.")
        return
    dttTrans = inputDate("Enter transaction date:", "%Y%m%d")
    if dttTrans is None:
        print("Aborted.")
        return
    ymdTrans = dttTrans.strftime("%Y%m%d")
    amount   = inputMoney("Enter amount transacted:")
    if amount is None:
        print("Aborted.")
        return
    desc   = inputDescription("Enter description:")
    if desc is None:
        print("Aborted.")
        return
    desc = desc.strip()
    ### Register the transaction
    trans = [ dttToday, acctCode, ymdTrans, amount, desc]
    G_EnteredTransactions.append(trans)
    print(f"Inserted new transaction of amount ${amount:.2f}.")


def listTransactions():
    global G_EnteredTransactions
    print("List All Transactions.")
    bars  = "-"*60
    bar   = f"""\
{bars[:13]:13s}{bars[:10]:10s}{bars[:13]:13s}{bars[:15]:15s}---{bars[:20]:20s}
"""
    print(bar)
    for trans in G_EnteredTransactions:
        dttCreate, acctCode, ymdTrans, amount, desc = trans
        dtt1   = dtt(int(dttCreate[:4]), int(dttCreate[4:6]),
                     int(dttCreate[6:8]))
        dttCreate_str = dtt1.strftime("%Y %b %d")
        dtt2   = dtt(int(ymdTrans[:4]), int(ymdTrans[4:6]),
                     int(ymdTrans[6:8]))
        ymdTrans_str  = dtt2.strftime("%Y %b %d")
        ss = f"""\
{dttCreate_str:<13s}{acctCode:<10s}{ymdTrans_str:<13s}{amount:15,.2f}   {desc:<20s}\
"""
        print(ss)
    #
    print(bar)



def deleteAllEnteredTransactions():
    global G_EnteredTransactions
    print("Delete All Entered Transactions.")
    G_EnteredTransactions = []
    print("Done.  All transactions deleted.")
    

def saveTransactionsToLedger():
    global G_LedgerFilename, G_TransactionCSVHeader, G_EnteredTransactions
    print("Save Transactions To Ledger.")
    if len(G_EnteredTransactions) <= 0:
        print("Nothing to save.")
        return
    fs = open(G_LedgerFilename, "w", newline="", encoding="utf-8")
    csvWriter = csv.writer(fs)
    csvWriter.writerow(G_TransactionCSVHeader)
    csvWriter.writerows(G_EnteredTransactions)
    fs.close()
    
def loadTransactionsFromLedger():
    global G_EnteredTransactions, G_LedgerFilename
    print("Load Transactions From Ledger.")
    if len(G_EnteredTransactions) > 0:
        while True:
            p = "There is existing entered transaction.  Continue (will erase) (Enter 'yes' or 'no')?"
            yn = input(p)
            yn = yn.strip()
            if yn in ['yes', 'no']:  break
        #
        if yn == "no":  return
    #
    if os.path.exists(G_LedgerFilename) == False:
        print(f"Ledger file \"{G_LedgerFilename}\" does not exist.")
        return
    fs = open(G_LedgerFilename, "r", newline="", encoding="utf-8")
    csvReader = csv.reader(fs)
    linenum   = 0
    ### Can also perform a check if headerRow's content
    ### is same as G_TransactionCSVHeader.  If not, it's an error.
    arr = []
    for row in csvReader:
        if linenum == 0:  ### Skip the header column names
            headerRow = next(csvReader)
            linenum += 1
            continue
        # Ensure that amount is float type
        try:
            row[3] = float(row[3])
        except:
            row[3] = float("nan")
        #
        arr.append(row)
        linenum += 1
    fs.close()
    G_EnteredTransactions = arr
    

# Q6(b)
def mainMenu():
    while True:
        displayMenu()
        cmd = input("Please enter your command:")
        cmd = cmd.strip()
        if cmd == "x":  break
        if cmd == "1":  inputTransaction()
        elif cmd == "2":    listTransactions()
        elif cmd == "3":    deleteAllEnteredTransactions()
        elif cmd == "4":    saveTransactionsToLedger()
        elif cmd == "5":    loadTransactionsFromLedger()
        else:
            print("Unknown command.  Please re-enter.")
        print("===============\n\n")



if (__name__ == "__main__"):
    mainMenu()
