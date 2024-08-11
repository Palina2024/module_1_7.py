grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnn', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(sorted(students))
print(students)
grades = [int(sum(grades[0])) / len(grades[0]), int(sum(grades[1])) / len(grades[1]), int(sum(grades[2])) / len(grades[2]), int(sum(grades[3])) / len(grades[3]), int(sum(grades[4])) / len(grades[4])]
print(grades)
a = {students[0]: grades[0], students[1]: grades[1], students[2]: grades[2], students[3]: grades[3], students[4]: grades[4]}
print(a)

