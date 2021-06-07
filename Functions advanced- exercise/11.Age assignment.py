def age_assignment(*args,**kwargs):
    names = []
    result = {}
    for i in args:
        names.append(i)
    for name in names:
        for key,value in kwargs.items():
            if name.startswith(key):
                result[name] =value
    return result




print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))