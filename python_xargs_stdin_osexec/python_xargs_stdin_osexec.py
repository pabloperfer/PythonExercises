''' 

receives the input of a csv file and behaves like xargs 
xargs reads items from the standard input, delimited by blanks and executes the command 
 like :   echo users.csv | python3 myxargs.py useradd -e 2080-03-27

CSV files contain data comma-separated values describing values in a table.:

FIRST NAME ,LAST NAME,USERNAME ,PASSWORD ,EMAIL ADDRESS,PHONE NUMBER,PASSPORT,GROUPS,USERCODE,TITLE,ADDRESS 1 ,ADDRESS 2,CITY,STATE,ZIP
Frank,Riley,friley,changeme,friley@kanab.org,123-456-7890,3,"1,3",1040,Teacher,328 Innovation,Suite # 200 ,state college,PA,16803
Steve,Brannigan,sbrannigan,changeme,sbrannigan@kanab.org,123-456-7890,3,1,1041,Teacher,328 Innovation,Suite # 200 ,state college,PA,16803
Marie,Ambrose,mambrose,changeme,mambrose@kanab.org,123-456-7890,3,1,1042,Teacher,328 Innovation,Suite # 200 ,state college,PA,16803

In this example we create only the first  user that shows up in the cxv file in a linux system concatenating first and last name of each user.
We expect only one input in the stdin, the name of the csv file
because only use execution is going to be done we use os.execvp which replaces the current program execution. If we needed to add all of the users in the csv file we'd use subprocess.call
''' 

import sys,csv,os 

### we create a string for the command and its possible arguments.

command =  sys.argv[1]
args=[]
args.append(command)

for i in sys.argv[2:] :     ##create a list excluding the name of the script with the command args
    args.append(i)
space=" "



for line in sys.stdin:         ####we get a string with the stdin filename to parse later
    filename = line.rstrip()

user=""
users = []


with open(filename) as f:      ### we open the file and create csv reader object to go through it
    reader = csv.reader(f)
    next(reader)                 ### we forward one line the position of the reader 
    for row in reader:           
        print (row)
        user = row[0]+row[1]  
        user= user.lower()
        args.append(user)  
        os.execvp(command, args)
        del args[-1]


# To mimic xargs behaviour, we execute a Python script without spawning a new process inline within the same interpreter by invoking exec





