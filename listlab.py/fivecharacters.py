def upperCase(s):
    if(len(s) > 5):
        news = s.upper()
    else:
        return s
    
    return news
    
# calling fnc upperFnc
print(upperCase("college")) 
print(upperCase("remote")) 
print(upperCase("sports"))
print(upperCase("fair"))
print(upperCase("hat")) 
