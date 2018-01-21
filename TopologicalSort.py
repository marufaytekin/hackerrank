"""
execute dependent jobs
no cyclic dependency
job dic = {'a': ['b', 'c'], 'f': ['k', 'l'], 'c': ['d', 'e', 'f']}
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
    for job in stack:
        print job  # execute(job)


j = {'a': ['b', 'c'], 'f': ['k', 'l'], 'c': ['d', 'e', 'f']}

sort(j)
