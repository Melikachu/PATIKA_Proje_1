def flatten(List):
    flatten_s=[s for l in List for s in l]
    return flatten_s
    

List=[["1,2,3,4",True,"2"],((1,2)),"Python"*2]    
print (flatten(List))    