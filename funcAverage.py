# Function to find average Marks
def find_Average(marks):
    AverageSum = sum(marks)
    AverageTotal = len(marks)
    Average_Marks = AverageSum / AverageTotal
    return Average_Marks

# Function to compute Average Grade
def compute_grade(Average):
    if Average >= 90:
        grade = 'A'
    elif Average >= 70:
        grade = 'B'
    else:
        grade= 'C'
    return grade

marks = [145, 656, 137, 67, 78, 100]
Average = find_Average(marks)
print(f"Your average mark is {Average}")

grade = compute_grade(Average)
print(f"Your Grade is {grade}", Average)