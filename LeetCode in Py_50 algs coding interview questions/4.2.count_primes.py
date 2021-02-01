# https://leetcode.com/problems/count-primes/
# 204. Count Primes

import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if (n < 2):
            return 0
        isPrime = [True]*n
        isPrime[0] = isPrime[1] = False

        for i in range(2, int(math.ceil(math.sqrt(n)))):
            if (isPrime[i]):
                for multiples_of_i in range(i*i, n, i):
                    isPrime[multiples_of_i] = False
        return sum(isPrime)

    def countPrimes_(self, n: int) -> int:
        ctr = 0

        for num in range(n):
            if num <= 1:
                continue
            for i in range(2, num):
                if num%i == 0:
                    break
            else:
                ctr += 1
        return ctr


s = Solution()
print(s.countPrimes(10))
print(s.countPrimes_(10))