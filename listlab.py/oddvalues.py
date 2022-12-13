new_list = []

def odd_list(List):
    
    for i in range(0,len(List)):
        if(List[i] % 2 !=0):
            new_list.append(List[i])
            
    
    return new_list
    
List = [51, 20, 24, 49, 69]
odd_list(List)

for x in range(len(new_list)):
    print(new_list[x],end=' ')
