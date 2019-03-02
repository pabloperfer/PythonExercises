import collections
from collections import Counter

#Global variables
File_path = input("\n\nEnter filename path > ")
Ip_position = 0
Site_position = 6
Code_position  = -2

#Opening file
File_object = open(File_path)

#We create a named tuple with the 3 values from the logs we'll need
Request = collections.namedtuple('Request', 'ip, site, code')

#We create a list to store all the requests of apache and a dictionary to mix all of them later in a single dict
request_list=[]
#We read the log file line by line, for each we create an instance of a named tuple
File_line = File_object.readline()

while File_line:
    Line_splitted = File_line.split()
    Record = Request((Line_splitted[Ip_position]),(Line_splitted[Site_position].split('?')[0]),(Line_splitted[Code_position]))
    Record_dict= Record._asdict() 
    request_list.append(Record_dict)
    File_line = File_object.readline()


File_object.close



####Using counter to count all the IP occurrences and return the 10 most common
print ("Top 10 IPs#########\n")
print(Counter(x['ip'] for x in request_list).most_common(10))




