"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18]
"""
def merge_inetrvals(intervals):
    stack = []
    for interval in intervals:
        if not stack:
            stack.append(interval)
        else:
            x1, y1 = stack.pop()
            x2, y2 = interval
            if y1 >= x2:
                if y1 > y2:
                    stack.append((x1, y1))
                else:
                    stack.append((x1, y2))
            else:
                stack.append((x1, y1))
                stack.append(interval)
    return stack


test_data = [(1, 3), (2, 6), (8, 10), (15, 18)]

sorted_intervals = sorted(test_data, key=lambda x: x[0])

print "input: %s" % test_data
print "sorted: %s " % sorted_intervals

merged_intervals = merge_inetrvals(sorted_intervals)

print "output: %s" % merged_intervals
