import os.path
import shutil
import filecmp

#VARS
dataset = "/users/leandersparla/documents/test/start"
target = "/users/leandersparla/documents/test/ziel"
dirstocreate = []
filesalreadyexists = []
filestocheck = []
original = []
errorswhilecopy = []
originalerrorfile=[]

#HELPFUNCTIONS
def file(_input):
    return os.path.normpath(_input)

def check_validity(_dataset, _target):
    _temp_data_array = os.listdir(_dataset)
    for _temp_data in _temp_data_array:
        check_org = os.path.join(_dataset, _temp_data)
        print("Check of: ", check_org)
        if os.path.isfile(check_org):
            #print("Is File")
            if not _temp_data == '.DS_Store':
                if os.path.exists(os.path.join(_target, _temp_data)):
                    print("File exists in Target Folder!")
                    filesalreadyexists.append(check_org)
                #else:
                    #print("File does not yet exist")
                    #Throw Error
            else: 
                print("Ignore this file")
        else:
            print("Is Dir")
            if os.path.exists(os.path.join(_target, _temp_data)):
                print("Dir exists in target folder") 
            else:
                print("Have to create Dir in Target Folder")
                dirstocreate.append(os.path.join(_target,_temp_data))
            check_validity(os.path.join(_dataset,_temp_data),os.path.join(_target,_temp_data))
    return True

def copy(_dataset, _target):
    #DirsCreations auslagern? Muss nicht wenn array auf null gesetzt ist
    global dirstocreate
    if not dirstocreate == []:
        dirstocreate.sort(key=len)
        for dir in dirstocreate:
            dir = os.path.normpath(dir)
            print("Create Dir: ", dir)
            os.mkdir(dir)
            print("Created Dir: ", dir)
        print("Folderstructure copied")
        dirstocreate = []
    #else: 
        #print("Folderstructure was fine")
    _temp_data_array = os.listdir(_dataset)
    for _temp_data in _temp_data_array:
        _copy_file = os.path.join(_dataset, _temp_data)
        if os.path.isfile(_copy_file):
            if not os.path.exists(os.path.join(_target, _temp_data)):
                if not _temp_data == ".DS_Store": #errorcodes
                    if _temp_data not in filesalreadyexists:
                        print("Copy File: ", _copy_file)
                        shutil.copy2(_copy_file, _target)
                        print("Copy complete: ", _copy_file)
                        filestocheck.append(os.path.join(_target,_temp_data))
                        original.append(_copy_file)
        else:
            copy(os.path.join(_dataset, _temp_data), os.path.join(_target, _temp_data))

def check_file(_file, _copy): 
    #_temp = filecmp.cmp(_file, _copy, shallow=False)
    _temp = actual_check(_file,_copy)
    #print("Check of ", _file , "and ", _copy, _temp)
    #with open(_file, 'rb') as original:
     #   print("Opening ", _file)
      #  with open(_copy, 'rb') as copy:
       #     print("Opening ", _copy)
        #    while True:
         #       byte_original = original.read(1)
          #      if not byte_original:
           #         break
            #    byte_copy = copy.read(1)
             #   if not byte_original == byte_copy:
              #      print("Copy Failed!")
               #     return False
                #    exit
                 #   break
    #print(_file, "checked!")
    #return True
    return _temp

def getfiles():
    global dataset
    global target
    dataset = file(input("Enter File or Directory to be copied: "))
    while not os.path.exists(dataset) == True:
        dataset = file(input("Address not found. Enter File or Directory to be copied: "))
    _temp = input("Do you want to create a new folder as a destination? [Y/N]").upper()
    while _temp not in ["Y", "N"]:
        _temp = input("Input not valid. Do you want to create a new folder as a destination? [Y/N]").upper()
    if _temp == "Y":
        #target = file(input("Enter new folder adress"))
        #while not os.path.exists(file(os.path.split(target)[0])):
         #   print(os.path.split(target)[0])
          #  target = file(input("Not possibile to create desired folder. Please enter a adress where the subfolder does exist!"))
        #os.mkdir(target)
        target = newfolder()
    else:
        target = file(input("Enter Directory to be copied to: "))
        while not os.path.exists(target) == True:
            if os.path.isfile(target):
                target = file(input("Destination is a file. Enter Directory to be copied to: "))
            else: 
                target = file(input("Adress not found. Enter Directory to be copied to: "))
        #Check Files again
        if os.path.exists(dataset):
            if os.path.exists(target):
                print("Success")
                return True
    #Fehlercodes in Else
    return False

