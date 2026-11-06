"""
LeetCode 933 - Number of Recent Calls
Difficulty: Easy
Category: Queue / Deque

Design a RecentCounter class that counts the number of recent requests.

Implement the RecentCounter class:

- RecentCounter() initializes the counter with zero recent requests.
- ping(t) adds a new request at time t, where t represents milliseconds,
  and returns the number of requests that occurred within the past
  3000 milliseconds, inclusive.

In other words, return the number of requests that occurred in the range:

    [t - 3000, t]

It is guaranteed that every call to ping uses a strictly larger value of t
than the previous call.

Example:

Input:
ping(1)
ping(100)
ping(3001)
ping(3002)

Output:
1
2
3
3
"""

from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)

        while t - 3000 > self.requests[0]:
            self.requests.popleft()

        return len(self.requests)


counter = RecentCounter()

print(counter.ping(1))      # 1
print(counter.ping(100))    # 2
print(counter.ping(3001))   # 3
print(counter.ping(3002))   # 3