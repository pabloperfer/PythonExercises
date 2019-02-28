import re

filepath = input("\n\nEnter filename path > ") 

file_object = open(filepath)

file_lines = file_object.readlines()


def Top10IPs(lines):
    """
    Show the top 10 IPs making the most requests, displaying the IP address and number of requests made for each.
    """
    top10requesting = {}
    Ip_position = 0
    #we iterate all the lines in the file 
    for line in file_lines:
        splitted=line.split()
    ###we check the ips that are repeated and how many times
        if (splitted[Ip_position]) not in top10requesting:
            top10requesting[(splitted[Ip_position])]=1
        else:
            top10requesting[(splitted[Ip_position])]+=1
         
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
    site_position = 6
    code_position = -2

    for ip in top10list:
        for line in lines:
            if ip in line:          
                splitted=line.split()
                if (int(splitted[code_position]) > 199 and int(splitted[code_position]) < 309): 
                    if (splitted[site_position]) not in top5requesting:
                        top5requesting[(splitted[site_position])]=1                 
                    else:
                        top5requesting[(splitted[site_position])]+=1                 

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
    site_position = 6
    for line in lines:
        splitted=line.split()       
        if (splitted[site_position]) not in top10sites:
            top10sites[(splitted[site_position])]=1                 
        else:
            top10sites[(splitted[site_position])]+=1                 
               
    print (f"\n ########## TOP 10 SITES REQUESTED ########\n")
    i=0
    for site, count in sorted(top10sites.items(),reverse=True, key=lambda x: x[1]):
        if i<5:
            print(f"\n site: {site} count : {count}") 
            i+=1
                
def Top10Unsuccessful(lines) : 
    """Top 10 unsuccessful page requests"""
    top10fail = {}
    code_position = -2
    site_position = 6
    for line in lines:
        splitted=line.split()
        if re.match(("^[4-5]"), (splitted[code_position])):
            if (splitted[site_position]) not in top10fail:
                top10fail[(splitted[site_position])]=1
            else:
                top10fail[(splitted[site_position])]+=1

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
