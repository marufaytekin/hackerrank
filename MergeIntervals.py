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


my_list = [(1, 3), (6, 8), (2, 4), (5, 9)]

sorted_int = sorted(my_list, key=lambda x: x[0])
# [(1, 3), (2, 4), (5, 7), (6, 8)]

print "input: %s" % my_list
print "sorted: %s " % sorted_int

output = merge_inetrvals(sorted_int)

print "output: %s" % output
