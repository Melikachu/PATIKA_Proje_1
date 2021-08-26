def reversed(List):
    for s in range(len(List)):
        m=List[s].reverse()
        n=m.reverse()
    return n

List=[[1,2,3,4,True,2],[1,2],[5,3]]
print(reversed(List))