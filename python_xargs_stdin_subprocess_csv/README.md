receives the input of a csv file and a command with some arguments
xargs reads items from the standard input, delimited by blanks and executes the command 

echo users.csv | python3 python_xargs_stdin_subprocess_csv.py  useradd -e 2080-03-27 -U 
['useradd', '-e', '2080-03-27', '-U', 'frankriley']
useradd: user 'frankriley' already exists
['useradd', '-e', '2080-03-27', '-U', 'stevebrannigan']
['useradd', '-e', '2080-03-27', '-U', 'marieambrose']

In this example we create all the users that shows up in the csv file in a linux system concatenating first and last name of each user.
We expect only one input in the stdin, the name of the csv file and an infinite numebr of arguments
we'd use subprocess.call

