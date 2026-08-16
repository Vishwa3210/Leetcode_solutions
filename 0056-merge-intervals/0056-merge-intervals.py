class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged_list=[]
        initial=intervals[0]
        for i in intervals[1:]:
            if i[0]<=initial[1]:
                initial[1]=max(initial[1],i[1])
                
                
            else:
                merged_list.append(initial)
                initial=i  
        merged_list.append(initial) 

        return merged_list
        