import os.path
import shutil

#VARS
dataset = "/users/leandersparla/documents/test/start"
target = "/users/leandersparla/documents/test/ziel"
dirstocreate = []

#HELPFUNCTIONS
def file(_input):
    return _input

def check_validity(_dataset, _target):
    _temp_data_array = os.listdir(_dataset)
    #_temp_target_array = os.listdir(_target)
    for _temp_data in _temp_data_array:
        check_org = os.path.join(_dataset, _temp_data)
        print("Check of: ", check_org)
        if os.path.isfile(check_org):
            print("Is File")
            if not _temp_data == '.DS_Store':
                if os.path.exists(os.path.join(_target, _temp_data)):
                    print("File exists in Target Folder!")
                else:
                    print("File does not yet exist")
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
        for dir in dirstocreate:
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
                print("Copy File: ", _copy_file)
                shutil.copy2(_copy_file, _target)
                print("Check File: ", _copy_file)
                check_file(_copy_file,os.path.join(_target,_temp_data))
        else:
            copy(os.path.join(_dataset, _temp_data), os.path.join(_target, _temp_data))

def check_file(_file, _copy): 
    with open(_file, 'rb') as original:
        with open(_copy, 'rb') as copy:
            while True:
                byte_original = original.read(1)
                if not byte_original:
                    break
                byte_copy = copy.read(1)
                if not byte_original == byte_copy:
                    print("Copy Failed!")
                    return False
    print(_file, "checked!")
    return True

print(check_validity(dataset, target))
copy(dataset, target)


#TODO
#Copy of _DS.Store abfangen
#Init schreiben
#Fehler abfangen und Fehlermeldung bei falschem Copy