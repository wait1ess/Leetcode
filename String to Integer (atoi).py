class Solution:
    def myAtoi(self, str):
        answer=""
        nums = {'1','2','3','4','5','6','7','8','9','0'}
        sign={"+","-"}
        for element in str:
            if element in nums:
                answer+=element
            elif element!=" " and element not in sign or element in sign and answer!="":
                break
            elif element==" " and answer!="":
                break
            if answer=="" and element in sign  :
                answer+=element

        if answer=="" or answer in sign :return 0
        answer=int(answer)
        if answer<-2147483648:return -2147483648
        if answer>2147483647:return 2147483647
        return answer

if __name__=="__main__":
    s="  -4  2  "
    answer=Solution().myAtoi(s)
    print(answer)

