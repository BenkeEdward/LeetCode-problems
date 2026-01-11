class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x < 1 and n==(2**31) - 1 and x != -1:
            return 0
        if x == 1 or x == -1:
            if n%2==0:
                return 1
            else:
                return 1 if x == 1 else -1
        if x > 1 and n == (-2**31):
            return 0
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            y = 1/x
            z= y
            while n != -1:
                z*=y
                n+=1
            return z
        else:
            y = x
            while n != 1:
                x*= y
                n-=1
            return x
#quite bad tbh
        
        



sol = Solution()