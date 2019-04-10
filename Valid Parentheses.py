class Solution():
    def isValid(self, s):
        left_Parentheses={"(":1,"[":2,"{":3}
        right_Parentheses={")":1,"]":2,"}":3}
        stack=[]
        for element in s:
            if element in left_Parentheses:
                stack.append(element)
            elif element in right_Parentheses :
                if stack==[]: return False
                if left_Parentheses[stack.pop()]!=right_Parentheses[element]:
                    return False
        if stack==[]:
            return True
        else : return False

if __name__=="__main__":
    s="{["
    answer=Solution().isValid( s)
    print(answer)
