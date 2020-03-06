from typing import List
def prime_filter(n: int) -> List[int]:
    visited = [False] * (n+1)
    prime = []
    for i in range(2, n+1):
        if not visited[i]:
            prime.append(i)
        for j in range(len(prime)):
            if i * prime[j] > n:
                break
            visited[i*prime[j]] = True
            if i % prime[j] == 0:
                break
        print (prime)
    return prime

print (prime_filter(19))