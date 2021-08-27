def melike(l):
    new=[]
    for i in l:
        i.reverse()
        new.append(i)
    
    new.reverse()
    return new

List=[[1,2,3,4,1,2],[1,2],[5,3]]
print(melike(List))