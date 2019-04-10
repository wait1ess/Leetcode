class Solution:
    def lengthOfLongestSubstring(self, T):
        last={}
        count=0
        record=[]
        l=len(T)
        for index,element in enumerate(T):
            if element in last:
                record.append(count)
                if count>=index-last[element]:
                    count=index-last[element]
                else: count=count+1
                #print(element,last[element])
                last[element]=index
            else:
                last[element]=index
                count=count+1
            if index==l-1:
                record.append(count)
            #print(count,last)
        print(record,last)
        if record==[]:
            return 0
        return max(record)
if __name__ == "__main__":
    s="tmmzuxt"
    answer=Solution().lengthOfLongestSubstring(s)
    print(answer)
