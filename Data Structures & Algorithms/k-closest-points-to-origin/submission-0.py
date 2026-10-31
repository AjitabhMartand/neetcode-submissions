class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i,j in points:
            cal = -(i**2+j**2)
            heapq.heappush(heap,[cal,i,j])
        while len(heap)>k:
            heapq.heappop(heap)
        res = []
        while heap:
            cal,x,y = heapq.heappop(heap)
            res.append([x,y])
        return res