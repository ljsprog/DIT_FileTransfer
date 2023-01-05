#imports
import os
import shutil

#variables
copy=""
dest=""
bybyby=True
process=""
#helpfunctions
#checkifexists(dir/file)
    #global copy
    #if not copy:
    #    copy=os.path.normpath(input("Enter File or Directory to be copied: \n"))
    #while not os.path.exists(copy):
    #    copy=os.path.normpath(input("File or Directory not found. Please enter valid adress: \n"))
    #return True
def check_validity(_copy, _dest):
    #check if copy is file or dir. only works with dir.. create code for file
    if(os.path.isfile(_copy)):
        _tempdest = os.listdir(_dest)
        _tempdest = [_temp.lower() for _temp in _tempdest]
        if os.path.split(_copy)[1].lower() in _tempdest:
            return False
        else: 
            return True
    _tempcopy = os.listdir(_copy)
    _tempdest = os.listdir(_dest)
    for _filecopy in _tempcopy:
        if not os.path.isfile(os.path.join(_copy,_filecopy)):
            print("IS DIR: ", _filecopy)
            if os.path.exists(os.path.join(_dest,_filecopy)):
                print("Dir existiert schon. ", os.path.join(dest, _filecopy))
                if not check_validity(os.path.join(_copy,_filecopy),os.path.join(_dest,_filecopy)):
                    print("Files in Subfolder already exists")
                    return False
                #join scheint falschen path zu geben. check_validity(os.path.join(_copy,_filecopy), os.path.join(_dest,_filecopy))
            else:
                print("Dir existiert noch nicht")
                
            
                #WHAT TO DO HERE?   
                
        else:
            if not _filecopy == '.DS_Store':
                if _filecopy in _tempdest:
                    print(_filecopy, " existiert schon in ", _dest)
                    return False    
    return True 

def checkfile_bybyby(_file,_copy):
    with open(_file, 'rb') as original:
        with open(_copy, 'rb') as copy:
            while True:
                byte_original = original.read(1)
                if not byte_original:
                    break
                byte_copy = copy.read(1)
                if not byte_original == byte_copy:
                    print("Copy failed.")
                    return False
    print(_file, "geprüft.")
    return True

#functions
def init():
    #alle vars setzen
    global copy
    global dest
    global bybyby
    copy=""
    dest=""
    bybyby=True
    print("***********************")
    print("******WELCOME**********")
    print("***********************\n")
    ###weiter lines
    bybyby_input = input("Should files be checked Byte by Byte? If not, only metadatas will be compared. [Y/N]\n").upper()
    bybyby_input = "Y"
    while bybyby_input not in ["Y","N"]:
        bybyby_input = input("No valid data. Should files be checked Byte by Byte? If not, only metadatas will be compared. [Y/N\n")
    if bybyby_input == "N":
        bybyby = False
    

def load_directories():
    global copy
    global dest
    #if not copy:
    copy=os.path.normpath(input("Enter File or Directory to be copied: \n"))
    while not os.path.exists(copy):
        copy=os.path.normpath(input("File or Directory not found. Please enter valid adress: \n"))
    #if not dest:
    dest=os.path.normpath(input("Enter destination to be copied to: \n"))
    while not os.path.exists(dest) or os.path.isfile(dest):
        dest=os.path.normpath(input("Please enter valid destination: \n"))
        #Unterschied ob Fehler wegen file oder nicht existent
    if check_validity(copy, dest):
        if os.path.isfile(copy):
            return "file"
        else:
            return "dir"
    else:
        print(check_validity(copy,dest))
        print("Files already exist in Destination. Please change parameters.")
        load_directories()

def copy_file(_file,_dest,_bybyby):
    shutil.copy2(_file, _dest)  
    print("Copy complete of file: ", _file,". Begin to check file")
    if _bybyby:
        if(checkfile_bybyby(_file,os.path.join(dest,os.path.split(_file)[1]))):
            print("Copy ok.")
            return True
        else:
            print("Copy not ok. Abort")
            return False
    else:
        print("check not possible")
    
def copy_dir(_copy,_dest,_bybyby):
    _tempcopy = os.listdir(_copy)
    
#copyfile - check ob file existiert im ziel, copy, checken
#copydir - checken ob dateien besteht. Wen file dann copyfile, sonst mkdir

#main
init()
start_prog = input("To start the programm, enter START").upper()
start_prog = "START"
while start_prog != "START":
    start_prog = input("No valid data. To...\n")
if start_prog == "START":   
    process = load_directories()
    print(process, " CHECK 1")
    if load_directories()=="file":  
        print("File")
        copy_file(copy,dest,bybyby)
    else:
        print("Dir")
    exit
#Check FILE oder DIR, aber durch Eingabe ->get Eingabe
#copy dir oder
#copy file


#TODO
#bybyby eingabe
#    /Users/leandersparla/Documents/Test/