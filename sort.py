students = ["Peter", "Barry", "Tony","Raven","Pearl"]
students.sort()
students.sort(reverse = True)
sorted_students = sorted(students)
for i in sorted_students:
    print(i)
for i in students:
    print(i)
students = [("Peter", "B", 30), 
            ("Barry", "A", 20),  
            ("Tony", "F", 36),
            ("Raven", "C", 50),
            ("Pearl", "D", 25)]
grade = lambda grades:grades[1]
students.sort(key=grade)
for i in students:
    print(i)
