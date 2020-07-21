def is_isogram(string):
    string = string.lower().replace(" ","")
    string = string.replace("-","")    
    return len(string)==len(set(string))