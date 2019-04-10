

a=[1,[2,3,4,[5,6,7],8,9],10]
total=0
def list_sum(b):
    global total
    for x in b:
        print('x=',x)
        if isinstance(x,list):
            #print('x=',x)
            list_sum(x)
        
        else:
            total=total+x
            print('total=',total)
list_sum(a)
print(total)


'''
#################################################
a=[1,[1,1,1,[1,1,1],1,1],1]
total=0
def list_sum(b):
    global total
    if isinstance(b,list): 
        for x in b:
            return list_sum(x)
    else:
        total=total+b

list_sum(a)
print(total)
'''
