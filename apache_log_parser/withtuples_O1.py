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

#we create a list of dictionaries with each named tuple
while File_line:
    Line_splitted = File_line.split()
    Record = Request((Line_splitted[Ip_position]),(Line_splitted[Site_position].split('?')[0]),(Line_splitted[Code_position]))
    Record_dict= Record._asdict() 
    request_list.append(Record_dict)
    File_line = File_object.readline()


File_object.close


def Print_final(Dict,Topnumber,banner):
    """we print the correspondent banner and number of top requests for each case"""
    print (f"\n{banner}\n")
    i = 0
    for key, value in sorted(Dict.items(),reverse=True ,key=lambda x: x[1]):
        if i < Topnumber :
            print(f" {key} : count {value}," ,end = ' ' )
            i+=1

    print ("\n")


# we walk the list of dictionaries for the tops that depend on a second index pattern

####Using counter to count all the IP occurrences and return the 10 most common ip requesting
print ("Top 10 IPs#########\n")
print(Counter(x['ip'] for x in request_list).most_common(10)); print ("\n")
Top10ip=(Counter(x['ip'] for x in request_list).most_common(10));
#we unpack the tuple count in order to find the top 5 from these ips new list
Top10list=[]
for i in range(0,10):
    ip,count = Top10ip[(i)]
    Top10list.append(ip)



###Top 10  sites
print ("Top 10 Sites#########\n")
print(Counter(x['site'] for x in request_list).most_common(10))


###Top 10 unsucessful
Top10_fail = {}

for d in request_list:
    if int(d['code']) >399 and int(d['code']) <522:
        if d['site'] not in Top10_fail:
            Top10_fail[(d['site'])]=1
        else: 
            Top10_fail[(d['site'])]+=1

Print_final(Top10_fail,10,"Top 10 failed sites requested in total #########")

#Top5sitesfortop10ips
Top5Success_fortop10 = {}

for d in request_list:
    if int(d['code']) > 199 and int(d['code'])  <399 and d['ip'] in Top10list:
        if (d['site']) in Top5Success_fortop10:
            Top5Success_fortop10[(d['site'])]+=1
        else:
            Top5Success_fortop10[(d['site'])]=1

Print_final(Top5Success_fortop10,5,"Top 5 sites visited for the top 10 ips####")


