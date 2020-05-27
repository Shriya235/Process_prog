import re
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as md
from  datetime import datetime

"""If required can be used to plot
def Data_Plotting(x,y,title):
    ax=plt.gca()
    xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(xfmt)
    plt.xticks( rotation=30, horizontalalignment='right' )
    plt.plot(x,y)
    plt.title(title)
    plt.xlabel('Duration')
    plt.ylabel(title)
    plt.show()                                                             
    plt.savefig('utilisation.png')
"""
    
def process_data(catch_start,catch_end,process_name,logfile):           #accesses the data portion specified by the parameters
    results = []
    pro=[]
    vsz=[]
    date_time=[]
    variations=[]
    with open(logfile, 'r') as f1:
        lines = f1.readlines()
    i = 0
    while i < len(lines):                                               
        if catch_start in lines[i]:
            for j in range(i + 1, len(lines)):
                if catch_end in lines[j] or j == len(lines)-1:
                    results.append(lines[i:j])
                    i = j
                    break
        else:
            i += 1
    c=0
    d=0
    for a in results:                                               #accessed the part of data, now to find the portions of data having the req process name
        for b in a:
            d+=1                                                    #to keep a count of all lines having process names
            if process_name in b:
                pro.append(re.split(r'[|\s]\s*', b))                #appended the lines of req process in a list(=pro)
            else:
                c+=1                                                #to keep a count if process name is not present in the file
    if c==d:                                                        #if no line has the process name then display the following else do required steps
        print(process_name+" process is not found in this file\n")
    else:
        for x in pro:
            for y in range(len(x)):
                if x[y] == 'root':
                   vsz.append(x[y+1])                               #get VSZ values
        length=len(x)
        date_time.append(x[length-3]+" "+x[length-2])
        date_obj = []
        for temp in date_time:
            date_obj.append(datetime.strptime(temp, '%Y-%m-%d %H:%M:%S.%f'))
        dates = md.date2num(date_obj)
        vsz_len= len(vsz)                                           
        val=list(set(vsz))
        last=int(vsz[vsz_len-1])
        first=int(vsz[0])
        delta= last-first                                           #for each process, find difference between its first and last VSZ value i.e delta
        print('Process: '+process_name)
        if last > first:
            print("VSZ lastvalue is more than firstvalue.")
            #Data_Plotting(dates,vsz,process_name)
        elif last < first:
            print("VSZ lastvalue is less than firstvalue.")
        elif last == first:
            print("The first and last VSZ value are same.")
        if len(val)==1:                                             #to check if there are variations in vsz values or not
            print("All the VSZ values are same")
        else:
            print("There are variations seen in VSZ values across all values")    
        print("Delta: ",delta)
        print('\n')
                       
    
#fname=logfile, process_list=takes process list from config file,vsz_start & vsz_end= start and end strings, data between them will be used           
def access_pro(fname,process_list,vsz_start,vsz_end):           
    for x in process_list:
        process_data(vsz_start,vsz_end,x,fname)

