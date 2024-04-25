#Created a 2 dimensional list based on values given in instructions. I also modified the lists by ussing the append, remove, and concatenate functions. 

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics","calculus","poetry","history"]
grades = [98,97,85,88]
grade_book = [["physics", 98],["calculus", 97],["poetry", 85],["history", 88]]
print(grade_book)

grade_book.append(["computer science", 100])
grade_book.append(["visual arts", 93])

grade_book[-1][-1] = 98
print(grade_book)

grade_book[2].remove(85)
grade_book[2].append("Pass")
print(grade_book)

full_gradebook = last_semester_gradebook + grade_book
print(full_gradebook)
