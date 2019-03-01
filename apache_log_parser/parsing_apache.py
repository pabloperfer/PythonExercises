filepath = input("\n\nEnter filename path > ") 
file_object = open(filepath)
#Global variables 
Top10Requesting = {}
Top10IpList=[]
Top5Requesting = {}
Ip_Position = 0
Site_Position = 6
Code_Position  = -2
Top10Sites = {}
Top10Fail = {}


def FirsWalk(object):
    file_object = open(filepath)
    """reads every line in the file and invokes the correspondent function for each use case"""
    file_line = file_object.readline()
    while file_line:
        linesplitted = file_line.split()
        Top10IPs(linesplitted)
        Top10Pages(linesplitted)
        Top10Unsuccessful(linesplitted) 
        file_line = file_object.readline()

"""i need to read the file again after i got the top 10 ips in order to get the top 5
sites requested only from those 10 ips. It't not possible to do it in the first read """ 

def SecondWalkAfterTop10IPs(object):
    file_object.seek(0)
    file_line = file_object.readline()
    while file_line:
        linesplitted = file_line.split()
        Top5PagesforTop10IPs(Top10IpList,linesplitted)
        file_line = file_object.readline()

def Top10IPs(splitted):
    """
    Creates a dictionary with the IPs making the most requests displaying the IP address and number of requests made for each.
    """
    ###we check the ips that are repeated and how many times
    if (splitted[Ip_Position]) not in Top10Requesting:
        Top10Requesting[(splitted[Ip_Position])]=1
    else:
        Top10Requesting[(splitted[Ip_Position])]+=1


def PrintFinalDict(dict,topnumber,banner):         
    """we print the correspondent banner and number of top requests for each case"""
    print (f"\n\n{banner}\n")
    print ("======================")
    i = 0
    if (len(Top10IpList) == 0) : 
        for key, value in sorted(dict.items(),reverse=True ,key=lambda x: x[1]):
            if i < topnumber :
                print(f"\n  {key}    count {value}")
                Top10IpList.append(key)
                i+=1
    else:
        for key, value in sorted(dict.items(),reverse=True ,key=lambda x: x[1]):
            if i < topnumber :
                print(f"\n  {key}    count {value}")
                i+=1
          
    print ("\n")   

def Top5PagesforTop10IPs(Top10IpList,splitted):
    """
    For each of the top 10 IPs, create a dict with the top 5 pages succesful requested" 
    """
    
    if (int(splitted[Code_Position ]) > 199 and int(splitted[Code_Position ]) < 400):
        if  splitted[Ip_Position] in Top10IpList: 
            if splitted[Site_Position] not in Top5Requesting:
                Top5Requesting[(splitted[Site_Position])]=1                 
            else:
                Top5Requesting[(splitted[Site_Position])]+=1                 


def Top10Pages(splitted):
    """ Top 10 requested pages and the number of requests made for each """
    if (splitted[Site_Position]) not in Top10Sites:
        Top10Sites[(splitted[Site_Position])]=1                 
    else:
        Top10Sites[(splitted[Site_Position])]+=1                 
               
def Top10Unsuccessful(splitted) : 
    """Top 10 unsuccessful page requests"""
    if (int(splitted[Code_Position ]) > 399 and int(splitted[Code_Position ]) < 522 ):
        if (splitted[Site_Position]) not in Top10Fail:
            Top10Fail[(splitted[Site_Position])]=1
        else:
            Top10Fail[(splitted[Site_Position])]+=1


FirsWalk(file_object)
PrintFinalDict(Top10Requesting,10,"######## TOP 10 IPs #######")
PrintFinalDict(Top10Sites,10,"##### TOP 10 sites requested in total ####")
PrintFinalDict(Top10Fail,10,"##### TOP 10 failed sites requested in total ####")
SecondWalkAfterTop10IPs(file_object)
PrintFinalDict(Top5Requesting,5,"### Top 5 Sites requested by top 10 IPS ###")
file_object.close
