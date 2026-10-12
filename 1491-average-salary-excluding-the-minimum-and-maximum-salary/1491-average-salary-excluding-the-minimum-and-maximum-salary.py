class Solution:
    def average(self, salary: list[int]) -> float:
        salary.sort()
        new_s=salary[1:-1]
        sum_i=0
        n=len(new_s)
        for i in range(n):
            sum_i=sum_i+new_s[i]
        return sum_i/n
        