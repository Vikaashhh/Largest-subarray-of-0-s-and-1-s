class Solution:
    def maxLen(self, arr):
        # Step 1: Replace all 0s with -1s to convert the problem
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[i] = -1

        # Step 2: Initialize a map to store prefix sum and its first index
        prefix_map = {}
        max_len = 0
        curr_sum = 0

        for i in range(len(arr)):
            curr_sum += arr[i]  # prefix sum banao

            if curr_sum == 0:
                # agar sum 0 hai, matlab 0 to i tak subarray balanced hai
                max_len = i + 1

            if curr_sum in prefix_map:
                # agar same sum pehle aaya hai, tab uske baad se leke ab tak ka sum zero hoga
                length = i - prefix_map[curr_sum]
                max_len = max(max_len, length)
            else:
                # sirf pehli baar aane par hi index store karo
                prefix_map[curr_sum] = i

        return max_len
