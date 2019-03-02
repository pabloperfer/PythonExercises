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

# we walk the list of dictionaries for the tops that depend on a second index pattern
Top10_fail = {}

for d in request_list:
    if int(d['code']) >399 and int(d['code']) <522:
        if d['site'] not in Top10_fail:
            Top10_fail[(d['site'])]=1
        else: 
            Top10_fail[(d['site'])]+=1


def Print_final(Dict,Topnumber,banner):         
    """we print the correspondent banner and number of top requests for each case"""
    print (f"\n{banner}\n")
    i = 0
    for key, value in sorted(Dict.items(),reverse=True ,key=lambda x: x[1]):
        if i < Topnumber :
            print(f" {key} : count {value}," ,end = ' ' )
            i+=1
          
    print ("\n")   

Print_final(Top10_fail,10,"Top 10 failed sites requested in total #########")

####Using counter to count all the IP occurrences and return the 10 most common
print ("Top 10 IPs#########\n")
print(Counter(x['ip'] for x in request_list).most_common(10)); print ("\n")

###The same but with sites
print ("Top 10 Sites#########\n")
print(Counter(x['site'] for x in request_list).most_common(10))

###Top 10 unsucessful
print ("Top 10 Unsuccefulf Requested Sites#########\n")


