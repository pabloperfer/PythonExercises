import re

filepath = input("\n\nEnter filename path > ") 

file_object = open(filepath)

file_lines = file_object.readlines()


def Top10IPs(lines):
    """
    Show the top 10 IPs making the most requests, displaying the IP address and number of requests made for each.
    """
    top10requesting = {}
    #we iterate all the lines in the file 
    for line in file_lines:
        splitted=line.split()
    ###we check the ips that are repeated and how many times
        if (splitted[0]) not in top10requesting:
            top10requesting[(splitted[0])]=1
        else:
            top10requesting[(splitted[0])]+=1
         
    ###we print the ips in order by adding an inline function that adds the second element ,the value,to be passed to the sort function 
    print ("\n\n########### TOP 10 IPS #############\n")
    print ("======================")
    i = 0
    outputlist=[]
    for ip, count in sorted(top10requesting.items(),reverse=True ,key=lambda x: x[1]):
        if i < 10 :
            print(f"\nip : {ip}    count {count}")
            i+=1
            outputlist.append(ip)
     
    
    return outputlist


def Top5PagesforTop10IPs(top10list,lines):
    """
    For each of the top 10 IPs, this shows the top 5 pages requested and the number of requests for each. (anything 2xx or 3xx)
    """
    top5requesting = {}

    for ip in top10list:
        for line in lines:
            if ip in line:          
                splitted=line.split()
                if re.match(("^[2-3]"), (splitted[-2])): 
                    if (splitted[6]) not in top5requesting:
                        top5requesting[(splitted[6])]=1                 
                    else:
                        top5requesting[(splitted[6])]+=1                 

                else :
                    continue
    i = 0
    print (f"\n ########## Top 5 Sites requested by top 10 IPS ########\n")
    for site, count in sorted(top5requesting.items(),reverse=True, key=lambda x: x[1]):
        if i<5:
            i+=1
            print(f"\n site: {site} count : {count}") 

def Top10pages(lines):
    """ Top 10 requested pages and the number of requests made for each """
    top10sites = {}
    for line in lines:
        splitted=line.split()       
        if (splitted[6]) not in top10sites:
            top10sites[(splitted[6])]=1                 
        else:
            top10sites[(splitted[6])]+=1                 
               
    print (f"\n ########## TOP 10 SITES REQUESTED ########\n")
    i=0
    for site, count in sorted(top10sites.items(),reverse=True, key=lambda x: x[1]):
        if i<5:
            print(f"\n site: {site} count : {count}") 
            i+=1
                
def Top10Unsuccessful(lines) : 
    """Top 10 unsuccessful page requests"""
    top10fail = {}
    for line in lines:
        splitted=line.split()
        if re.match(("^[4-5]"), (splitted[-2])):
            if (splitted[6]) not in top10fail:
                top10fail[(splitted[6])]=1
            else:
                top10fail[(splitted[6])]+=1

        else :
            continue
    i = 0
    print (f"\n ########## Top 10 site requests failed  ########\n")
    for site, count in sorted(top10fail.items(),reverse=True, key=lambda x: x[1]):
        if i<10:
            i+=1
            print(f"\n site: {site} count : {count}")
    print ("\n")
outputlist=Top10IPs(file_lines)
Top5PagesforTop10IPs(outputlist,file_lines)
Top10pages(file_lines)
Top10Unsuccessful(file_lines)


file_object.close
