class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_dict = {}
    
        for i in nums:
            if i in num_dict:
                num_dict[i] += 1

            else:
                num_dict[i] = 1

        # sorting in desc order based on the values of num_dict specified through key 
        sorted_num_dict = sorted(num_dict.items(), key=lambda x:x[1], reverse=True)
        
        #sorted_num_dict[:k] -> taking k most frequent elements           
        
        return [ item[0] for item in sorted_num_dict[:k] ]