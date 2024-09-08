'''2. Write a program to accept marks of 6 students and display them in a sorted
manner.'''

marks = []

m_a = int(input("Enter marks: "))
marks.append(m_a)
m_b = int(input("Enter marks: "))
marks.append(m_b)
m_c = int(input("Enter marks: "))
marks.append(m_c)
m_d = int(input("Enter marks: "))
marks.append(m_d)
marks.sort()
print(marks)