def newfolder():
    global target
    _target = file(input("Enter new folder adress"))
    while True:
        if not os.path.exists(file(os.path.split(_target)[0])):
            _target = file(input("Cannot create folder. Subdirectory does not exists. Please start with the first new folder or check adress."))
        elif os.path.exists(_target):
            _temp = input("Cannot create folder. Folder does exists. Do you want to use the folder?").upper()
            while not _temp in ["Y","N"]:
                _temp = input("No valid input. [Y/N").upper()
            if _temp == "Y":
                target=_target
                return _target
        else:
            break
    os.mkdir(_target)
    print(_target, "created.")
    _text = ("Should the directory be used as a destintation? Otherwise you can still create a subfolder [Y/N]")
    _temp = input(_text).upper()
    while _temp not in ["Y","N"]:
        _temp = input("No valid Input. [Y/N]").upper()
    if _temp == "N":
        target=_target
        newfolder()
    return _target

#org copy from filecmp
bufsize=0
def actual_check(file1, file2):
    bufsize=4*1024
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        while True:
            b1=f1.read(bufsize)
            b2=f2.read(bufsize)
            if b1!=b2:
                return False
            if not b1:
                return True

def init():
    print("Loading TRANSFER.PIE")
    print("TRANSFER.PIE 0.3.2.8")
    global dataset
    print("*")
    dataset = ""
    print("**")
    global target
    print("***")
    target = ""
    print("****")
    global dirstocreate
    print("*****")
    dirstocreate = []
    print("******")
    global  filesalreadyexists
    print("*******")
    filesalreadyexists = []
    print("********")
    global filestocheck
    print("*********")
    filestocheck = []
    print("**********")
    global original
    print("***********")
    original = []
    print("************")
    global errorswhilecopy
    print("*************")
    errorswhilecopy = []
    print("**************")
    global originalerrorfile
    print("***************")
    originalerrorfile = []
    print("****************")
    print("TRANSFER.PIE ready for use!\n\n")
    #print(dataset," >>> ", target)
    #print("Starting to check Files\n\n")

def main():
    init()
    getfiles()
    print(dataset," >>> ", target)
    print("Starting to check Files\n\n")
    check_validity(dataset, target)
    print("All files checked")
    if not filesalreadyexists == []:
        print("Found files that already exists in targetfolder.")
        for _file in filesalreadyexists:
            print(_file,)
        _input = input("Do you want to copy the other files anyways? [Y/N]").upper()
        while _input not in ["Y", "N"]:
            _input = input("No valid input. Do you want to copy the other files anyways? [Y/N]").upper()
        if _input == "Y":
            print("Copy ", dataset, " >>> ", target)
            copy(dataset, target)
        else:
            exit
    print("Copy ", dataset, " >>> ", target)  
    _temp=input("Is that correct?[Y/N] - Y will start copy and checking").upper()
    while not _temp in ["Y","N"]:
        _temp=input("No valid input [Y/N]").upper()  
    if _temp =="N":
        main()
    else:  
        copy(dataset,target)
        print("Copied ", dataset, " >>> ", target)
        print("Checking files")
    #for _file_copy in filestocheck:
        #    for _file_org in original:
        #       print("Checking ", _file_copy)
        #      check_file(_file_org,_file_copy)
        if not len(filestocheck) == len(original):
            print("ERROR CODE 001")
        else:
            i=0
            _temp=True
            while i<len(filestocheck):
                print("CHECK OF ", filestocheck[i], " and ", original[i])
                _temp = check_file(filestocheck[i],original[i])
                if _temp:
                    print("Copy of ", original[i], " successful.")
                else:
                    print("Error with file of ", filestocheck[i])
                    errorswhilecopy.append(filestocheck[i])
                    originalerrorfile.append(original[i])
                i+=1
            if errorswhilecopy:
                for _error in errorswhilecopy:
                    print("Error with the copy ", _error)
                #print("Error while copying ", original[i],". Copy is not the same as the original.")
        print("Thanks for using TRANSFER.PIE")

main()

#TODO
#FehlerCodes
#FEHLER IM CHECKEN!! - wegen Array. Vergleicht falsche Dateien, solved
#beim neuen ordner checken ob ordner schon besteht, solved
#Files neu kopieren nach Fehlerhafter kopie?
#Ladebalken