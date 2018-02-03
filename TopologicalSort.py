"""
You are given  a list of jobs that someof them have dependencies. Execute these jobs in an order.
For example: In the following job dictionary,
job_dic = {'a': ['b', 'c'], 'f': ['k', 'l'], 'c': ['d', 'e', 'f']}
'a' can be executed after 'b' and 'c' are executed etc.

It is given that there is no cyclic dependency between the jobs.
"""


def dfs(k, jobs, visited, stack):
    visited[k] = True
    if k in jobs:
        for job in jobs[k]:
            if job not in visited:
                dfs(job, jobs, visited, stack)
    stack.append(k)


def sort(jobs):
    visited = {}
    stack = []
    for k in jobs:
        if k not in visited:
            dfs(k, jobs, visited, stack)
    return stack


j = {'a': ['b', 'c'], 'f': ['k', 'l'], 'c': ['d', 'e', 'f']}

print sort(j)
