File_path = input("\n\nEnter filename path > ") 
File_object = open(File_path)
#Global variables 
Top10_requesting = {}
Top10_iplist=[]
Top5_requesting = {}
Ip_position = 0
Site_position = 6
Code_position  = -2
Top10_sites = {}
Top10_fail = {}


def First_walk(object):
    File_object = open(File_path)
    """reads every line in the file and invokes the correspondent function for each use case"""
    File_line = File_object.readline()
    while File_line:
        Line_Splitted = File_line.split()
        Top_10ips(Line_Splitted)
        Top10_pages(Line_Splitted)
        Top10_unsuccessful(Line_Splitted) 
        File_line = File_object.readline()

def Second_walk(object):
    File_object.seek(0)
    File_line = File_object.readline()
    while File_line:
        Line_Splitted = File_line.split()
        Top5_pages(Top10_iplist,Line_Splitted)
        File_line = File_object.readline()

def Top_10ips(Splitted):
    """
    Creates a dictionary with the IPs making the most requests displaying the IP address and number of requests made for each.
    """
    ###we check the ips that are repeated and how many times
    if (Splitted[Ip_position]) not in Top10_requesting:
        Top10_requesting[(Splitted[Ip_position])]=1
    else:
        Top10_requesting[(Splitted[Ip_position])]+=1


def Print_final(Dict,Topnumber,banner):         
    """we print the correspondent banner and number of top requests for each case"""
    print (f"\n\n{banner}\n")
    print ("======================")
    i = 0
    if (len(Top10_iplist) == 0) : 
        for key, value in sorted(Dict.items(),reverse=True ,key=lambda x: x[1]):
            if i < Topnumber :
                print(f"\n  {key}    count {value}")
                Top10_iplist.append(key)
                i+=1
    else:
        for key, value in sorted(Dict.items(),reverse=True ,key=lambda x: x[1]):
            if i < Topnumber :
                print(f"\n  {key}    count {value}")
                i+=1
          
    print ("\n")   

def Top5_pages(Top10_iplist,Splitted):
    """
    For each of the top 10 IPs, create a dict with the top 5 pages succesful requested" 
    """
    
    if (int(Splitted[Code_position ]) > 199 and int(Splitted[Code_position ]) < 400):
        if Splitted[Ip_position] in Top10_iplist: 
            Pure_url=Splitted[Site_position].split('?')[0]
            if Pure_url not in Top5_requesting:
                Top5_requesting[Pure_url]=1                 
            else:
                Top5_requesting[Pure_url]+=1                 


def Top10_pages(Splitted):
    """ Top 10 requested pages and the number of requests made for each """
    if (Splitted[Site_position]) not in Top10_sites:
        Top10_sites[(Splitted[Site_position])]=1                 
    else:
        Top10_sites[(Splitted[Site_position])]+=1                 
               
def Top10_unsuccessful(Splitted) : 
    """Top 10 unsuccessful page requests"""
    if (int(Splitted[Code_position ]) > 399 and int(Splitted[Code_position ]) < 522 ):
        if (Splitted[Site_position]) not in Top10_fail:
            Top10_fail[(Splitted[Site_position])]=1
        else:
            Top10_fail[(Splitted[Site_position])]+=1


First_walk(File_object)
Print_final(Top10_requesting,10,"######## TOP 10 IPs #######")
Print_final(Top10_sites,10,"##### TOP 10 sites requested in total ####")
Print_final(Top10_fail,10,"##### TOP 10 failed sites requested in total ####")
Second_walk(File_object)
Print_final(Top5_requesting,5,"### Top 5 Sites requested by top 10 IPS ###")
File_object.close
