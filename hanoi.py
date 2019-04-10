def hanoi(n,prime,support,target):
    if n==1:
        print(prime,"-->",target)          # 递归终点
    else:
        hanoi(n-1,prime,target,support)    # 递归关系1
        
        print(prime,'-->',target)
        
        hanoi(n-1,support,prime,target)    # 递归关系2


n=int(input("please input a integer:"))
hanoi(n,'x','y','z')
