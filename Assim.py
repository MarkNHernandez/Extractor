#This program receives data from a converted pdf file and then outputs selected data to a txt
#file so that it can easily be added to an excel spreadsheet. It was used to quickly and easily transfer
#data from pdfs to an excel sheet (which was required by the customer)

def Data(filename): 
    with open(filename, 'r') as g:
        numbers = g.readlines()
        data = dict(enumerate(numbers))
    title = filename[38:-8]
    month = data[58][5:7]
    day = data[58][8:10]
    year = data[58][:4]
    date = "{}/{}/{}".format(month, day, year)
    row1 = data[119].strip()
    row2 = data[121].strip()
    row3 = data[123].strip()
    package = "{}, {}, {}, {}, {}\n".format(title,date,row1,row2,row3)
    #print(package)
    fo = open('data.txt', 'a')
    fo.write(package)
    fo.close

with open('dir.txt', 'r') as d:
    for i in d:
        name = i.strip("\n")
        #print(name)
        if (name.find('Blank') != -1):
            pass
        else:
            Data(name)

