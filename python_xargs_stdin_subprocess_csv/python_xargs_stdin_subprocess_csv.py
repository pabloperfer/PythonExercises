''' 

receives the input of a csv file and behaves like xargs 
xargs reads items from the standard input, delimited by blanks and executes the command 

echo users.csv | python3 python_xargs_stdin_subprocess_csv.py  useradd -e 2080-03-27 -U 
['useradd', '-e', '2080-03-27', '-U', 'frankriley']
useradd: user 'frankriley' already exists
['useradd', '-e', '2080-03-27', '-U', 'stevebrannigan']
['useradd', '-e', '2080-03-27', '-U', 'marieambrose']

In this example we create all the users that shows up in the csv file in a linux system concatenating first and last name of each user.
We expect only one input in the stdin, the name of the csv file and an infinite numebr of arguments
we'd use subprocess.call

''' 

import sys,csv,subprocess,logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


### we create a string for the command and its possible arguments.

if len(sys.argv) < 1  :
    print("This program needs at least one argument")
    sys.exit(1)

command =  sys.argv[1]
args=[]
#args.append(command)

for i in sys.argv[1:]:
    args.append(i)

for line in sys.stdin:         ####we get a string with the stdin filename to parse later
    filename = line.rstrip()

user=""
users = []

try:

    with open(filename) as f:      ### we open the file and create csv reader object to go through it
        reader = csv.reader(f)
        next(reader)                 ### we forward one line the position of the reader 
        for row in reader:           
            user = row[0]+row[1]  
            user= user.lower()
            args.append(user)  
            print(args)
            subprocess.call(args)
            del args[-1]
except Exception:
    log.exception("Execution has failed!")


