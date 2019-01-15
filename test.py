class Solution:
    # dictionary keys are tuples, storing results
    # structure of the tuple:
    # (level, prev_sum, val_to_include)
    # value is number of successful tuples

    def fourSumCount(self, A, B, C, D, prev_sum=0, level=0, sums={}):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # handle clearing dictionary between tests
        sums = {} if level == 3 else sums
        # base case:
        if level == 3:
            total = 0
            for num in D:
                if prev_sum + num == 0:
                    print("At level 3, 0 total found using entry w/ value {0}".
                          format(num))
                    total += 1
            return total
        total = 0
        lists = [A, B, C]
        for num in lists[level]:
            if level == 0:
                print(str(sums))
            if (level, prev_sum, num) in sums:
                total += sums[(level, prev_sum, num)]
                print("Used dictionary entry {0}, making total {1}".
                      format((level, prev_sum, num), total))
            else:
                print("Call from level {0} to level {1}; current sum is {2}".
                      format(level, level + 1, prev_sum + num))
                result = self.fourSumCount(A, B, C, D, prev_sum + num,
                                           level + 1, sums)
                sums[(level, prev_sum, num)] = result
                total += result
        if level == 0:
            sums = {}
            print(sums)
        return total

sol = Solution()
A = [1]
B = [-1]
C = [0]
D = [1]
result = sol.fourSumCount(A, B, C, D)
print("Test 1: {0}".format(result))
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
result = sol.fourSumCount(A, B, C, D)
print("Test 2: {0}".format(result))
