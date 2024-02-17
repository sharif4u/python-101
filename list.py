subjects = ['bangla', 'english', 'math', 'science']
print(subjects)
print(subjects[1])
print(subjects[-1])
sub = ['c', 'c++', 'java', 'python']
#for find length of list
print(len(sub))
# add items using append and insert
sub.append(5)
sub.insert(3,"j")
print(sub)
sub.remove(sub[3])
print(sub)
print(sub.pop())
print(sub.pop())
# item clear
print(sub.clear())
newlist = subjects.copy()
print(newlist)
# check item position in list
pos = newlist.index('math')
print(pos)
print(newlist.count('math'))

