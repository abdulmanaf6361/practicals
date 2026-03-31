marks = int(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 45:
    print("Grade: D")
else:
    print("Grade: F")