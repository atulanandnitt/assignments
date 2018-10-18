# Requirement:

Multiple json files ( having data in nested structure)  getting copied in a particular folder.Each json file may have different number of records.This python code parse these json files and add these data into separate Excel files.
Once the existing json files in the source folder is processed,upcoming new json files should get processed at real time.

json data files are stored at #rootDir.
and after processsing converted data in csv should be stored at folder name : #destination

Value for #rootDir,destination
are read from config file #details.config

All Json file need to be processed once only.Rows of the excel data should not be repeated.


#Approach:
Step 1 : create a config file and store: src folder location,destination folder location and frequency of python script execution.

Step 2 : All json files at rootDir location which are newer than previous execution, should be processed one by one and the data should be stored corresponding to respective columns.

Future enhancement :  If the frequency is very low: step1 can be made real time, by introducing some trigger concept,that when ever a new json gets populated in source folder the rigger will execute the process of reading json and creating csv. As our assumption is, frequency of incoming json is high we dont need to do this.

