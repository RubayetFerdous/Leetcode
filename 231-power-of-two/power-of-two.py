class Solution:
    def isPowerOfTwo(self, n: int ,k=0) -> bool:
        if 2**k==n:
            return True
        if 2**k>n:
            return False
        return self.isPowerOfTwo(n,k+1)
