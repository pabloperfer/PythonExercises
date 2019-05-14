receives the input of a csv file and behaves like xargs

#xargs reads items from the standard input, delimited by blanks and executes the command 

#like :   echo users.csv | python3 myxargs.py useradd -e 2080-03-27

#In this example we create only the first user that shows up in the cxv file in a linux system concatenating first and last #name of each user.
#We expect only one input in the stdin, the name of the csv file
#because only use execution is going to be done we use os.execvp which replaces the current program execution. If we needed to #add all of the users in the csv file we'd use subprocess.call
