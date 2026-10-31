class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i,j in points:
            cal = (i**2+j**2)
            heapq.heappush(heap,[cal,i,j])
        res=[]
        for _ in range(k):
            dist,x,y=heapq.heappop(heap)
            res.append([x,y])
        return res
