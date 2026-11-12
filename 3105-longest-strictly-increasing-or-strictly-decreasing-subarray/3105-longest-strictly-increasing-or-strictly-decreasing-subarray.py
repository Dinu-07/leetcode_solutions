class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        list_ = []
        list1 = []
        for i in nums:
            if not list_:
                list_.append([i])
                list1.append([i])
            else:
                if i > list_[-1][-1]:
                    list_[-1].append(i)
                    list1.append([i])
                elif i < list1[-1][-1]:
                    list1[-1].append(i)
                    list_.append([i])
                else:
                    list_.append([i])
                    list1.append([i])
        list_.sort(key = len , reverse = True)
        list1.sort(key = len , reverse = True)
        return len(list_[0]) if len(list_[0])>len(list1[0]) else len(list1[0])

                    
                
        return len(list_)

        