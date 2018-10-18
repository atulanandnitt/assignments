# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 09:28:48 2018

@author: Atul Anand
"""

import json
import os
import pandas as pd
import time
import datetime


    
def findMonthNo(monthName):
    monthName = monthName.strip()
    if monthName =="Jan":   return 1
    elif monthName == "Feb": return 2
    elif monthName == "Mar": return 3
    elif monthName == "Apr": return 4
    elif monthName == "May": return 5
    elif monthName == "Jun": return 6
    elif monthName == "Jul": return 7
    elif monthName == "Aug": return 8
    elif monthName == "Sep": return 9
    elif monthName == "Oct": return 10
    elif monthName == "Nov": return 11
    elif monthName == "Dec": return 12
        
    
    
def find_date_dateFormat(date):    
    dateDetails = date.split()
    dateYear = int(dateDetails[-1])
    dateMonth = int(findMonthNo(dateDetails[1]))
    datedate = int(dateDetails[2])
    dateHr= int(dateDetails[3].split(":")[0])
    dateMin = int(dateDetails[3].split(":")[1])
    #dateSec = int(dateDetails[3].split(":")[2])
    sol = datetime.datetime(dateYear, dateMonth, datedate, dateHr, dateMin)
    print(datetime.datetime(dateYear, dateMonth, datedate, dateHr, dateMin))
    
    return sol

  
    

def createCSVFile(alreadProcessedDT,currentDT,rootDir,destination):    
    fileNamesList=[]    
    print("alreadProcessedDT before compare : ",alreadProcessedDT)
    print("currentDT before compare : ",currentDT )

    for folder,subFolder,fileNamesList in os.walk(rootDir):
        print("fileNames are ", fileNamesList, type(fileNamesList))
        
 
    for jsonFileName in fileNamesList:    
        abs_json_fileName = rootDir + jsonFileName
        createdDate = time.ctime(os.path.getctime(abs_json_fileName))
        
        createdDate_dateFormat = find_date_dateFormat(createdDate)
       
        if createdDate_dateFormat < alreadProcessedDT :
            continue
            
        print("alreadProcessedDT",alreadProcessedDT)
        print("currentDT",currentDT )
        with open(abs_json_fileName) as file:
            data = json.load(file)
            print("data : ", data)
            df = pd.io.json.json_normalize(data)

            df.columns = df.columns.map(lambda x: x.split(".")[-1])
            abs_csvFileName = destination + jsonFileName.split(".")[0] + ".csv"
            abs_csvFileName = str(abs_csvFileName)
            
            df.to_csv(abs_csvFileName, encoding='utf-8', index=False)
            
            
    return currentDT


def getDetailsFromConfigFile(fileName):
    with open(fileName,"r") as configData:
        completeData = configData.readlines()
        print(completeData, type(completeData))
        for data in completeData:
                
            if data.split("=")[0].strip() == "time":
                t = int(data.split("=")[1])
            if data.split("=")[0].strip() == "rootDir":
                rootDir = data.split("=")[1].strip()
                print("got the value of rootDir", rootDir)
            if data.split("=")[0].strip() == "destination":
                destination  = data.split("=")[1].strip()

    return t,rootDir,destination           
                

if __name__ == "__main__":# ????
    
    t=0
    rootDir=""
    destination=""
    
    t,rootDir,destination = getDetailsFromConfigFile("details.config")
             
                
        
    print("time to wait :", t)
    print("t,rootDir,destination  ",t,rootDir,destination)
    startOfFileTime = "Mon Oct 01 00:00:00 2018"
    #startOfFileTime = "Mon Jan 01 00:00:00 2001"
    alreadProcess_dateFormat = find_date_dateFormat(startOfFileTime)
    
    while True:
        time.sleep(t)
        
        currentDT = datetime.datetime.now()
        alreadProcess_dateFormat = createCSVFile(alreadProcess_dateFormat,currentDT,rootDir,destination)
        print("alreadProcess_dateFormat ", alreadProcess_dateFormat)
        
        
    print("done")
                
