import bisect

def sliding_window_median(nums, k):
    if not nums or k == 0:
        return []
    window = sorted(nums[:k])
    medians = []
    for i in range(k, len(nums)+1):
        # Compute median
        if k % 2 == 1:
            medians.append(float(window[k//2]))
        else:
            medians.append((window[k//2-1] + window[k//2]) / 2)
        if i == len(nums):
            break
        # Remove outgoing element
        out_elem = nums[i-k]
        idx = bisect.bisect_left(window, out_elem)
        window.pop(idx)
        # Insert incoming element
        bisect.insort(window, nums[i])
    return medians

# User input
nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))
k = int(input("Enter the window size k: "))
print("Sliding window medians:", [int(x) for x in sliding_window_median(nums, k)])
