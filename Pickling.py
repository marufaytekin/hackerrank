import pickle

grades = {'Bart':75, 'Lisa':98, 'Milhouse':80, 'Nelson':65}

"""
with statement ensures that previously would use try ... finally block
to ensure that clean-up code is executed. It is used with uncontrolled
resources such as files.
"""
with open("data.p", "wb") as f:
    pickle.dump(grades, f, -1)


with open("data.p", "rb") as f:
    data = pickle.load(f)

for item in data:
    print item, data[item]