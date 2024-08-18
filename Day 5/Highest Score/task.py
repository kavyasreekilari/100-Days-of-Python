student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

max_score = max(student_scores)
print(f"Using max function max score is: {max_score}")

max_student_score = student_scores[0]
for score in student_scores:
    if score > max_student_score:
        max_student_score = score
        print(max_student_score)
print(f"Max student score using for loop: {max_student_score}")