class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        total=0
        prev=-2
        for i in range (len(flowerbed)):
            if flowerbed[i]:
                total+=(i-prev-2)//2
                prev=i
        total+=(len(flowerbed)-prev-1)//2
        return total>=n 
        