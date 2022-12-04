student_scores = {
  "Harry": 95,
  "Ron": 97,
  "Hermione": 99, 
  "Draco": 96,
  "Neville": 92,
}


student_grades = {}


x = 0

for i in student_scores:
    x = student_scores[i]
    if x > 90:
        student_grades[i] = "outstanding"
    

print(student_grades)