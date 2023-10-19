student_marks=[78,83,90,88,75]
def sum(student_marks):
    total=0
    for x in student_marks:                            # sum all items in the list
        total +=x
    return total
sum(student_marks)
print(f"The sum of the items in the student marks list is {sum(student_marks)}")


student_marks=[78,83,90,88,75]
print(student_marks[0:1])     # first mark
print(student_marks[4:5])     # last mark

student_marks.append(96)
print(student_marks)         # adding 96 to the list

student_marks[0]=87
print(student_marks)         # updating student mark of 78 to 87