class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1

        item = []
        for key, value in map.items():
            item.append((key, value))

        item.sort(key=lambda x: x[1], reverse=True)
        return [x[0] for x in item[:k]]
        

            
        