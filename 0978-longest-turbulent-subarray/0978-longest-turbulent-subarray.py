class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:

        if len(arr) == 1:
            return 1

        ol_max = 1
        cur_count = 1

        expecting = -2
        
        for i in range(1, len(arr)):
            
            if expecting == -2:
                if arr[i] < arr[i-1]:
                    expecting = 1
                    cur_count += 1
                elif arr[i] > arr[i-1]:
                    expecting = -1
                    cur_count += 1
                else:
                    expecting = -2 
                    cur_count = 1
            elif expecting == 1:
                if arr[i] > arr[i-1]:
                    expecting = -1
                    cur_count += 1
                elif arr[i] < arr[i-1]:
                    expecting = 1
                    cur_count = 2
                else:
                    expecting = -2
                    cur_count = 1
            elif expecting == -1:
                if arr[i] < arr[i-1]:
                    expecting = 1
                    cur_count += 1
                elif arr[i] > arr[i-1]:
                    expecting = -1 
                    cur_count = 2
                else:
                    expecting = -2 
                    cur_count = 1

            ol_max = max(ol_max, cur_count)

        return ol_max





        
        